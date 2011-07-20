#
# Copyright (C) 2011 openlava foundation
#
# Install parallel integration 
# scripts
#

TOP = ../
include $(TOP)/Make.misc

OPENLAVA_INTEGRATION_SCRIPTS = lam-mpirun mpich2-mpiexec mpich-mpirun \
    openmpi-mpirun

install:
	mkdir -p $(OPENLAVA_BINDIR)
	install -c -m 755 $(OPENLAVA_INTEGRATION_SCRIPTS)  $(OPENLAVA_BINDIR)

.PHONY : clean
clean:
	
