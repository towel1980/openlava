
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "lib.h"
#include "lproto.h"
#include "lib.table.h"

#define MAX_HOSTALIAS 64
#define MAX_HOSTIPS   32

static hTab *nameTab;
static hTab *addrTab;

static int mkHostTab(void);
static void stripDomain(char *);
static void addHost2Tab(const char *,
                        in_addr_t **,
                        char **);
/* ls_getmyhostname()
 */
char *
ls_getmyhostname(void)
{
   static char hname[MAXHOSTNAMELEN];
   struct hostent *hp;

   if (hname[0] != 0)
       return hname;

   gethostname(hname, MAXHOSTNAMELEN);
   hp = Gethostbyname_(hname);
   if (hp == NULL) {
       hname[0] = 0;
       return NULL;
   }

   strcpy(hname, hp->h_name);

   return hname;
}

/* Gethostbyname_()
 */
struct hostent *
Gethostbyname_(char *hname)
{
    int cc;
    hEnt *e;
    struct hostent *hp;
    char lsfHname[MAXHOSTNAMELEN];

    if (strlen(hname) >= MAXHOSTNAMELEN) {
        lserrno = LSE_BAD_HOST;
        return NULL;
    }

    strcpy(lsfHname, hname);
    /* openlava strips all hostnames
     * of thier domain names and lowercase
     * them.
     */
    stripDomain(lsfHname);
    strToLower_(lsfHname);

    if (nameTab == NULL)
        mkHostTab();

    e = h_getEnt_(nameTab, lsfHname);
    if (e) {
        hp = e->hData;
        return hp;
    }

    hp = gethostbyname(lsfHname);
    if (hp == NULL) {
        lserrno = LSE_BAD_HOST;
        return NULL;
    }

    /* add the new host to the host hash table
     */
    addHost2Tab(hp->h_name,
                (in_addr_t **)hp->h_addr_list,
                hp->h_aliases);

    cc = 0;
    while (hp->h_addr_list[cc]) {
        { /* dybag */
            char *p;
            struct in_addr a;
            memcpy(&a, hp->h_addr_list[cc], sizeof(a));
            p = inet_ntoa(a);
            fprintf(stderr, "%s\n", p); /* could be closed */
            ++cc;
        }
    }

    return hp;
}

/* Gethostbyaddr_()
 */
struct hostent *
Gethostbyaddr_(in_addr_t *addr, socklen_t len, int type)
{
    struct hostent *hp;
    static char ipbuf[32];
    hEnt *e;

    sprintf(ipbuf, "%u", *addr);

    e = h_getEnt_(addrTab, ipbuf);
    if (e) {
        hp = e->hData;
        return hp;
    }

    hp = gethostbyaddr(addr, len, type);
    if (hp == NULL) {
        lserrno = LSE_BAD_HOST;
        return NULL;
    }

    addHost2Tab(hp->h_name,
                (in_addr_t **)hp->h_addr_list,
                hp->h_aliases);
    return hp;
}

#define ISBOUNDARY(h1, h2, len)  ( (h1[len]=='.' || h1[len]=='\0') && \
                                (h2[len]=='.' || h2[len]=='\0') )

int
equalHost_(const char *host1, const char *host2)
{
    int len;

    if (strlen(host1) > strlen(host2))
        len = strlen(host2);
    else
        len = strlen(host1);

    if ((strncasecmp(host1, host2, len) == 0)
        && ISBOUNDARY(host1, host2, len))
        return TRUE;

    return FALSE;
}

/* sockAdd2Str_()
 */
char *
sockAdd2Str_(struct sockaddr_in *from)
{
    static char adbuf[24];

    sprintf(adbuf, "\
%s:%d", inet_ntoa(from->sin_addr), (int)ntohs(from->sin_port));
    return adbuf;

}

/* stripDomain()
 */
static inline void
stripDomain(char *name)
{
    char *p;

    if ((p = strchr(name, '.')))
        *p = 0;
}

/* mkHostTab()
 */
static int
mkHostTab(void)
{
    static char fbuf[BUFSIZ];
    char *buf;
    FILE *fp;

    if (nameTab) {
        assert(addrTab);
        return -1;
    }

    nameTab = calloc(1, sizeof(hTab));
    addrTab = calloc(1, sizeof(hTab));

    h_initTab_(nameTab, 101);
    h_initTab_(addrTab, 101);

    if (initenv_(NULL, NULL) < 0)
        return -1;

    sprintf(fbuf, "\
%s/%s", genParams_[LSF_CONFDIR].paramValue, "hosts");

    if ((fp = fopen(fbuf, "r")) == NULL)
        return -1;

    while ((buf = nextline_(fp))) {
        char *addrstr;
        char *name;
        char *p;
        char *alias[MAX_HOSTALIAS];
        in_addr_t *addr[2];
        in_addr_t x;
        int cc;

        memset(alias, 0, sizeof(char *) * MAX_HOSTALIAS);

        addrstr = getNextWord_(&buf);
        if (addrstr == NULL)
            continue;

        x = inet_addr(addrstr);
        addr[0] = &x;
        addr[1] = NULL;

        name = getNextWord_(&buf);
        if (name == NULL)
            continue;

        stripDomain(name);
        strToLower_(name);

        cc = 0;
        while ((p = getNextWord_(&buf))
               && cc < MAX_HOSTALIAS) {
            alias[cc] = strdup(p);
            ++cc;
        }
        /* multihomed hosts are
         * listed multiple times
         * in the host file each time
         * with the same name but different
         * addr.
         *
         * 192.168.7.1 jumbo
         * 192.168.7.4 jumbo
         *     ...
         */
        addHost2Tab(name, addr, alias);

        cc = 0;
        while (alias[cc]) {
            FREEUP(alias[cc]);
            ++cc;
        }

    } /* while() */

    fclose(fp);

    return 0;
}

/* addHost2Tab()
 */
static void
addHost2Tab(const char *name,
            in_addr_t **addrs,
            char **aliases)
{
    struct hostent *hp;
    char ipbuf[32];
    hEnt *e;
    hEnt *e2;
    int new;
    int cc;

    /* add the host to the table by its name
     * if it exists already we must be processing
     * another ipaddr for it.
     */
    e = h_addEnt_(nameTab, name, &new);
    if (new) {
        hp = calloc(1, sizeof(struct hostent));
        hp->h_name = strdup(name);
        hp->h_addrtype = AF_INET;
        hp->h_length = 4;
        e->hData = hp;
    } else {
        hp = (struct hostent*)e->hData;
    }

    cc = 0;
    while (aliases[cc])
        ++cc;
    hp->h_aliases = calloc(cc + 1, sizeof(char *));
    cc = 0;
    while (aliases[cc]) {
        hp->h_aliases[cc] = strdup(aliases[cc]);
        ++cc;
    }

    cc = 0;
    while (addrs[cc])
        ++cc;
    hp->h_addr_list = calloc(cc + 1, sizeof(char *));
    cc = 0;
    while (addrs[cc]) {
        hp->h_addr_list[cc] = calloc(1, sizeof(in_addr_t));
        memcpy(hp->h_addr_list[cc], addrs[cc], sizeof(in_addr_t));
        /* now hash the host by its addr,
         * there can be N addrs but each
         * must be unique...
         */
        sprintf(ipbuf, "%u", *(addrs[cc]));
        e2 = h_addEnt_(addrTab, ipbuf, &new);
        assert(new);
        e2->hData = hp;

        ++cc; /* nexte */
    }
}

