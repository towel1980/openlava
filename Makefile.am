#
# Copyright (C) openlava foundation 
#
SUBDIRS = lsf config lsbatch lsf/res eauth

.PHONY: $(SUBDIRS)

# Always and only use C
CC = gcc -g 

MISSING_FILES = aclocal.m4

DISTCLEANFILES = config.guess config.sub depcomp install-sh ltmain.sh missing

MAINTAINERCLEANFILES = Makefile.in config.h.in configure $(MISSING_FILES) 
