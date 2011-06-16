#
# Main Makefile. 
#

# Pick up machine-specific definitions
TOP = .
include Make.misc

TOP_DIR = lsf eauth lsbatch chkpnt config 
TOP_TGT = slsf seauth slsbatch schkpnt 

all build:  $(TOP_TGT)

slsf: 
	@echo "Building on $(ARCH)..."
	cd lsf; $(MAKE)

slsbatch:  
	@echo "Building on $(ARCH)..."
	cd lsbatch; $(MAKE)

seauth:
	@echo "Building on $(ARCH)..."
	cd eauth; $(MAKE)

schkpnt:
	@echo "Building on $(ARCH)..."
	cd chkpnt; $(MAKE)

install: 
	@echo "Building on $(ARCH)..."
	set -x; for i in $(TOP_DIR); do \
	( if [ -d $$i ]; then cd $$i; $(MAKE) install; fi ); done
	mkdir -p $(OPENLAVA_LOGDIR)
	mkdir -p $(OPENLAVA_WORKDIR)/$(OPENLAVA_CLUSTERNAME)/logdir

clean:
	set -x; for i in $(TOP_DIR); do\
	( if [ -d $$i ]; then cd $$i; $(MAKE) clean; fi ); done
	rm -f $(COMCLEAN)

cleanall: clean
	rm -rf $(BRELEASE) 
arch:
	@echo "architecture: $(ARCH) uname: `uname -a`"
