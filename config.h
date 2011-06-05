/* $Id: config.h 397 2007-11-26 19:04:00Z mblack $
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

#ifndef _CONFIG_H_
#define _CONFIG_H_

#include "lsf/lsf.h"

#ifdef __linux__
#define SYSV_SIGNALS    1
#define getopt linux_getopt
#endif

typedef void (*SIGFUNCTYPE)(int);


#define LIM_PORT        36000  
#define RES_PORT        36002  


#ifndef FALSE
# define FALSE	(0)
#endif  
#ifndef TRUE
# define TRUE	(1)
#endif 

#ifndef MSGSIZE
# define MSGSIZE		8192
#endif

#ifndef PATH_MAX
#define PATH_MAX _POSIX_PATH_MAX
#endif


extern char *getwd(char *);

#define NICE_LEAST -40
#define NICE_MIDDLE 20


#ifndef WCOREDUMP
#ifdef LS_WAIT_INT
#define WCOREDUMP(x)    ((x) & 0200)
#else 
#define WCOREDUMP(x) (x).w_coredump
#endif 
#endif 

#ifndef FD_SET
typedef long    fd_mask;
# define NFDBITS	(sizeof(fd_mask) * NBBY) 
# define FD_SET(n, p)	((p)->fds_bits[(n)/NFDBITS] |= (1 << ((n) % NFDBITS)))
# define FD_CLR(n, p)	((p)->fds_bits[(n)/NFDBITS] &= ~(1 << ((n) % NFDBITS)))
# define FD_ISSET(n, p)	((p)->fds_bits[(n)/NFDBITS] & (1 << ((n) % NFDBITS)))
# define FD_ISCLR(n, p)	(((p)->fds_bits[(n)/NFDBITS] & (1<<((n)%NFDBITS))) == 0)
# define FD_ZERO(p)     memset((char *)(p), 0, sizeof(*(p)))
#endif

#define BSD_NICE	

#ifdef __linux__
extern int strcasecmp(const char *s1, const char *s2);
extern int strncasecmp(const char *s1, const char *s2, size_t n);
extern struct group *getgrent(void);
extern void setgrent(void);
extern void endgrent(void);
extern int gethostname(char *name, size_t len);
extern int nice( int val );
extern int linux_getopt( int nargc, char *const *nargv, const char *ostr );
#endif       

#define getpwuiddir getpwuid
#define getpwnamdir getpwnam

typedef struct stat LS_STAT_T;
#define LSTMPDIR 	lsTmpDir_
#define LSDEVNULL      	"/dev/null"
#define LSETCDIR        "/etc"
#define closesocket close
#define CLOSESOCKET(s) close((s))
#define SOCK_CALL_FAIL(c) ((c) < 0 )
#define SOCK_INVALID(c) ((c) < 0 )
#define CLOSEHANDLE close
#define SOCK_READ_FIX  b_read_fix
#define SOCK_WRITE_FIX b_write_fix
#define NB_SOCK_READ_FIX   nb_read_fix
#define NB_SOCK_WRITE_FIX  nb_write_fix

#define LSF_NSIG NSIG

#endif    
