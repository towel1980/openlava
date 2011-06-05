# $Header: /cvs/CVS/lava_test/lsf/pim/Makefile,v 1.7 2007/08/15 22:18:55 tmizan Exp $
############################################################################
#
# Makefile for PIM
#
###########################################################################

TOP = ../..
include $(TOP)/Make.misc

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a

CFLAGS = $(SITE)

LIBS =  $(LSFLIB) $(INTLIB) 
LINKLIBS =  $(BSDLIB) -lm -ldl 
OBJS =  pim.main.o pim.os.o

PIM_TGT = pim

all: $(PIM_TGT)

pim: $(OBJS) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS) $(LIBS) $(LINKLIBS) $(OUTF)

$(INTLIB):
	cd ${@D}; ${MAKE}

$(LSFLIB):
	cd ${@D}; ${MAKE}

install: $(PIM_TGT)
	mkdir -p $(LAVA_SBINDIR) ; \
	install -m 755 $(PIM_TGT) $(LAVA_SBINDIR)

clean: 
	rm -f $(COMCLEAN) $(PIM_TGT)


# These dependencies are maintained by hand
PIM = ../../config.h ../lib/lib.pim.h ../lib/lproto.h
PLATFORMS = pim.linux.h
pim.main.o:	$(PIM)
pim.os.o:	$(PIM) $(PLATFORMS)
