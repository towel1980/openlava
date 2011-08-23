#
# Copyright (C) openlava foundation
#
CC = gcc -g
HOSTTYPE=LINUX64
INCLUDES = -I$(top_srcdir)/lsf
AM_CFLAGS = -Wall -DNO_SIGALARM -D$(HOSTTYPE) -DHOST_TYPE_STRING=\"$(HOSTTYPE)\"

SUFFIXES = .c
.c.o:
	$(CC) $(AM_CFLAGS) -c $<

sbin_PROGRAMS = lim
lim_SOURCES  = \
lim.cluster.c lim.control.c lim.internal.c lim.main.c lim.policy.c \
lim.xdr.c lim.conf.c lim.info.c lim.load.c lim.misc.c  lim.rload.c 
lim_LDADD =  $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a
