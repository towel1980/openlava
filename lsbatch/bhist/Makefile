###########################################################################
# $Id: Makefile,v 1.5 2007/08/15 22:18:43 tmizan Exp $
#
# Makefile for Lsbatch - BHIST Command
#
###########################################################################
TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a
LSBLIB = $(TOP)/lsbatch/lib/liblsfbat.a

LIBS = $(LSBLIB) $(LSFLIB) $(INTLIB) $(BSDLIB) 

CFLAGS = -I$(TOP)

OBJS_BHIST = bhist.o read.event.o ../cmd/cmd.job.o \
     ../cmd/cmd.misc.o ../cmd/cmd.jobid.o ../cmd/cmd.prt.o \
     ../cmd/cmd.err.o ../cmd/cmd.hist.o

TGT = bhist

build all: $(TGT)

.c.o:     $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

bhist: $(OBJS_BHIST) $(INTLIB) $(LSFLIB) $(LSBLIB)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BHIST) $(LIBS) $(OUTF)

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

$(LSBLIB):
	cd ${@D}; $(MAKE)

install: build
	mkdir -p $(LAVA_BINDIR) ; \
	install -m 755 $(TGT) $(LAVA_BINDIR)

clean: 
	rm -f $(COMCLEAN) $(TGT) 

# These dependencies must be maintained by hand (for now)
bhist.o read.event.o:	bhist.h ../lsbatch.h ../../lsf/lsf.h 

