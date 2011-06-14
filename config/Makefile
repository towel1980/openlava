#$Id: Makefile,v 1.1 2007/08/10 15:05:49 tmizan Exp $

TOP = ../
include $(TOP)/Make.misc

LAVA_BASE_CONFIG_FILES = lsf.conf lsf.shared lsf.cluster.openlava \
                         lsf.task 
LAVA_BATCH_CONFIG_FILES = lsb.params lsb.users lsb.queues 
LAVA_STARTUP_SCRIPT = lava
LAVA_SHELL_INIT_SCRIPTS = lava.sh lava.csh
LAVA_SLAVE_SETUP_SCRIPT = openlava.setup

install:
	mkdir -p $(LAVA_CONFDIR) 
	install -c -m 644 $(LAVA_BASE_CONFIG_FILES) $(LAVA_CONFDIR)
#
	mkdir -p $(LAVA_CONFDIR)/lsbatch/$(LAVA_CLUSTERNAME)/configdir
	install -c -m 644 $(LAVA_BATCH_CONFIG_FILES) \
 	$(LAVA_CONFDIR)/lsbatch/$(LAVA_CLUSTERNAME)/configdir
#
	mkdir -p $(LAVA_SBINDIR)
	install -c -m 755 $(LAVA_STARTUP_SCRIPT)  $(LAVA_SBINDIR)
	install -c -m 644 $(LAVA_SHELL_INIT_SCRIPTS)  $(LAVA_SBINDIR)
	install -c -m 755 $(LAVA_SLAVE_SETUP_SCRIPT)  $(LAVA_SBINDIR)
#
# At last create the soft link in the root installation 
# openlava -> openlava-major.minor
#
	#ln -sf $(LAVA_TOP) $(LAVA_ROOT)/openlava
clean:
#	
