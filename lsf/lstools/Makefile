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
	$(CC)  $(CFLAGS) lsplace.o $(LIBS) $(OUTF)

lseligible: lseligible.o $(LIBS)
	$(CC)  $(CFLAGS) lseligible.o $(LIBS) $(OUTF)

lsload:	lsload.o load.o $(LIBS)
	$(CC)  $(CFLAGS) lsload.o load.o $(LIBS) $(OUTF)

lsloadadj: lsloadadj.o $(LIBS)
	$(CC)  $(CFLAGS) lsloadadj.o $(LIBS) $(OUTF)

lsid:	lsid.o $(LIBS)
	$(CC)  $(CFLAGS) lsid.o $(LIBS) $(OUTF)

lslockhost:	lslockhost.o $(LIBS)
	$(CC)  $(CFLAGS) lslockhost.o $(LIBS) $(OUTF)

lsunlockhost:	lsunlockhost.o $(LIBS)
	$(CC)  $(CFLAGS) lsunlockhost.o $(LIBS) $(OUTF)

lshosts: lshosts.o $(LIBS)
	$(CC)  $(CFLAGS) lshosts.o $(LIBS) $(OUTF)

lsinfo:	lsinfo.o $(LIBS)
	$(CC)  $(CFLAGS) lsinfo.o $(LIBS) $(OUTF)

lsmon: lsmon.o load.o $(LIBS)
	$(CC)  $(CFLAGS) lsmon.o load.o $(LIBS) -lncurses $(OUTF)

lsacct: lsacct.o $(LIBS)
	$(CC)  $(CFLAGS) lsacct.o $(LIBS) $(OUTF)

lsrcp:	lsrcp.o $(LIBS)
	$(CC)  $(CFLAGS) lsrcp.o $(LIBS) $(BSDLIB) $(OUTF)

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

install: $(CMDS)
	mkdir -p $(OPENLAVA_BINDIR) ; \
	install -m 755 $(CMDS) $(OPENLAVA_BINDIR)

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
