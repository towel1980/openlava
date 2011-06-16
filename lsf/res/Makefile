############################################################################
#
# Makefile for RES, NIOS
#
############################################################################

TOP = ../..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a
LSBLIB = $(TOP)/lsbatch/lib/liblsfbat.a

LIBS = $(LSBLIB) $(LSFLIB) $(INTLIB) -lnsl -lm 
CFLAGS = -I$(TOP)

RES_OBJS = res.o res.handler.o res.init.o res.misc.o \
       res.pty.o res.rf.o res.tasklog.o res.getproc.o 

NIOS_OBJS = nios.o nios.handler.o

RES_TGT = res nios

all: $(RES_TGT)

.c.o:     $<
	$(CC) $(CFLAGS)  -I$(TOP) $(OUTF) -c $<

res: $(RES_OBJS) $(INTLIB) $(LSBLIB) $(LSFLIB)
	$(CC) $(LDFLAGS) $(CFLAGS) $(RES_OBJS) $(LIBS) $(OUTF)

nios: $(NIOS_OBJS) $(INTLIB) $(LSBLIB) $(LSFLIB)
	$(CC) $(LDFLAGS) $(CFLAGS) $(NIOS_OBJS) $(LIBS) $(OUTF)

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

$(LSBLIB):
	cd ${@D}; $(MAKE)

install: $(RES_TGT)
	mkdir -p $(OPENLAVA_SBINDIR) ; \
	install -m 755 $(RES_TGT) $(OPENLAVA_SBINDIR)

clean:
	rm -f $(COMCLEAN) $(RES_TGT)
#
# These dependencies are maintained by hand (for now)
res.o:	res.h ../lim/limout.h resout.h ../lsf.h ../intlib/intlib.h \
	../../config.h ../lib/lproto.h  ../lib/lib.h
res.handler.o:	res.h resout.h rescom.h ../lsf.h ../intlib/intlib.h \
	../../config.h ../lib/lproto.h  ../lib/lib.h \
	../lib/mls.h
res.init.o:	res.h resout.h ../lsf.h ../intlib/intlib.h ../../config.h \
		../lib/mls.h
res.init.o:	../lib/lproto.h
res.misc.o:	res.h resout.h ../lsf.h
res.pty.o:	res.h resout.h ../lsf.h ../intlib/intlib.h
nios.o:	../lsf.h resout.h nios.h ../../config.h ../lib/lproto.h \
	        ../lib/mls.h rescom.h
res.rf.o:	res.h resout.h rescom.h ../lsf.h ../intlib/intlib.h \
		../../config.h ../lib/lproto.h  ../lib/lib.h \
		../lib/lib.rf.h
