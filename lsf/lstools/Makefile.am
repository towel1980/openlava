#
# Copyright (C) openlava foundation
#
INCLUDES = -I$(top_srcdir)/lsf

bin_PROGRAMS = lsacct lseligible lshosts lsid lsinfo lsloadadj lsload lsmon lsplace lsrcp

lsacct_SOURCES = lsacct.c  
lsacct_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lseligible_SOURCES = lseligible.c  
lseligible_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lshosts_SOURCES = lshosts.c  
lshosts_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lsid_SOURCES = lsid.c  
lsid_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lsinfo_SOURCES = lsinfo.c  
lsinfo_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lsloadadj_SOURCES = lsloadadj.c  
lsloadadj_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lsload_SOURCES = lsload.c  
lsload_LDADD = load.o $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lsmon_SOURCES = lsmon.c  
lsmon_LDADD = load.o $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a -lncurses

lsplace_SOURCES = lsplace.c  
lsplace_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a

lsrcp_SOURCES = lsrcp.c
lsrcp_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl

