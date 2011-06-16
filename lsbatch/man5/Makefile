#
#
#

TOP = ../..
include $(TOP)/Make.misc

BATCH_MAN5 = lsb.acct.5 lsb.events.5 lsb.hosts.5 lsb.params.5 lsb.queues.5 \
	     lsb.users.5

install:
	mkdir -p $(OPENLAVA_MANDIR)/man5 ; \
	install -c -m 644 $(BATCH_MAN5) $(OPENLAVA_MANDIR)/man5
