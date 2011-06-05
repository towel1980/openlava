# $Id: Makefile,v 1.6 2007/08/03 23:39:33 jchan Exp $
############################################################################
#
# Makefile for the binaries related to external authentication
#
#
###########################################################################
TOP = ..
include $(TOP)/Make.misc

.SUFFIXES: .o

INTLIB = $(TOP)/lsf/intlib/lsfint.a
LSFLIB = $(TOP)/lsf/lib/liblsf.a

LIBS = $(LSFLIB) $(INTLIB)

EXEC_ALL = eauth.o

all:	eauth

eauth: $(EXEC_ALL) $(INTLIB) $(LSFLIB)
	$(CC) $(LDFLAGS) $(CFLAGS) $(EXEC_ALL) $(LIBS) $(OUTF)

.c.o:     $<
	$(CC) $(CFLAGS) $(OUTF) -c $<

$(INTLIB):
	cd ${@D}; $(MAKE)

$(LSFLIB):
	cd ${@D}; $(MAKE)

install: eauth
	mkdir -p $(LAVA_SBINDIR) ; \
	install -m 755 eauth $(LAVA_SBINDIR)

clean: 
	rm -f $(COMCLEAN) $(EXEC_ALL) eauth
