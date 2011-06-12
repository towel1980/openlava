#
# Directory specific make file.
#
TOP = ../
include $(TOP)/Make.misc

LAVA_BASE_CONFIG_FILES = lsf.conf lsf.shared lsf.cluster.openlava \
                         lsf.task 
LAVA_BATCH_CONFIG_FILES = lsb.params lsb.users lsb.queues 
LAVA_STARTUP_SCRIPT = openlava
LAVA_SHELL_INIT_SCRIPTS = openlava.sh openlava.csh

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
#
# At last create the soft link in the root installation 
# openlava -> openlava-major.minor
#
	#ln -sf $(LAVA_TOP) $(LAVA_ROOT)/openlava
clean:
	
