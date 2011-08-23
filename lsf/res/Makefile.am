#
# Copyright (C) openlava foundation
#
INCLUDES = -I$(top_srcdir)/lsf

sbin_PROGRAMS = res nios
res_SOURCES  = \
res.c res.handler.c res.misc.c res.rf.c res.getproc.c res.init.c \
res.pty.c res.tasklog.c rescom.h res.h resout.h
res_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

nios_SOURCES = nios.c nios.handler.c nios.h
#
# yep.. true
#
nios_LDADD = $(top_srcdir)/lsbatch/lib/liblsbatch.a \
	$(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a \
	-lnsl -lm
#
