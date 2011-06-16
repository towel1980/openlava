#
#
##


TOP = ../
include $(TOP)/Make.misc

OPENLAVA_BASE_CONFIG_FILES = lsf.conf lsf.shared lsf.cluster.openlava \
                         lsf.task 
OPENLAVA_BATCH_CONFIG_FILES = lsb.params lsb.users lsb.queues 
OPENLAVA_STARTUP_SCRIPT = openlava
OPENLAVA_SHELL_INIT_SCRIPTS = openlava.sh openlava.csh
OPENLAVA_SLAVE_SETUP_SCRIPT = openlava.setup

install:
	mkdir -p $(OPENLAVA_CONFDIR) 
	install -c -m 644 $(OPENLAVA_BASE_CONFIG_FILES) $(OPENLAVA_CONFDIR)
	install -c -m 644 ../README $(OPENLAVA_CONFDIR)
	install -c -m 644 ../COPYING $(OPENLAVA_CONFDIR)
#
	mkdir -p $(OPENLAVA_CONFDIR)/lsbatch/$(OPENLAVA_CLUSTERNAME)/configdir
	install -c -m 644 $(OPENLAVA_BATCH_CONFIG_FILES) \
 	$(OPENLAVA_CONFDIR)/lsbatch/$(OPENLAVA_CLUSTERNAME)/configdir
#
	mkdir -p $(OPENLAVA_SBINDIR)
	install -c -m 755 $(OPENLAVA_STARTUP_SCRIPT)  $(OPENLAVA_SBINDIR)
	install -c -m 644 $(OPENLAVA_SHELL_INIT_SCRIPTS)  $(OPENLAVA_SBINDIR)
	install -c -m 755 $(OPENLAVA_SLAVE_SETUP_SCRIPT)  $(OPENLAVA_SBINDIR)

.PHONY : clean
clean:
	
