#
# Copyright (C) openlava foundation
#
CC = gcc -g
INCLUDES = -I$(top_srcdir)/lsf
AM_CFLAGS = -Wall

SUFFIXES = .c
.c.o:
	$(CC) $(AM_CFLAGS) -c $<

sbin_PROGRAMS = pim
pim_SOURCES  = pim.main.c  pim.os.c
pim_LDADD = $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a
