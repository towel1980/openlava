# $Id: Makefile,v 1.13 2007/08/15 22:18:49 tmizan Exp $
############################################################################
#
# Makefile for LIB
#
############################################################################

TOP = ../..
include ${TOP}/Make.misc

.SUFFIXES: .o

OBJS = daemon.o window.o userok.o \
       timers.o wait.o resreq.o misc.o \
       cmdtime.o \
       admin.o list.o \
       lsftcl.o resourcecmd.o callex.o \
       listset.o bitset.o \
       jidx.o vector.o

LIB = lsfint.a

all:	$(LIB)

$(LIB):	$(OBJS)
	$(AR) cru $(LIB) $(OBJS)
	$(RANLIB) $@

.c.o : $<
	$(CC) $(CFLAGS) $(OUTF) -c $< 

callex.o: callex.c
	$(CC)  $(CFLAGS)  -DYYCHAR_ARRAY -c callex.c

clean: 
	rm -f $(COMCLEAN) $(LIB)

install:
	@echo""	

# These dependencies are maintained by hand
LIB_H = ../lib/lib.h ../lsf.h ../lim/limout.h
$(OBJS):	$(LIB_H)
daemon.o:	intlib.h ../../config.h
window.o:	intlib.h ../../config.h
timers.o:	intlib.h ../../config.h intlibout.h
wait.o:		intlib.h ../../config.h intlibout.h
resreq.o:	$(LIB_H) intlib.h resreq.h ../../config.h
cmdtime.o:	intlib.h ../../config.h ../lib/lproto.h
admin.o:	intlib.h ../../config.h
list.o:	        intlib.h ../../config.h intlibout.h
lsftcl.o:	        intlib.h ${TCL_INCLUDE}/tcl.h ../../config.h intlibout.h lsftcl.h
resourcecmd.o:	intlib.h ../../config.h intlibout.h 
listset.o:    intlib.h ../../config.h intlibout.h
bitset.o:    intlib.h ../../config.h intlibout.h bitset.h
testbitset.o: bitset.h bitset.c ../lsf.h intlib.h 
userok.o:    ../lib/mls.h

etags :
	etags *.[hc] ../*.h ../lib/*.[hc] ../intlib/*.[hc]

