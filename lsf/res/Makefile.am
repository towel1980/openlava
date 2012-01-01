#
# Copyright (C) openlava foundation
#
INCLUDES = -I$(top_srcdir)/lsf

sbin_PROGRAMS = res nios
res_SOURCES  = \
res.c res.handler.c res.misc.c res.rf.c res.getproc.c res.init.c \
res.pty.c res.tasklog.c rescom.h res.h resout.h
res_LDADD = ../lib/liblsf.a ../intlib/liblsfint.a -lm
if !CYGWIN
res_LDADD += -lnsl
endif

nios_SOURCES = nios.c nios.handler.c nios.h
#
# yep.. true
#
nios_LDADD = ../../lsbatch/lib/liblsbatch.a \
	../lib/liblsf.a ../intlib/liblsfint.a -lm
if !CYGWIN
nios_LDADD += -lnsl
endif
#
