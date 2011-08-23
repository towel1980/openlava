#
# Copyright (C) openlava foundation
#
INCLUDES = -I$(top_srcdir)/lsf

bin_PROGRAMS = lsadm

lsadm_SOURCES = lsadmin.c startup.c cmd.limcontrol.c cmd.rescontrol.c
lsadm_LDADD =  $(top_srcdir)/lsf/lib/liblsf.a \
	$(top_srcdir)/lsf/intlib/liblsfint.a
