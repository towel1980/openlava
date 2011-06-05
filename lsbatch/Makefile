#$Id: Makefile,v 1.4 2007/08/10 14:57:46 tmizan Exp $

TOP = ..
include $(TOP)/Make.misc

LSB_SUBDIR = lib daemons cmd bhist 
LSB_TGT = slib sdaemons scmd sbhist 

build all: ${LSB_TGT}

slib: 
	cd lib; $(MAKE)

sdaemons: 
	cd daemons; $(MAKE)

scmd: 
	cd cmd; $(MAKE)

sbhist: 
	cd bhist; $(MAKE)

clean:
	rm -f $(COMCLEAN)
	@for d in $(LSB_SUBDIR); do (if [ -d $$d ]; then \
	    echo "cd $$d; $(MAKE) $@"; cd $$d; $(MAKE) $@; fi); done

install: 
	@for d in $(LSB_SUBDIR) man1 man5 man8; do\
	    (echo "cd $$d; $(MAKE) $@" ; cd $$d; $(MAKE) $@); done
	mkdir -p $(LAVA_INCLUDEDIR) 
	install -m 644 lsbatch.h $(LAVA_INCLUDEDIR)/lsbatch.h

