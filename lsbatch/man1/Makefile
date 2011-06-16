#
#
#

TOP = ../..
include $(TOP)/Make.misc

BATCH_MAN1 = bsub.1 bhosts.1 bjobs.1 bkill.1 \
		bmod.1 bparams.1 bpeek.1 bqueues.1 bresume.1 \
		bstop.1 bmgroup.1 busers.1  \
		bchkpnt.1 bmig.1 brestart.1 \
                lsfbatch.1 bbot.1 btop.1 \
                bugroup.1 brequeue.1 
install:
	mkdir -p $(OPENLAVA_MANDIR)/man1 ; \
	install -c -m 644 $(BATCH_MAN1) $(OPENLAVA_MANDIR)/man1
