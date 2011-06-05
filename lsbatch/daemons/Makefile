# $Id: Makefile,v 1.19 2007/08/15 22:18:44 tmizan Exp $
############################################################################
#
# Makefile for Lsbatch daemons
#
###########################################################################
TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a
LSBLIB = $(TOP)/lsbatch/lib/liblsfbat.a

LIBS = $(LSBLIB) $(LSFLIB) $(INTLIB) -lm $(BSDLIB) -ldl
CFLAGS = -I$(TOP) 

MOBJ = mbd.main.o mbd.serv.o mbd.job.o mbd.queue.o \
       mbd.log.o misc.o mbd.comm.o daemons.o \
       daemons.xdr.o mbd.init.o mbd.misc.o mbd.grp.o \
       mbd.host.o mbd.policy.o mbd.dep.o \
       mbd.requeue.o mbd.resource.o \
       mbd.jgrp.o mbd.proxy.o \
       mbd.jarray.o elock.o mail.o \
       mbd.window.o

SOBJ = sbd.main.o sbd.serv.o sbd.job.o sbd.comm.o \
       daemons.o misc.o daemons.xdr.o sbd.misc.o \
       sbd.file.o sbd.sig.o sbd.policy.o sbd.xdr.o \
       elock.o mail.o

LSB_DAEMON_TGT = mbatchd sbatchd

build all:	$(LSB_DAEMON_TGT)

.c.o: $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

$(LSBLIB):
	cd ${@D}; $(MAKE)

mbatchd: $(MOBJ) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(MOBJ) $(LIBS) $(TCLLIB) $(OUTF) 

sbatchd: $(SOBJ) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(SOBJ) $(LIBS) $(TCLLIB) $(OUTF)

install: build
	mkdir -p $(LAVA_SBINDIR) ; \
	install -m 755 $(LSB_DAEMON_TGT) $(LAVA_SBINDIR)

clean:
	rm -f $(COMCLEAN) $(LSB_DAEMON_TGT)

# These dependencies are maintained by hand
mbd.h:                  jgrp.h proxy.h
daemons.xdr.$(OEXT):	daemonout.h ../lsbatch.h ../../lsf/lsf.h daemons.h
daemons.$(OEXT):	daemonout.h ../lsbatch.h ../../lsf/lsf.h daemons.h 
mbd.comm.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
mbd.host.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.grp.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.init.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.job.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.jgrp.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.dep.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.jarray.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.policy.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
mbd.log.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.main.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
mbd.misc.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.queue.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h
mbd.serv.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
mbd.window.$(OEXT):     mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
                ../lsbatch.h ../../lsf/lsf.h
mbd.resource.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
mbd.requeue.$(OEXT):	mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
mbd.proxy.$(OEXT): mbd.h ../../lsf/lib/lib.table.h daemonout.h daemons.h\
		../lsbatch.h ../../lsf/lsf.h 
misc.$(OEXT):	../lsbatch.h ../../lsf/lib/mls.h ../../lsf/lsf.h daemons.h
elock.$(OEXT):	../lsbatch.h ../../lsf/lsf.h daemons.h
mail.$(OEXT):	../lsbatch.h ../../lsf/lsf.h daemons.h
sbd.comm.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lsf.h
sbd.job.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lib/mls.h ../../lsf/lsf.h 
sbd.policy.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lsf.h 
sbd.main.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lsf.h 
sbd.misc.$(OEXT):	sbd.h daemons.h
sbd.serv.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lsf.h
sbd.file.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lib/mls.h ../../lsf/lsf.h
sbd.sig.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lib/mls.h ../../lsf/lsf.h
sbd.xdr.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lsf.h
sbd.misc.$(OEXT):	sbd.h daemons.h daemonout.h ../lsbatch.h\
		../../lsf/lsf.h
etags :
	etags *.[hc] ../*.h ../lib/*.[hc] ../../lsf/*.h \
	../../lsf/lib/*.[hc] ../../lsf/intlib/*.[hc]

