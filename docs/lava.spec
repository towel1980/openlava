# Copyright (C) 2007 Platform Computing Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
# 	
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
#
# 
# $Id$
# 

%define clustername lava
%define subversion 3

Summary: Platform(R) Lava(tm) Batch Scheduling and management
Name: lava
Version: 1.0
Release: 6
License: GPLv2
Group: Applications/Productivity
Vendor: Platform Computing Inc.
ExclusiveArch: %{ix86} x86_64
URL: http://www.osgdc.org/
Source: %{name}-%{version}.%{subversion}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: gcc, tcl-devel, ncurses-devel
Requires: ncurses, tcl
Requires(pre): /usr/sbin/useradd
Requires(post): chkconfig
Requires(preun): chkconfig

%description
Platform(R) Lava(tm) Batch scheduling

%package master-config
Summary: Platform Lava master - configuration files
Group: Applications/Productivity
Vendor: Platform Computing Inc.
Requires: %{name} = %{version}

%description master-config
Platform(R) Lava(tm) master configuration files

%package devel
Summary: Development files for Lava
Group: Development/Libraries
Vendor: Platform Computing Inc.
Requires: %{name} = %{version}
%description devel
Platform(R) Lava(tm) development files

%package static
Summary: Static libraries for Lava development
Group: Development/Libraries
Requires: %{name}-devel = %{version}

%description static
The lava-static package includes static libraries needed
to develop programs that use the lava batch scheduler.

##
## PREP
##
%prep
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT

%setup -q -n %{name}

# Make a bunch of directories
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_var}/log/lava
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir
mkdir -p ${RPM_BUILD_ROOT}%{_var}/spool/lava/work
mkdir -p ${RPM_BUILD_ROOT}%{_var}/spool/lava/work/%{clustername}/lsf_cmddir
mkdir -p ${RPM_BUILD_ROOT}%{_var}/spool/lava/work/%{clustername}/lsf_indir
mkdir -p ${RPM_BUILD_ROOT}%{_var}/spool/lava/work/%{clustername}/logdir
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/lava
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/profile.d
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/lava/misc

##
## BUILD
##
%build
make

##
## CLEAN
##
%clean
/bin/rm -rf $RPM_BUILD_ROOT

##
## INSTALL
##
%install

# Install configs
install -m644 config/lava.sh ${RPM_BUILD_ROOT}%{_sysconfdir}/profile.d
install -m644 config/lava.csh ${RPM_BUILD_ROOT}%{_sysconfdir}/profile.d
install -m644 config/lsf.shared ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf
install -m644 config/lsf.task ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf

# Batch configuration
install -m644 config/lsb.modules ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir
install -m644 config/lsb.params ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir
install -m644 config/lsb.queues ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir
install -m644 config/lsb.users ${RPM_BUILD_ROOT}%{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir

# MPI Wrappers
install -m755 scripts/mpich-mpirun ${RPM_BUILD_ROOT}%{_bindir}
install -m755 scripts/openmpi-mpirun ${RPM_BUILD_ROOT}%{_bindir}
install -m755 scripts/lam-mpirun ${RPM_BUILD_ROOT}%{_bindir}
install -m755 scripts/lava.init ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d/lava
install -m755 scripts/mpich2-mpiexec ${RPM_BUILD_ROOT}%{_bindir}

# Install binaries, daemons
make install INSTALL_PREFIX=$RPM_BUILD_ROOT

# Make the symlinks for the DSOs
cd ${RPM_BUILD_ROOT}/%{_libdir}
ln -s liblsf.so.1.0.0 liblsf.so.1
ln -s liblsfbat.so.1.0.0 liblsfbat.so.1

cd ${RPM_BUILD_ROOT}/usr/bin
ln -s mpich-mpirun mvapich1-mpirun
ln -s mpich2-mpiexec mvapich2-mpiexec

##
## PRE
##
## %pre
# Add "lavaadmin" user
/usr/sbin/useradd -c "Lava Administrator" -s /sbin/nologin -m -d /home/lavaadmin lavaadmin 2> /dev/null || :

##
## POST
##
%post
/sbin/ldconfig
# Register lava daemons
/sbin/chkconfig --add lava
/sbin/chkconfig lava on

##
## PREUN
##
%preun
if [ $1 = 0 ]; then
   /sbin/service lava stop > /dev/null 2>&1
   /sbin/chkconfig lava off
   /sbin/chkconfig --del lava
   /sbin/ldconfig
fi

##
## POSTUN
##
%postun
/sbin/ldconfig

##
## FILES
##
%files
%defattr(-,root,root)
%{_datadir}/lava/misc
%{_sysconfdir}/init.d/lava
#%{_sysconfdir}/profile.d/lava.sh
#%{_sysconfdir}/profile.d/lava.csh
%config(noreplace) %{_sysconfdir}/profile.d/lava.csh
%config(noreplace) %{_sysconfdir}/profile.d/lava.sh
%{_libdir}/liblsf.so.?*
%{_libdir}/liblsfbat.so.?*
%{_sbindir}/eauth
%{_sbindir}/echkpnt
%{_sbindir}/erestart
%{_sbindir}/mbatchd
%{_sbindir}/sbatchd
%{_sbindir}/lim
%{_sbindir}/res
%{_sbindir}/pim
%{_sbindir}/nios
%{_sbindir}/badmin
%{_sbindir}/lsadmin
%{_bindir}/bbot
%{_bindir}/bhist
%{_bindir}/bhosts
%{_bindir}/bjobs
%{_bindir}/bkill
%{_bindir}/bstop
%{_bindir}/bresume
%{_bindir}/bchkpnt
%{_bindir}/bmgroup
%{_bindir}/bugroup
%{_bindir}/bmig
%{_bindir}/bmod
%{_bindir}/bparams
%{_bindir}/bpeek
%{_bindir}/bqueues
%{_bindir}/brequeue
%{_bindir}/brestart
%{_bindir}/brun
%{_bindir}/bsub
%{_bindir}/bswitch
%{_bindir}/btop
%{_bindir}/busers
%{_bindir}/lam-mpirun
%{_bindir}/mpich-mpirun
%{_bindir}/mpich2-mpiexec
%{_bindir}/openmpi-mpirun
%{_bindir}/mvapich2-mpiexec
%{_bindir}/mvapich1-mpirun
%{_bindir}/lsacct
%{_bindir}/lseligible
%{_bindir}/lshosts
%{_bindir}/lsid
%{_bindir}/lsinfo
%{_bindir}/lsload
%{_bindir}/lsloadadj
%{_bindir}/lsmon
%{_bindir}/lsplace
%{_bindir}/lsrcp

# Man pages
%{_mandir}/man1/bbot.1.gz
%{_mandir}/man1/bchkpnt.1.gz
%{_mandir}/man1/bhosts.1.gz
%{_mandir}/man1/bjobs.1.gz
%{_mandir}/man1/bkill.1.gz
%{_mandir}/man1/bmgroup.1.gz
%{_mandir}/man1/bmig.1.gz
%{_mandir}/man1/bmod.1.gz
%{_mandir}/man1/bparams.1.gz
%{_mandir}/man1/bpeek.1.gz
%{_mandir}/man1/bqueues.1.gz
%{_mandir}/man1/brequeue.1.gz
%{_mandir}/man1/brestart.1.gz
%{_mandir}/man1/bresume.1.gz
%{_mandir}/man1/bstop.1.gz
%{_mandir}/man1/bsub.1.gz
%{_mandir}/man1/btop.1.gz
%{_mandir}/man1/bugroup.1.gz
%{_mandir}/man1/busers.1.gz
%{_mandir}/man1/bswitch.1.gz
%{_mandir}/man1/lsacct.1.gz
%{_mandir}/man1/lseligible.1.gz
%{_mandir}/man1/lsfbase.1.gz
%{_mandir}/man1/lsfbatch.1.gz
%{_mandir}/man1/lsfintro.1.gz
%{_mandir}/man1/lshosts.1.gz
%{_mandir}/man1/lsid.1.gz
%{_mandir}/man1/lsinfo.1.gz
%{_mandir}/man1/lsload.1.gz
%{_mandir}/man1/lsloadadj.1.gz
%{_mandir}/man1/lsmon.1.gz
%{_mandir}/man1/lsplace.1.gz
%{_mandir}/man1/lsrcp.1.gz
%{_mandir}/man1/lstools.1.gz
%{_mandir}/man5/lsb.acct.5.gz
%{_mandir}/man5/lsb.events.5.gz
%{_mandir}/man5/lsb.hosts.5.gz
%{_mandir}/man5/lsb.params.5.gz
%{_mandir}/man5/lsb.queues.5.gz
%{_mandir}/man5/lsb.users.5.gz
%{_mandir}/man8/badmin.8.gz
%{_mandir}/man8/brun.8.gz
%{_mandir}/man8/eauth.8.gz
%{_mandir}/man8/lim.8.gz
%{_mandir}/man8/lsadmin.8.gz
%{_mandir}/man8/lsfinstall.8.gz
%{_mandir}/man8/mbatchd.8.gz
%{_mandir}/man8/nios.8.gz
%{_mandir}/man8/pim.8.gz
%{_mandir}/man8/res.8.gz
%{_mandir}/man8/sbatchd.8.gz
%{_mandir}/man5/install.config.5.gz
%{_mandir}/man5/lim.acct.5.gz
%{_mandir}/man5/lsf.acct.5.gz
%{_mandir}/man5/lsf.cluster.5.gz
%{_mandir}/man5/lsf.conf.5.gz
%{_mandir}/man5/lsf.shared.5.gz
%{_mandir}/man5/res.acct.5.gz

#%config(noreplace) %{_sysconfdir}/lava/conf/lsf.shared
#%config(noreplace) %{_sysconfdir}/lava/conf/lsf.task
#%attr(0644,lavaadmin,lavaadmin) %{_sysconfdir}/lava/conf/lsf.shared
#%attr(0644,lavaadmin,lavaadmin) %{_sysconfdir}/lava/conf/lsf.task

%doc COPYING

%files master-config
%defattr(0644,lavaadmin,lavaadmin)
%config(noreplace) %{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir/lsb.params
%config(noreplace) %{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir/lsb.queues
%config(noreplace) %{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir/lsb.users
%config(noreplace) %{_sysconfdir}/lava/conf/lsbatch/%{clustername}/configdir/lsb.modules
%config(noreplace) %{_sysconfdir}/lava/conf/lsf.shared
%config(noreplace) %{_sysconfdir}/lava/conf/lsf.task
%attr(-,lavaadmin,lavaadmin) %{_var}/spool/lava/*
%attr(-,lavaadmin,lavaadmin) %dir %{_var}/log/lava

%files static
%{_libdir}/liblsf.a
%{_libdir}/liblsfbat.a

%files devel 
%{_includedir}/lsf/lsbatch.h
%{_includedir}/lsf/lsf.h
%{_libdir}/liblsf.so
%{_libdir}/liblsfbat.so
%{_mandir}/man8/esub.8.gz
%{_mandir}/man8/eexec.8.gz

%changelog
* Fri May 30 2008 Shawn Starr <sstarr@platform.com> 1.0-6
- Fix symlinks for MVAPICH1/2.
* Tue May 27 2008 Gerry Wen <gwen@platform.com> 1.0-2
- Add wrapper script for MPICH2 mpiexec
* Mon Feb 13 2008 Shawn Starr <sstarr@platform.com> 1.0-1
- Make home directory for lavaadmin user.
* Mon Jan 23 2008 Shawn Starr <sstarr@platform.com> 1.0-0
- Initial release of Lava 1.0
