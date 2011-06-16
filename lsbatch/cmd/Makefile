############################################################################
#
# Makefile for Lsbatch Commands
#
###########################################################################
TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a
LSBLIB = $(TOP)/lsbatch/lib/liblsfbat.a

LIBS = $(LSBLIB) $(LSFLIB) $(INTLIB) -ldl $(BSDLIB)

CFLAGS = -I../.. 

OBJS_BSUB       = bsub.o cmd.sub.o cmd.jobid.o \
		  cmd.err.o
OBJS_BRESTART   = brestart.o cmd.sub.o cmd.jobid.o \
		  cmd.err.o
OBJS_BJOBS   = bjobs.o cmd.prt.o cmd.err.o cmd.job.o \
	       cmd.jobid.o cmd.misc.o
OBJS_BKILL   = bkill.o cmd.sig.o cmd.jobid.o cmd.err.o
OBJS_BSWITCH = bswitch.o  cmd.jobid.o cmd.err.o
OBJS_BREQUEUE = brequeue.o cmd.jobid.o \
	        cmd.err.o
OBJS_BTOP    = btop.o cmd.move.o cmd.jobid.o cmd.misc.o \
		cmd.prt.o cmd.err.o
OBJS_BBOT    = bbot.o cmd.move.o cmd.jobid.o cmd.misc.o \
		cmd.prt.o cmd.err.o
OBJS_BQUEUES = bqueues.o cmd.prt.o cmd.misc.o
OBJS_BHOSTS  = bhosts.o  cmd.prt.o cmd.misc.o
OBJS_BUSERS  = busers.o cmd.misc.o
OBJS_BPARAMS  = bparams.o
OBJS_BPEEK   = bpeek.o cmd.err.o cmd.jobid.o \
		cmd.misc.o cmd.prt.o
OBJS_BMGROUP   = bmgroup.o cmd.misc.o 
OBJS_BADMIN  = badmin.o cmd.bqc.o cmd.hist.o \
	       cmd.bhc.o cmd.misc.o cmd.job.o \
               ../../lsf/lsadm/startup.o cmd.prt.o
OBJS_BMIG     = bmig.o cmd.jobid.o cmd.err.o
OBJS_BMOD     = bmod.o cmd.sub.o cmd.jobid.o \
	       cmd.err.o
OBJS_BRUN       = brun.o cmd.jobid.o cmd.err.o

BATCH_BIN = bjobs bsub badmin bmgroup \
		bmod bhosts bparams busers \
		bqueues bkill bpeek brun \
		bswitch	brequeue btop bbot \
		brestart bmig

all:	$(BATCH_BIN)

.c.o:   $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

bsub:	$(OBJS_BSUB) $(LIBS) 
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BSUB) $(LIBS)  $(OUTF)

brestart: $(OBJS_BRESTART) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BRESTART) $(LIBS) $(OUTF)

bjobs: $(OBJS_BJOBS) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BJOBS) $(LIBS) $(OUTF)

bkill:	$(OBJS_BKILL) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BKILL) $(LIBS) $(OUTF)
	rm -f bstop bresume bchkpnt
	ln -s bkill bstop
	ln -s bkill bresume
	ln -s bkill bchkpnt

bswitch: $(OBJS_BSWITCH) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BSWITCH) $(LIBS) $(OUTF)

brequeue: $(OBJS_BREQUEUE) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BREQUEUE) $(LIBS) $(OUTF)

btop: $(OBJS_BTOP) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BTOP) $(LIBS) $(OUTF)

bbot: $(OBJS_BBOT) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BBOT) $(LIBS) $(OUTF)

bqueues: $(OBJS_BQUEUES) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BQUEUES) $(LIBS) $(OUTF)

bhosts: $(OBJS_BHOSTS) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BHOSTS) $(LIBS) $(OUTF)

busers: $(OBJS_BUSERS) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BUSERS) $(LIBS) $(OUTF)

bparams: $(OBJS_BPARAMS) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BPARAMS) $(LIBS) $(OUTF)

bpeek: $(OBJS_BPEEK) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BPEEK) $(LIBS) $(OUTF)

bmgroup: $(OBJS_BMGROUP) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BMGROUP) $(LIBS) $(OUTF)
	rm -f bugroup
	ln -s bmgroup bugroup

bmig: $(OBJS_BMIG) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BMIG) $(LIBS) $(OUTF)

bmod: $(OBJS_BMOD) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BMOD) $(LIBS) $(OUTF)

badmin: $(OBJS_BADMIN) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BADMIN) $(LIBS) $(OUTF)

brun: $(OBJS_BRUN) $(LIBS)
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJS_BRUN) $(LIBS) $(OUTF)

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

$(LSBLIB):
	cd ${@D}; $(MAKE)

install: $(BATCH_BIN)
	mkdir -p $(OPENLAVA_BINDIR) ; \
	install -m 755 $(BATCH_BIN) $(OPENLAVA_BINDIR) ; \
	(cd $(OPENLAVA_BINDIR); ln -sf bkill bstop; \
	ln -sf bkill bresume ; \
	ln -sf bkill bchkpnt ; \
	ln -sf bmgroup bugroup) ; \

clean: 
	rm -f $(COMCLEAN) $(BATCH_BIN)
	rm -f bstop bresume bchkpnt bugroup

# These dependencies are maintained by hand
bmgroup.$(OEXT):	../lsbatch.h cmd.h
bhosts.$(OEXT):	../lsbatch.h cmd.h 
busers.$(OEXT):	../lsbatch.h cmd.h
bparams.$(OEXT):	../lsbatch.h cmd.h
bjobs.$(OEXT):	../lsbatch.h cmd.h
bpeek.$(OEXT):	../lsbatch.h cmd.h
bswitch.$(OEXT):	../lsbatch.h cmd.h
brequeue.$(OEXT): ../lsbatch.h cmd.h    
btop.$(OEXT):		../lsbatch.h cmd.h
bbot.$(OEXT):		../lsbatch.h cmd.h
bqc.$(OEXT):	        ../lsbatch.h cmd.h
bhc.$(OEXT):	        ../lsbatch.h cmd.h
bqueues.$(OEXT):	../lsbatch.h cmd.h
bmod.$(OEXT):	../lsbatch.h cmd.h
badmin.$(OEXT):	../lsbatch.h cmd.h badmin.h
cmd.job.$(OEXT):	../lsbatch.h cmd.h
cmd.sig.$(OEXT):	../lsbatch.h cmd.h
cmd.move.$(OEXT):	../lsbatch.h cmd.h
cmd.sub.$(OEXT):	../lsbatch.h cmd.h ../daemons/daemons.h
cmd.misc.$(OEXT):     ../lsbatch.h cmd.h
cmd.bqc.$(OEXT):     ../lsbatch.h cmd.h
cmd.bhc.$(OEXT):     ../lsbatch.h cmd.h
cmd.hist.$(OEXT):     ../lsbatch.h cmd.h
cmd.breconfig.$(OEXT): ../lsbatch.h cmd.h

