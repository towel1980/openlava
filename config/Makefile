#$Id: Makefile,v 1.1 2007/08/10 15:05:49 tmizan Exp $

TOP = ../
include $(TOP)/Make.misc

LAVA_BASE_CONFIG_FILES = lsf.conf lsf.shared lsf.cluster.ciao \
                         lsf.task lava.sh lava.csh
LAVA_BATCH_CONFIG_FILES = lsb.params lsb.users lsb.queues 

install:
	mkdir -p $(LAVA_CONFDIR) 
	install -c -m 644 $(LAVA_BASE_CONFIG_FILES) $(LAVA_CONFDIR)
#
	mkdir -p $(LAVA_CONFDIR)/lsbatch/$(LAVA_CLUSTERNAME)/configdir
	install -c -m 644 $(LAVA_BATCH_CONFIG_FILES) \
 	$(LAVA_CONFDIR)/lsbatch/$(LAVA_CLUSTERNAME)/configdir

clean:
	
