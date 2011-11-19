#
# Copyright (C) openlava project
#

# Install configuration files for openlava base and batch 
# in the conf directory.

# noinst_SCRIPTS = lsf.conf
# CLEANFILES = $(noinst_SCRIPTS)
# 
# do_subst = sed -e 's,[@]prefix[@],$(prefix),g'

# lsf.conf :
# 	$(do_subst) < lsf.conf.template > lsf.conf

# Install the shell profile scrips and the system startup 
# script in the etc directory.
etcdir = $(prefix)/etc
etc_DATA = openlava openlava.sh openlava.csh \
	lsf.conf lsf.cluster.openlava lsf.shared lsf.task \
	lsb.hosts lsb.params lsb.queues lsb.users 

# Create the working directory where the working files are
# kept.
install-data-local:
	mkdir -p $(prefix)/work/logdir
	mkdir -p $(prefix)/log

# Tell automake to install during distcheck the
# configuration and etc files. 
#
EXTRA_DIST = $(etc_DATA)
