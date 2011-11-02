
#include <unistd.h>
#include "lib.h"
#include "lproto.h"
#include <ctype.h>
#include <arpa/inet.h>

#define HP_CACHE_SIZE 1200
#define HP_VALID_PERIOD (24*60*60)
static struct {
    struct hostent hp;
    time_t cacheTime;
    time_t lastAccessTime;
} hpCache[HP_CACHE_SIZE];
static int firstHPCache = TRUE;

static int cpHostent(struct hostent *, struct hostent *);
static void freeHp(struct hostent *);
static struct hostent *getHpCache(char *);
static struct hostent *putHpCache(char *, struct hostent *);
static struct hostent *getHpCacheByAddr(char *);
static struct hostent *my_gethostbyaddr(char *);

char *
ls_getmyhostname(void)
{
   static char hname[MAXHOSTNAMELEN];
   struct hostent *hp;

   if (hname[0] == 0) {
       gethostname(hname, MAXHOSTNAMELEN);
       hp = Gethostbyname_(hname);
       if (hp != NULL) {
           strcpy(hname, hp->h_name);
       } else {
           hname[0] = 0;
           return(NULL);
       }
   }

   return hname;
}

#define MY_HOSTSFILE "hosts"
#define MY_LINESIZE 1024
#define MY_NUMALIASES 36

struct hostent *
my_gethostbyname(char *name)
{
    FILE *hfile;
    static char buf[MY_LINESIZE];
    char *addrstr;
    static struct hostent host;
    static char *names[MY_NUMALIASES], *addrs[2];
    static u_int addr;
    int n, found = 0;

    if (initenv_(NULL, NULL) < 0)
        return NULL;

    sprintf(buf, "%s/%s", genParams_[LSF_CONFDIR].paramValue, MY_HOSTSFILE);

    if ((hfile = fopen(buf, "r")) == NULL)
        return NULL;

    while (fgets(buf, MY_LINESIZE, hfile)) {
        char *tmp;
        n = 0;

        if ((tmp = strpbrk (buf, "\n#")))
            *tmp='\0';

        if ((addrstr = strtok (buf, " \t")))
            continue;

        addr = inet_addr(addrstr);

        while ((names[n] = strtok(NULL, " \t"))) {
            if (equalHost_(names[n], name))
                found++;
            n++;
        }

        if (found) {
            host.h_name = names[0];
            host.h_aliases = names + 1;
            host.h_addrtype = AF_INET;
            host.h_length = sizeof(addr);
            addrs[1] = NULL;
            addrs[0] = (char *)&addr;
            host.h_addr_list = addrs;
            fclose(hfile);

            return(&host);
        }
    }

    fclose(hfile);

    return NULL;
}

struct hostent *
Gethostbyname_(char *hname)
{
    char *sp;
    char *strip;
    struct hostent *hp;
    int hnlen;
    static struct hostent hostent;
    static char lsfHname[MAXHOSTNAMELEN];
    char lhname[MAXHOSTNAMELEN];

    if (strlen(hname) >= MAXHOSTNAMELEN) {
        lserrno = LSE_BAD_HOST;
        return NULL;
    }

    strcpy(lsfHname, hname);
    strToLower_(lsfHname);
    strcpy(lhname, lsfHname);

    if ((hp = getHpCache(lsfHname)))
        return hp;

    if ((hp = my_gethostbyname(lsfHname)) == NULL)
        hp = gethostbyname(lsfHname);

    if (! hp) {
        lserrno = LSE_BAD_HOST;
        return NULL;
    }

    memcpy((char *)&hostent, (char *) hp, sizeof (struct hostent));
    hostent.h_name = lsfHname;
    strcpy(hostent.h_name, hp->h_name);

    if (stripDomains_ != NULL) {

        hnlen = strlen(hostent.h_name);
        for (strip = stripDomains_ ; *strip ; strip += (*strip + 1)) {

            if (*strip >= hnlen)
                     continue;

            sp = hostent.h_name + hnlen - *strip;
            if (strncasecmp(sp, (strip + 1), *strip) == 0) {
                if (sp > hostent.h_name && sp[-1] == '.')
                    sp[-1] = '\0';
                else
                    *sp = '\0';
                break;
            }
        }
    }

    strToLower_(hostent.h_name);
    putHpCache(lhname, &hostent);

    return hp;

}  /* Gethostbyname_ */


static struct hostent *
putHpCache(char *hname, struct hostent *hp)
{
    time_t now, oldestTime = 0;
    int oldest = 0, i, j;
    char **t;

    time(&now);

    for (i = 0; i < HP_CACHE_SIZE; i++) {
        if (hpCache[i].hp.h_name == NULL) {
            break;
        } else if (hpCache[i].cacheTime - now > HP_VALID_PERIOD) {
            freeHp(&hpCache[i].hp);
            break;
        }

        if (hpCache[i].lastAccessTime > oldestTime)
            oldest = i;
    }

    if (i == HP_CACHE_SIZE) {
        i = oldest;
        freeHp(&hpCache[i].hp);
    }

    if (cpHostent(&hpCache[i].hp, hp) == -1) {
        return (NULL);
    }

    hpCache[i].cacheTime = now;
    hpCache[i].lastAccessTime = now;

    if (! equalHost_(hname, hpCache[i].hp.h_name)) {
        for (j = 0; hpCache[i].hp.h_aliases[j]; j++) {
            if (equalHost_(hname, hpCache[i].hp.h_aliases[j]))
                break;
        }
        if (!hpCache[i].hp.h_aliases[j]) {
            if ((t = (char **) realloc((char *) hpCache[i].hp.h_aliases,
                                       (j + 2) * sizeof(char *)))) {
                hpCache[i].hp.h_aliases = t;
                if ((hpCache[i].hp.h_aliases[j] = putstr_(hname)))
                    hpCache[i].hp.h_aliases[j+1] = NULL;
            }
        }
    }

    return (&hpCache[i].hp);
}


static struct hostent *
getHpCache(char *hname)
{
    time_t now;
    int i, j;

    if (firstHPCache) {
        for (i = 0; i < HP_CACHE_SIZE; i++) {
            hpCache[i].hp.h_name = NULL;
        }
        firstHPCache = FALSE;
        return (NULL);
    }

    time(&now);

    for (i = 0; i < HP_CACHE_SIZE; i++) {
        if (hpCache[i].hp.h_name) {
            if (now - hpCache[i].cacheTime < HP_VALID_PERIOD) {
                if (equalHost_(hpCache[i].hp.h_name, hname)) {
                    hpCache[i].lastAccessTime = now;
                    return (&hpCache[i].hp);
                }
                for (j = 0; hpCache[i].hp.h_aliases[j]; j++) {
                    if (equalHost_(hpCache[i].hp.h_aliases[j], hname)) {
                        hpCache[i].lastAccessTime = now;
                        return (&hpCache[i].hp);
                    }
                }
            } else {
                freeHp(&hpCache[i].hp);
            }
        }
    }

    return (NULL);
}

static void
freeHp(struct hostent *hp)
{
    int i;

    for (i = 0; hp->h_addr_list[i]; i++)
        free(hp->h_addr_list[i]);
    free(hp->h_addr_list);

    for (i = 0; hp->h_aliases[i]; i++)
        free(hp->h_aliases[i]);
    free(hp->h_aliases);

    free(hp->h_name);
    hp->h_name = NULL;
}

static int
cpHostent(struct hostent *to, struct hostent *from)
{
    int i, j, n;

    if ((to->h_name = putstr_(from->h_name)) == NULL)
        return (-1);

    for (n = 0; from->h_aliases[n]; n++);

    if ((to->h_aliases = (char **) calloc(n+1, sizeof(char *))) == NULL) {
        free(to->h_name);
        to->h_name = NULL;
        return (-1);
    }

    for (j = 0; j < n; j++) {
        if ((to->h_aliases[j] = putstr_(from->h_aliases[j])) == NULL) {
            while(j--)
                free(to->h_aliases[j]);
            free(to->h_aliases);
            free(to->h_name);
            to->h_name = NULL;
            return (-1);
        }
    }
    to->h_aliases[n] = NULL;


    to->h_addrtype = from->h_addrtype;
    to->h_length = from->h_length;

    for (n = 0; from->h_addr_list[n]; n++)
        ;

    if ((to->h_addr_list = (char **) calloc(n+1, sizeof(char *))) == NULL) {
        for (j = 0; to->h_aliases[j]; j++)
            free(to->h_aliases[j]);
        free(to->h_aliases);
        free(to->h_name);
        to->h_name = NULL;
        return (-1);
    }

    for (i = 0; i < n; i++) {
        if ((to->h_addr_list[i] = (char *) malloc(from->h_length)) == NULL) {
            while(i--)
                free(to->h_addr_list[i]);
            free(to->h_addr_list);
            for (j = 0; to->h_aliases[j]; j++)
                free(to->h_aliases[j]);
            free(to->h_aliases);
            free(to->h_name);
            to->h_name = NULL;
            return (-1);
        }
        memcpy(to->h_addr_list[i], from->h_addr_list[i], from->h_length);
    }

    to->h_addr_list[n] = NULL;
    return (0);
}

static struct hostent *
getHpCacheByAddr(char *addr)
{

    time_t now;
    int i, j;

    if (firstHPCache) {
        for (i = 0; i < HP_CACHE_SIZE; i++) {
            hpCache[i].hp.h_name = NULL;
        }
        firstHPCache = FALSE;
        return (NULL);
    }

    time(&now);

    for (i = 0; i < HP_CACHE_SIZE; i++) {
        if (hpCache[i].hp.h_name) {
            if (now - hpCache[i].cacheTime < HP_VALID_PERIOD) {
                for (j = 0; hpCache[i].hp.h_addr_list[j]; j++) {
                    if (!memcmp(addr, hpCache[i].hp.h_addr_list[j],
                                hpCache[i].hp.h_length)) {
                        hpCache[i].lastAccessTime = now;
                        return (&hpCache[i].hp);
                    }
                }
            } else {
                freeHp(&hpCache[i].hp);
            }
        }
    }

    return (NULL);
}

static struct hostent *
my_gethostbyaddr(char *faddr)
{
    FILE *hfile;
    static char buf[MY_LINESIZE];
    char *addrstr;
    static struct hostent host;
    static char *names[MY_NUMALIASES], *addrs[2];
    static u_int addr;
    int n;

    if (initenv_(NULL, NULL) < 0)
        return NULL;

    sprintf(buf, "%s/%s", genParams_[LSF_CONFDIR].paramValue, MY_HOSTSFILE);

    if (NULL == (hfile = fopen (buf, "r")))
        return((struct hostent *)NULL);

    while (NULL != fgets (buf, MY_LINESIZE, hfile)) {
        char *tmp;
        n = 0;

        /* get rid of newlines and comments */
        if (NULL != (tmp = strpbrk (buf, "\n#")))
            *tmp='\0';

        /* get address, skip blank lines */
        if (NULL == (addrstr = strtok (buf, " \t")))
            continue;

        addr = inet_addr (addrstr);
#ifdef _CRAY
        addr <<= 32;
        if (logclass & LC_TRACE)
            ls_syslog(LOG_DEBUG, "my_gethostbyaddr: addr %x faddr %x",
                      addr, (*(u_int *) faddr));
#endif /* cray */

        if (!memcmp((char *) &addr, faddr, sizeof(u_int))) {
            while (NULL != (names[n] = strtok(NULL, " \t"))) {
                n++;
            }

            host.h_name = names[0];
            host.h_aliases = names+1;
            host.h_addrtype = AF_INET;
            host.h_length = sizeof(addr);
            addrs[1] = NULL;
            addrs[0] = (char *)&addr;
            host.h_addr_list = addrs;
            fclose(hfile);
            return(&host);
        }
    }
    fclose(hfile);
    return((struct hostent *)NULL);
} /* my_gethostbyaddr */



/*
 *--------------------------------------------------------------------------
 *  Gethostbyaddr_(addr, len, type) --
 *
 *     Return official host entry given an address.  Multiple addresses
 * for a given host are cached.
 *
 *------------------------------------------------------------------------
 */
struct hostent *
Gethostbyaddr_(char *addr, int len, int type)
{
    struct hostent *hp;
    char hname[MAXHOSTNAMELEN];
    char **t;
    int i;

    if (logclass & LC_TRACE)
        ls_syslog(LOG_DEBUG, "Gethostbyaddr_: %x %x %x %x len %d",
                  addr[0], addr[1], addr[2], addr[3], len);
#ifdef _SPP_UX
    /* In the buggy SPP-UX 4.2, type = 0, this is used to fix it */
    type = AF_INET;
#endif

    if ((hp = getHpCacheByAddr(addr))) {
        return (hp);
    }

    if ((hp = my_gethostbyaddr(addr)) == NULL) {
        if ((hp = gethostbyaddr(addr, len, type)) == NULL) {
            lserrno = LSE_BAD_HOST;
            return (NULL);
        }
    }

    strcpy(hname, hp->h_name);
    if ((hp = Gethostbyname_(hname)) == NULL)
        return (NULL);

    /* Add the new address if hp is from cache.  This is a hack. */
    for (i = 0; i < HP_CACHE_SIZE; i++) {
        if (hp == &hpCache[i].hp)
            break;
    }

    if (i == HP_CACHE_SIZE) /* hp is not from cache */
        return (hp);

    for (i = 0; hp->h_addr_list[i]; i++) {
        if (!memcmp(hp->h_addr_list[i], addr, hp->h_length))
            return (hp);
    }

    if ((t = (char **) realloc((char *) hp->h_addr_list,
                               (i + 2) * sizeof(char *))) == NULL)
        return (hp);

    hp->h_addr_list = t;

    if ((hp->h_addr_list[i] = (char *) malloc(hp->h_length)) == NULL)
        return (hp);

    memcpy(hp->h_addr_list[i], addr, hp->h_length);
    hp->h_addr_list[i+1] = NULL;
    return (hp);
} /* Getbostbyaddr_ */

#define ISBOUNDARY(h1, h2, len)  ( (h1[len]=='.' || h1[len]=='\0') && \
                                (h2[len]=='.' || h2[len]=='\0') )

/*
 *------------------------------------------------------------------------
 *
 *  equalHost_ --
 *
 *     Check if host1 and host2 are the same host.
 *     nosy.white, nosy, nosy.white.toronto.edu will be considered equal.
 *
 *     nosy and nosy1 will not be equal.
 *
 *     nosy.white.toronto.edu and nosy.cs.york.edu are not eaul.
 *
 *     Return TRUE if same, otherwise return FALSE.
 *------------------------------------------------------------------------
*/
int
equalHost_(const char *host1, const char *host2)
{
    int len;

    if (strlen(host1) > strlen(host2))
        len = strlen(host2);
    else
        len = strlen(host1);

    /* Note: nosy and nosy1 are not the same. nosy and nosy.white are
     * the same.
     */
    if ((strncasecmp(host1, host2, len) == 0) && ISBOUNDARY(host1, host2, len))
        return TRUE;

    return FALSE;
} /* equalHost_ */

/*
 *----------------------------------------------------------------------
 *
 *  sockAdd2Str_ -
 *
 *  Convert socket address into a string: a.b.c.d:p,
 *  where p is the port number.
 *----------------------------------------------------------------------
*/
char *
sockAdd2Str_(struct sockaddr_in *from)
{
    static char adbuf[24];

    sprintf(adbuf, "\
%s:%d", inet_ntoa(from->sin_addr), (int)ntohs(from->sin_port));
    return adbuf;

} /* sockAdd2Str_ */
