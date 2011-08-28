#
# Copyright (C) openlava foundation
#

# Install configuration files for openlava base and batch 
# in the conf directory.
confdir = $(prefix)/conf
conf_DATA = lsf.conf lsf.cluster.openlava lsf.shared lsf.task \
            lsb.hosts lsb.params lsb.queues lsb.users 

# Install the shell profile scrips and the system startup 
# script in the etc directory.
etcdir = $(prefix)/etc
etc_DATA = openlava openlava.sh openlava.csh

# Create the working directory where the working files are
# kept.
install-data-local:
	mkdir -p $(prefix)/work

# Tell automake to install during distcheck the
# configuration and etc files. 
#
EXTRA_DIST = $(conf_DATA) $(etc_DATA)
