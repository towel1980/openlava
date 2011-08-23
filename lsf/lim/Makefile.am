#
# Copyright (C) openlava foundation
#
INCLUDES = -I$(top_srcdir)/lsf
AM_CPPFLAGS = -DNO_SIGALARM -D$(HOSTTYPE) -DHOST_TYPE_STRING=\"$(HOSTTYPE)\"

HOSTTYPE=LINUX64

sbin_PROGRAMS = lim
lim_SOURCES  = \
lim.cluster.c lim.control.c lim.internal.c lim.main.c lim.policy.c \
lim.xdr.c lim.conf.c lim.info.c lim.load.c lim.misc.c  lim.rload.c 
lim_LDADD =  $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a
