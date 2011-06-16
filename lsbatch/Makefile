#
# Da Make
#

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
	mkdir -p $(OPENLAVA_INCLUDEDIR) 
	install -m 644 lsbatch.h $(OPENLAVA_INCLUDEDIR)/lsbatch.h

