#$Id: Makefile,v 1.1 2007/08/10 15:05:49 tmizan Exp $

TOP = ../../..
include $(TOP)/Make.misc

BASE_MAN1 = lseligible.1  lsfintro.1  lsid.1 lsload.1  lsmon.1  lsrcp.1 \
            lsacct.1  lsfbase.1 lshosts.1  lsinfo.1  lsloadadj.1 lsplace.1 \
            lstools.1

install:
	mkdir -p $(LAVA_MANDIR)/man1 ; \
	install -c -m 644 $(BASE_MAN1) $(LAVA_MANDIR)/man1
