#
# Copyright (C) openlava foundation
#
CC = gcc -g
INCLUDES = -I$(top_srcdir)/lsf
AM_CFLAGS = -Wall 

SUFFIXES = .c
.c.o:
	$(CC) $(AM_CFLAGS) -c $<

sbin_PROGRAMS = eauth
eauth_SOURCES  = eauth.c
eauth_LDADD =  $(top_srcdir)/lsf/lib/liblsf.a $(top_srcdir)/lsf/intlib/liblsfint.a
