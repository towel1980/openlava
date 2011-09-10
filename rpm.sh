#!/bin/sh
set -x

#
# Copyright (c) 2011 openlava foundation 
#

major="1"
minor="0"

echo "Cleaning up ~/rpmbuild directory..."
rm -rf ~/rpmbuild

echo "Creating the ~/rpmbuild..."
rpmdev-setuptree

echo "Archving source code..."
git archive --format=tar --prefix="openlava-${major}.${minor}/" HEAD \
   | gzip > ~/rpmbuild/SOURCES/openlava-${major}.${minor}.tar.gz
cp spec/openlava.spec ~/rpmbuild/SPECS/openlava.spec

echo "RPM building..."
rpmbuild -ba --target x86_64 ~/rpmbuild/SPECS/openlava.spec
if [ "$?" != 0 ]; then
  echo "Failed buidling rpm"
  exit 1
fi
