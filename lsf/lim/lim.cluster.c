/* $Id: lim.cluster.c 397 2007-11-26 19:04:00Z mblack $
 * Copyright (C) 2007 Platform Computing Inc
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
#include "lim.h"
#include <math.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include "../../lsf/lib/lsi18n.h"

#define NL_SETN         24

#define ABORT     1
#define RX_HINFO  2
#define RX_LINFO  3

#define HINFO_TIMEOUT   120
#define LINFO_TIMEOUT   60

struct clientNode  *clientMap[MAXCLIENTS];

extern int chanIndex;

static void processMsg(int);
static void clientReq(XDR *, struct LSFHeader *, int );

static void shutDownChan(int);

void
clientIO(struct Masks *chanmasks)
{
    int  i;

    for (i = 0; (i < chanIndex) && (i < MAXCLIENTS); i++) {

        if (i == limSock || i == limTcpSock)
            continue;

        if (FD_ISSET(i, &chanmasks->emask)) {

            if (clientMap[i])
                ls_syslog(LOG_ERR, "\
%s: Lost connection with client %s IO or decode error",
                          __func__,
                          sockAdd2Str_(&clientMap[i]->from));
            shutDownChan(i);
            continue;
        }

        if (FD_ISSET(i, &chanmasks->rmask)) {
            processMsg(i);
        }
    }
}


static void
processMsg(int chanfd)
{
    struct Buffer *buf;
    struct LSFHeader hdr;
    XDR xdrs;
    struct sockaddr_in from;

    if (clientMap[chanfd] && clientMap[chanfd]->inprogress)
        return;

    if (chanDequeue_(chanfd, &buf) < 0) {
        ls_syslog(LOG_ERR, "\
%s: failed to dequeue from channel %d %M", __func__, chanfd);
        shutDownChan(chanfd);
        return;
    }

    ls_syslog(LOG_DEBUG,"\
%s: Received message with len %d on chan %d",
              __func__, buf->len, chanfd);

    xdrmem_create(&xdrs,
                  buf->data,
                  XDR_DECODE_SIZE_(buf->len),
                  XDR_DECODE);

    if (!xdr_LSFHeader(&xdrs, &hdr)) {
        ls_syslog(LOG_ERR, "\
%s: Bad header received chanfd %d", __func__, chanfd);
        xdr_destroy(&xdrs);
        shutDownChan(chanfd);
        chanFreeBuf_(buf);
        return;
    }

    if ((clientMap[chanfd] && hdr.opCode >= FIRST_LIM_PRIV)
        || (!clientMap[chanfd] && hdr.opCode < FIRST_INTER_CLUS)) {
        ls_syslog(LOG_ERR, "\
%s: Invalid opCode %d from client", __func__, hdr.opCode);
        xdr_destroy(&xdrs);
        shutDownChan(chanfd);
        chanFreeBuf_(buf);
        return;
    }

    if (hdr.opCode >= FIRST_INTER_CLUS && !masterMe) {
        ls_syslog(LOG_ERR, "\
%s: Intercluster request received, but I'm not master", __func__);
        xdr_destroy(&xdrs);
        shutDownChan(chanfd);
        chanFreeBuf_(buf);
        return;
    }

    if (!clientMap[chanfd]) {

        if (hdr.opCode != LIM_CLUST_INFO) {
            socklen_t L = sizeof(struct sockaddr_in);

            if (getpeername(chanSock_(chanfd),
                            (struct sockaddr *)&from,
                            &L) < 0) {
                ls_syslog(LOG_ERR, "\
%s: getpeername() on socket %d failed %M",
                          __func__, chanSock_(chanfd));
            }

            ls_syslog(LOG_ERR, "\
%s: Protocol error received opCode %d from %s",
                      __func__, hdr.opCode, sockAdd2Str_(&from));
            xdr_destroy(&xdrs);
            shutDownChan(chanfd);
            chanFreeBuf_(buf);
            return;
        }
    }

    ls_syslog(LOG_DEBUG, "\
%s: Received request %d from %s",
              __func__, hdr.opCode, sockAdd2Str_(&from));

    switch(hdr.opCode) {

        case LIM_LOAD_REQ:
        case LIM_GET_HOSTINFO:
        case LIM_PLACEMENT:
        case LIM_GET_RESOUINFO:
        case LIM_GET_INFO:

            clientMap[chanfd]->limReqCode = hdr.opCode;
            clientMap[chanfd]->reqbuf = buf;
            clientReq(&xdrs, &hdr, chanfd);
            break;
        case LIM_LOAD_ADJ:
            loadadjReq(&xdrs, &clientMap[chanfd]->from, &hdr, chanfd);
            xdr_destroy(&xdrs);
            shutDownChan(chanfd);
            chanFreeBuf_(buf);
            break;
        case LIM_PING:

            xdr_destroy(&xdrs);
            shutDownChan(chanfd);
            chanFreeBuf_(buf);
            break;
        default:
            ls_syslog(LOG_ERR, "\
%s: Invalid opCode %d from %s", __func__, hdr.opCode,
                      sockAdd2Str_(&from));
            xdr_destroy(&xdrs);
            chanFreeBuf_(buf);
            break;
    }
}


static void
clientReq(XDR *xdrs, struct LSFHeader *hdr, int chfd)
{
    static char fname[]="clientReq";
    struct decisionReq decisionRequest;
    int oldpos, i;

    clientMap[chfd]->clientMasks = 0;

    oldpos = XDR_GETPOS(xdrs);


    if (! xdr_decisionReq(xdrs, &decisionRequest, hdr)) {
        goto Reply1;
    }

    clientMap[chfd]->clientMasks = 0;
    for (i=1; i < decisionRequest.numPrefs; i++) {
        if (!findHostInCluster(decisionRequest.preferredHosts[i])) {
            clientMap[chfd]->clientMasks = 0;
            break;
        }
    }

    for(i=0; i < decisionRequest.numPrefs; i++)
        free(decisionRequest.preferredHosts[i]);
    free(decisionRequest.preferredHosts);

Reply1:

    {
        int pid = 0;

#if defined(NO_FORK)

        pid =0;
        io_block_(chanSock_(chfd));
#else
        pid = fork();
#endif
        if (pid == 0) {
            int sock;


#if !defined(NO_FORK)
            chanClose_( limSock );
            limSock = chanClientSocket_( AF_INET, SOCK_DGRAM, 0 );
#endif


            XDR_SETPOS(xdrs, oldpos);
            sock = chanSock_(chfd);
            if (io_block_(sock) < 0)
                ls_syslog(LOG_ERR, I18N_FUNC_FAIL, fname, "io_block_");

            switch(hdr->opCode) {
            case LIM_GET_HOSTINFO:
                hostInfoReq(xdrs, clientMap[chfd]->fromHost, &clientMap[chfd]->from, hdr, chfd);
                break;
            case LIM_GET_RESOUINFO:
                resourceInfoReq(xdrs, &clientMap[chfd]->from, hdr, chfd);
                break;


            case LIM_LOAD_REQ:
                loadReq(xdrs, &clientMap[chfd]->from, hdr, chfd);
                break;
            case LIM_PLACEMENT:
                placeReq(xdrs, &clientMap[chfd]->from, hdr, chfd);
                break;
            case LIM_GET_INFO:
                infoReq(xdrs, &clientMap[chfd]->from, hdr, chfd);

            default:
                break;
            }
#if !defined(NO_FORK)
            exit(0);
#else
            xdr_destroy(xdrs);
            shutDownChan(chfd);
            return;
#endif
        } else {
            if (pid < 0)
                ls_syslog(LOG_ERR, I18N_FUNC_FAIL, fname, "fork");
            xdr_destroy(xdrs);
            shutDownChan(chfd);
            return;
        }
    }
}

static void
shutDownChan(int chanfd)
{
    chanClose_(chanfd);
    if (clientMap[chanfd]) {
        chanFreeBuf_(clientMap[chanfd]->reqbuf);
        FREEUP(clientMap[chanfd]);
    }
}

