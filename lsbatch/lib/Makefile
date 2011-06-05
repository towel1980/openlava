# $Id: Makefile,v 1.15 2007/08/15 22:18:47 tmizan Exp $
############################################################################
#
# Makefile for Lsbatch Library
#
###########################################################################
TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o .so

STATIC_OBJ = lsb.groups.o lsb.hosts.o lsb.init.o lsb.jobs.o \
       lsb.misc.o lsb.peek.o lsb.qc.o lsb.queues.o \
       lsb.hc.o lsb.reconfig.o lsb.sig.o lsb.sub.o \
       lsb.xdr.o lsb.err.o lsb.move.o lsb.switch.o \
       lsb.users.o lsb.log.o lsb.comm.o \
       lsb.reason.o lsb.mig.o lsb.params.o lsb.spool.o \
       lsb.modify.o lsb.msg.o lsb.conf.o \
       lsb.resource.o lsb.signals.o lsb.debug.o \
       lsb.rexecv.o

SHARED_OBJ = lsb.groups.so lsb.hosts.so lsb.init.so lsb.jobs.so \
       lsb.misc.so lsb.peek.so lsb.qc.so lsb.queues.so \
       lsb.hc.so lsb.reconfig.so lsb.sig.so lsb.sub.so \
       lsb.xdr.so lsb.err.so lsb.move.so lsb.switch.so \
       lsb.users.so lsb.log.so lsb.comm.so \
       lsb.reason.so lsb.mig.so lsb.params.so lsb.spool.so \
       lsb.modify.so lsb.msg.so lsb.conf.so \
       lsb.resource.so lsb.signals.so lsb.debug.so \
       lsb.rexecv.so

STATIC_LIB = liblsfbat.a
SHARED_LIB = liblsfbat.so.1.0.0

all: $(STATIC_LIB) 

.c.o:   $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

.c.so:   $<
	$(CC) -fPIC $(CFLAGS) $(OUTF) -c $<

$(STATIC_LIB): $(STATIC_OBJ)
	$(AR) cru $(STATIC_LIB) $(STATIC_OBJ) 
	$(RANLIB) $@

$(SHARED_LIB): $(SHARED_OBJ)
	$(CC) -shared -Wl,--hash-style=both -Wl,--export-dynamic,-soname,liblsfbat.so.1 -o liblsfbat.so.1.0.0 $(SHARED_OBJ) -lnsl -lc
	ln -sf $(SHARED_LIB) liblsfbat.so
	ln -sf $(SHARED_LIB) liblsfbat.so.1

install:
	mkdir -p $(LAVA_LIBDIR) ; \
	install -m 644 $(STATIC_LIB) $(LAVA_LIBDIR) ; 
clean:
	rm -f $(COMCLEAN) liblsfbat*.so* liblsfbat.a

# These dependencies are maintained by hand
LIB_H = ../daemons/daemonout.h lsb.h ../lsbatch.h ../../lsf/lsf.h ../../config.h
$(OBJS):         $(LIB_H)
lsb.comm.o: ../daemons/daemonout.h lsb.h ../lsbatch.h
lsb.groups.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.hosts.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.users.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.params.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.init.o: ../daemons/daemonout.h lsb.h ../lsbatch.h
lsb.jobs.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.spool.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h ../../lsf/lib/mls.h
lsb.misc.o: ../daemons/daemonout.h lsb.h ../daemons/daemons.h ../lsbatch.h
lsb.peek.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.qc.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.queues.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.hc.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.reconfig.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.sig.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.sub.o: ../daemons/daemonout.h lsb.h lsb.xdr.h  ../lsbatch.h ../../lsf/lib/mls.h
lsb.xdr.o: ../daemons/daemonout.h lsb.h lsb.xdr.h  ../lsbatch.h
lsb.err.o: ../daemons/daemonout.h lsb.h ../lsbatch.h
lsb.move.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.switch.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.modify.o: ../daemons/daemonout.h lsb.h lsb.xdr.h ../lsbatch.h
lsb.log.o: lsb.h ../lsbatch.h
lsb.conf.o: lsb.h ../lsbatch.h
lsb.resource.o: lsb.h ../lsbatch.h ../../lsf/intlib/intlibout.h
lsb.estatus.o: lsb.h
