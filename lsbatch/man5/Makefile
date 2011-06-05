#$Id: Makefile,v 1.2 2007/08/10 17:19:19 tmizan Exp $

TOP = ../..
include $(TOP)/Make.misc

BATCH_MAN5 = lsb.acct.5 lsb.events.5 lsb.hosts.5 lsb.params.5 lsb.queues.5 \
	     lsb.users.5

install:
	mkdir -p $(LAVA_MANDIR)/man5 ; \
	install -c -m 644 $(BATCH_MAN5) $(LAVA_MANDIR)/man5
