# $Id: Makefile,v 1.12 2007/08/15 22:18:55 tmizan Exp $
############################################################################
#
# Makefile for Utility programs
#
############################################################################

TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a
LIBS = $(LSFLIB) $(INTLIB) 

OBJS = lsplace.o lseligible.o lsload.o \
       lsloadadj.o lsid.o lshosts.o \
       lsinfo.o \
       lsmon.o lsacct.o \
       lsrcp.o

CMDS = lsplace lseligible lsload \
       lsloadadj lsid lshosts \
       lsinfo lsmon \
       lsacct lsrcp

all: $(CMDS)

.c.o : $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

lsplace: lsplace.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsplace.o $(LIBS) $(OUTF)

lseligible: lseligible.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lseligible.o $(LIBS) $(OUTF)

lsload:	lsload.o load.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsload.o load.o $(LIBS) $(OUTF)

lsloadadj: lsloadadj.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsloadadj.o $(LIBS) $(OUTF)

lsid:	lsid.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsid.o $(LIBS) $(OUTF)

lslockhost:	lslockhost.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lslockhost.o $(LIBS) $(OUTF)

lsunlockhost:	lsunlockhost.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsunlockhost.o $(LIBS) $(OUTF)

lshosts: lshosts.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lshosts.o $(LIBS) $(OUTF)

lsinfo:	lsinfo.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsinfo.o $(LIBS) $(OUTF)

lsmon: lsmon.o load.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsmon.o load.o $(LIBS) -lncurses $(OUTF)

lsacct: lsacct.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsacct.o $(LIBS) $(OUTF)

lsrcp:	lsrcp.o $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) lsrcp.o $(LIBS) $(BSDLIB) $(OUTF)

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

install: $(CMDS)
	mkdir -p $(LAVA_BINDIR) ; \
	install -m 755 $(CMDS) $(LAVA_BINDIR)

clean:
	rm -f $(COMCLEAN) ${CMDS}


# These dependencies are maintained by hand
lseligible.$(OEXT):	../lsf.h ../../config.h
lshosts.$(OEXT):	../lsf.h
lsid.$(OEXT):	../lib/lproto.h ../lib/lib.table.h ../lsf.h
lsinfo.$(OEXT):	../lsf.h
lsload.$(OEXT):	../../config.h ../lib/lproto.h ../lib/lib.table.h ../lsf.h
lsloadadj.$(OEXT):	../../config.h ../lsf.h
lslockhost.$(OEXT):	../lsf.h
lsplace.$(OEXT):	../../config.h ../lsf.h
lsunlockhost.$(OEXT):	../lsf.h
lsmon.$(OEXT):        ../lsf.h ../../config.h
load.$(OEXT):         ../lsf.h ../../config.h
