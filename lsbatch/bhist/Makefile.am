#
# Copyright (C) openlava foundation
#
CC = gcc -g
INCLUDES = -I$(top_srcdir)/lsf  -I$(top_srcdir)/lsf/lib \
           -I$(top_srcdir)/lsbatch  -I$(top_srcdir)/lsbatch/lib -I./
AM_CFLAGS = -Wall

SUFFIXES = .c
.c.o:
	$(CC) $(AM_CFLAGS) -c $<

bin_PROGRAMS = bhist
bhist_SOURCES  = bhist.c read.event.c
bhist_LDADD = ../cmd/cmd.job.o \
	../cmd/cmd.misc.o ../cmd/cmd.jobid.o ../cmd/cmd.prt.o \
	../cmd/cmd.err.o ../cmd/cmd.hist.o \
	$(top_srcdir)/lsbatch/lib/liblsbatch.a \
	$(top_srcdir)/lsf/lib/liblsf.a \
	$(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm
