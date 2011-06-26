# $Id: Makefile,v 1.10 2007/08/15 22:18:53 tmizan Exp $
############################################################################
#
# Makefile for LIM
#
###########################################################################

TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a

LIBS = $(INTLIB) $(LSFLIB)
LINKLIBS = $(LSFLIB) $(INTLIB) -lm $(BSDLIB) -ldl

NO_SIGALARM = -DNO_SIGALARM

CFLAGS = -D$(HOSTTYPE) -DHOST_TYPE_STRING=\"$(HOSTTYPE)\" $(NO_SIGALARM)

OBJS = lim.main.o lim.conf.o lim.misc.o lim.load.o \
       lim.rload.o lim.xdr.o lim.internal.o \
       lim.policy.o lim.info.o lim.control.o \
       lim.cluster.o

LIM_TGT = lim

all: $(LIM_TGT)

.c.o:     $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

lim: $(OBJS) $(LIBS) 
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS) $(LINKLIBS) $(TCLLIB) $(OUTF)

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

install: $(LIM_TGT)
	mkdir -p $(OPENLAVA_SBINDIR); \
	install -m 755 $(LIM_TGT) $(OPENLAVA_SBINDIR)

clean: 
	rm -f $(COMCLEAN) $(LIM_TGT)

# These dependencies are maintained by hand
LIM_H = lim.h ../../config.h ../lsf.h limout.h ../intlib/intlib.h ../lib/lib.table.h
lim.conf.$(OEXT):	$(LIM_H) lim.conf.h
lim.control.$(OEXT):	$(LIM_H) ../lib/lib.xdr.h ../lib/lproto.h 
lim.info.$(OEXT):	$(LIM_H) ../lib/lib.xdr.h
lim.rload.$(OEXT):	$(LIM_H) lim.linux.h
lim.main.$(OEXT):	$(LIM_H) ../lib/lproto.h
lim.policy.$(OEXT):	$(LIM_H)
lim.xdr.$(OEXT):	$(LIM_H)
lim.cluster.$(OEXT):	$(LIM_H)

etags :
	etags *.[hc] ../*.h ../lib/*.[hc] ../intlib/*.[hc]

