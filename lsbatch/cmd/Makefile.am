#
# Copyright (C) openlava foundation
#
CC = gcc -g
INCLUDES = -I$(top_srcdir)/lsf  -I$(top_srcdir)/lsf/lib \
           -I$(top_srcdir)/lsbatch  -I$(top_srcdir)/lsbatch/lib -I./
AM_CFLAGS = -Wall

SUFFIXES = .c
.c.o:
	$(CC) $(AM_CFLAGS) -c $<

bin_PROGRAMS = badmin bkill bparams brestart btop bbot bmgroup \
bpeek brun busers bhosts bmig bqueues bsub bjobs bmod \
brequeue bswitch 

badmin_SOURCES = badmin.c cmd.bqc.c cmd.hist.c \
	cmd.bhc.c cmd.misc.c cmd.job.c cmd.prt.c
badmin_LDADD = $(top_srcdir)/lsf/lsadm/startup.o \
	$(top_srcdir)/lsbatch/lib/liblsbatch.a \
	$(top_srcdir)/lsf/lib/liblsf.a \
	$(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bkill_SOURCES = bkill.c cmd.sig.c cmd.jobid.c cmd.err.c
bkill_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bparams_SOURCES = bparams.c
bparams_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

brestart_SOURCES = brestart.c cmd.sub.c cmd.jobid.c \
	cmd.err.c
brestart_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
	$(top_srcdir)/lsf/lib/liblsf.a \
	$(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

btop_SOURCES = btop.c cmd.move.c cmd.jobid.c cmd.misc.c \
	 cmd.prt.c cmd.err.c
btop_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bbot_SOURCES = bbot.c cmd.move.c cmd.jobid.c cmd.misc.c \
	 cmd.prt.c cmd.err.c
bbot_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bmgroup_SOURCES = bmgroup.c cmd.misc.c
bmgroup_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bpeek_SOURCES = bpeek.c cmd.err.c cmd.jobid.c cmd.misc.c cmd.prt.c
bpeek_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

brun_SOURCES = brun.c cmd.jobid.c cmd.err.c
brun_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
	$(top_srcdir)/lsf/lib/liblsf.a \
	$(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

busers_SOURCES = busers.c cmd.misc.c
busers_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bhosts_SOURCES = bhosts.c cmd.prt.c cmd.misc.c
bhosts_LDADD = $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bmig_SOURCES = bmig.c cmd.jobid.c cmd.err.c
bmig_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bqueues_SOURCES = bqueues.c cmd.prt.c cmd.misc.c
bqueues_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bsub_SOURCES = bsub.c cmd.sub.c cmd.jobid.c cmd.err.c
bsub_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bjobs_SOURCES = bjobs.c cmd.prt.c cmd.err.c cmd.job.c \
	cmd.jobid.c cmd.misc.c
bjobs_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bmod_SOURCES = bmod.c cmd.sub.c cmd.jobid.c cmd.err.c
bmod_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

brequeue_SOURCES = brequeue.c cmd.jobid.c cmd.err.c
brequeue_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm

bswitch_SOURCES = bswitch.c cmd.jobid.c cmd.err.c
bswitch_LDADD =  $(top_srcdir)/lsbatch/lib/liblsbatch.a \
        $(top_srcdir)/lsf/lib/liblsf.a \
        $(top_srcdir)/lsf/intlib/liblsfint.a -lnsl -lm
#
