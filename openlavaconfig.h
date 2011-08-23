/*
 * Copyright (C) 2011 openlava foundation
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

typedef void (*SIGFUNCTYPE)(int);

#define LIM_PORT        36000
#define RES_PORT        36002

#ifndef MSGSIZE
#define MSGSIZE   8192
#endif

#define NICE_LEAST -40
#define NICE_MIDDLE 20

#ifndef WCOREDUMP
#ifdef LS_WAIT_INT
#define WCOREDUMP(x)    ((x) & 0200)
#else
#define WCOREDUMP(x) (x).w_coredump
#endif
#endif

#define BSD_NICE

#define getpwuiddir getpwuid
#define getpwnamdir getpwnam

typedef struct stat LS_STAT_T;
#define LSTMPDIR        lsTmpDir_
#define LSDEVNULL       "/dev/null"
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
