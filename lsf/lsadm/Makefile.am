#
# Copyright (C) openlava foundation
#
CC = gcc -g
INCLUDES = -I$(top_srcdir)/lsf
AM_CFLAGS = -Wall

SUFFIXES = .c
.c.o:
	$(CC) $(AM_CFLAGS) -c $<

bin_PROGRAMS = lsadm

lsadm_SOURCES = lsadmin.c startup.c cmd.limcontrol.c cmd.rescontrol.c
lsadm_LDADD =  $(top_srcdir)/lsf/lib/liblsf.a \
	$(top_srcdir)/lsf/intlib/liblsfint.a
