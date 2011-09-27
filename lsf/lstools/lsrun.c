/*
 * Copyright (C) 2011 David Bigagli
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of version 2 of the GNU General Public License as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
 *
 */

/* Note. lsrun is missing from the openlava distribution. We have
 * developed our own version which merges lsrun and lsgrun functionalites
 * in one command. The API documentation is available on the internet
 * and examples are provided in the LSF Programming Guide, the one
 * we have is for version 3.2 Fourth Edition, august 1998.
 * It works great.
 */

#include <stdlib.h>
#include <string.h>
#include "../lsf.h"
#include "../lib/lproto.h"

struct lsrunParams {
    char **hlist;
    char **cmd;
    char *resReq;
    char *hosts;
    int verbose;
    int parallel;
    int pty;
};

static struct lsrunParams *P;

static void
usage(void)
{
    fprintf(stderr, "\
lsrun: [-h] [-V] [-P] [-v] [-p] [-R] [-m hosts...]\n");
}
static int gethostsbyname(const char *, char **);
static char **gethostsbylist(int *);
static char **gethostsbyresreq(int *);

int
main(int argc, char **argv, char **environ)
{
    int cc;
    int num;
    int tid;
    char **hlist;

    /* tell getopt() to stop processing
     * options after the first non option
     * is found.
     */
    putenv("POSIXLY_CORRECT=yes");

    P = calloc(1, sizeof(struct lsrunParams));

    while ((cc = getopt(argc, argv, "hVPvpR:m:")) != EOF) {

        switch (cc) {
            char *err;
            case 'V':
                fprintf(stderr, "%s\n", _OPENLAVA_PROJECT_);
                return 0;
            case 'p':
                P->parallel = 1;
                break;
            case 'v':
                P->verbose = 1;
                break;
            case 'R':
                P->resReq = optarg;
                break;
            case 'P':
                P->pty = 1;
                break;
            case 'm':
                P->hosts = optarg;
                if (gethostsbyname(P->hosts, &err) < 0) {
                    fprintf(stderr, "\
lsrun: cannot resolve %s hostname", err);
                    free(err);
                    return -1;
                }
                break;
            case 'h':
            case '?':
                usage();
                return -1;
        }
    }

    P->cmd = &argv[optind];
    if (P->cmd[0] == NULL) {
        usage();
        free(P);
        return -1;
    }

    /* Ignore SIGUSR1 and use ls_rwait()
     * to poll for done tasks.
     */
    signal(SIGUSR1, SIG_IGN);

    if (P->hosts)
        hlist = gethostsbylist(&num);
    else
        hlist = gethostsbyresreq(&num);

    if (hlist == NULL) {
        free(P);
        return -1;
    }

    /* initialize the remote execution
     * library
     */
    cc = ls_initrex(1, 0);
    if (cc < 0) {
        ls_perror("ls_initrex()");
        return -1;
    }

    for (cc = 0; cc < num; cc++) {

        if (P->verbose) {
            printf("Running task on host %s\n", hlist[cc]);
        }

        tid = ls_rtaske(hlist[cc],
                        P->cmd,
                        P->pty ? REXF_USEPTY : 0,
                        environ);
        if (tid < 0) {
            fprintf(stderr, "\
lsrun: ls_rtaske() failed on host %s: %s\n",
                    hlist[cc], ls_sysmsg());
        }

        if (P->verbose)
            printf("Task %d on host %s started\n", tid, hlist[cc]);

        /* the host was manually selected
         * so let's tell li to jackup the
         * load so this host won't be
         * selected again
         */
        if (P->hosts) {
            struct placeInfo place;

            strcpy(place.hostName, hlist[cc]);
            place.numtask = 1;

            ls_loadadj(P->resReq, &place, 1);
        }
    }

    while (num > 0) {
        LS_WAIT_T stat;
        struct rusage ru;

        tid = ls_rwait(&stat, 0, &ru);
        if (tid < 0) {
            ls_perror("ls_rwait()");
            break;
        }

        if (P->verbose)
            printf("Task %d done\n", tid);

        --num;
    }

    /* the openlava library keeps memory to
     * this array inside, but since we are not
     * calling it again this should be safe.
     */
    free(P);

    return 0;
}

/* gethostbylist()
 * If user specified the list of host where to
 * run we ignore resource requirement an pty.
 */
static char **
gethostsbylist(int *num)
{
    int cc;
    char *p;
    char *p0;
    char *word;
    char **hlist;

    p0 = p = strdup(P->hosts);

    cc = 0;
    while ((word = getNextWord_(&p)))
        ++cc;
    free(p0);
    *num = cc;

    if (cc == 0) {
        fprintf(stderr, "\
%s: Not enough host(s) currently eligible\n", __FUNCTION__);
        return NULL;
    }

    hlist = calloc(cc, sizeof(char *));
    cc = 0;
    p0 = p = strdup(P->hosts);
    while ((word = getNextWord_(&p))) {
        hlist[cc] = strdup(word);
        ++cc;
    }
    free(p0);

    return hlist;

}

/* gethostbyresreq()
 */
static char **
gethostsbyresreq(int *num)
{
    char **hlist;

    /* ask lim for only one host if not
     * parallel request, in this case lim
     * will schedule different host all
     * the time avoid to overload on
     * host.
     */
    *num = 0;
    if (P->parallel == 0)
        *num = 1;

    hlist = ls_placereq(P->resReq, num, 0, NULL);
    if (hlist == NULL) {
        ls_perror("ls_placereq()");
        return NULL;
    }

    return hlist;
}

/* gethostsbyname()
 * Valide a list of given hosts, each host must be resolvable
 * with gethostbyname().
 */
static int
gethostsbyname(const char *list, char **err)
{
    return 0;
}
