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

%define subversion 6
%define _lavatop /opt/lava
%define _clustername lava
%define _lavaversion 1.0
%define _libdir %{_lavatop}/%{_lavaversion}/linux2.6-glibc2.3-x86_64/lib
%define _bindir %{_lavatop}/%{_lavaversion}/linux2.6-glibc2.3-x86_64/bin
%define _sbindir %{_lavatop}/%{_lavaversion}/linux2.6-glibc2.3-x86_64/etc
%define _mandir %{_lavatop}/%{_lavaversion}/man
%define _logdir %{_lavatop}/log
%define _includedir %{_lavatop}/%{_lavaversion}/include/lsf

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
Prefix: %{_lavatop}
%description
Platform(R) Lava(tm) Batch scheduling

%package master-config
Summary: Platform Lava master - configuration files
Group: Applications/Productivity
Vendor: Platform Computing Inc.
Requires: %{name} = %{version}
Prefix: %{_lavatop}
%description master-config
Platform(R) Lava(tm) master configuration files

%package devel
Summary: Development files for Lava
Group: Development/Libraries
Vendor: Platform Computing Inc.
Requires: %{name} = %{version}
Prefix: %{_lavatop}
%description devel
Platform(R) Lava(tm) development files

%package static
Summary: Static libraries for Lava development
Group: Development/Libraries
Requires: %{name}-devel = %{version}
Prefix: %{_lavatop}
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
mkdir -p ${RPM_BUILD_ROOT}%{_logdir}
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/conf
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/conf/lsbatch/%{_clustername}/configdir
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/work
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/work/%{_clustername}/lsf_cmddir
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/work/%{_clustername}/lsf_indir
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/work/%{_clustername}/logdir
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/init.d
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/profile.d
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}%{_lavatop}/%{_lavaversion}/misc

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
install -m644 config/lava.sh ${RPM_BUILD_ROOT}%{_lavatop}/conf
install -m644 config/lava.csh ${RPM_BUILD_ROOT}%{_lavatop}/conf
install -m644 config/lsf.shared ${RPM_BUILD_ROOT}%{_lavatop}/conf
install -m644 config/lsf.cluster.clustername ${RPM_BUILD_ROOT}%{_lavatop}/conf
install -m644 config/lsf.conf ${RPM_BUILD_ROOT}%{_lavatop}/conf
install -m644 config/lsf.task ${RPM_BUILD_ROOT}%{_lavatop}/conf

# Batch configuration
install -m644 config/lsb.modules ${RPM_BUILD_ROOT}%{_lavatop}/conf/lsbatch/%{_clustername}/configdir
install -m644 config/lsb.params ${RPM_BUILD_ROOT}%{_lavatop}/conf/lsbatch/%{_clustername}/configdir
install -m644 config/lsb.queues ${RPM_BUILD_ROOT}%{_lavatop}/conf/lsbatch/%{_clustername}/configdir
install -m644 config/lsb.users ${RPM_BUILD_ROOT}%{_lavatop}/conf/lsbatch/%{_clustername}/configdir

# MPI Wrappers
install -m755 scripts/mpich-mpirun ${RPM_BUILD_ROOT}%{_bindir}
install -m755 scripts/openmpi-mpirun ${RPM_BUILD_ROOT}%{_bindir}
install -m755 scripts/lam-mpirun ${RPM_BUILD_ROOT}%{_bindir}
install -m755 scripts/lava.init ${RPM_BUILD_ROOT}%{_lavatop}/conf/lava
install -m755 scripts/mpich2-mpiexec ${RPM_BUILD_ROOT}%{_bindir}

# Install binaries, daemons
make install INSTALL_PREFIX=$RPM_BUILD_ROOT

# Make the symlinks for the DSOs
cd ${RPM_BUILD_ROOT}%{_libdir}
ln -s liblsf.so.1.0.0 liblsf.so.1
ln -s liblsfbat.so.1.0.0 liblsfbat.so.1

cd ${RPM_BUILD_ROOT}%{_bindir}
ln -s mpich-mpirun mvapich1-mpirun
ln -s mpich2-mpiexec mvapich2-mpiexec

##
## PRE
##
## %pre
# Add "lavaadmin" user
#/usr/sbin/useradd -c "Lava Administrator" -s /sbin/nologin -m -d /home/lavaadmin lavaadmin 2> /dev/null || :

##
## POST
##
%post

##
## copy scripts into the relevant directories
##
mv ${RPM_INSTALL_PREFIX}/conf/lava.sh %{_sysconfdir}/profile.d
mv ${RPM_INSTALL_PREFIX}/conf/lava.csh %{_sysconfdir}/profile.d
mv ${RPM_INSTALL_PREFIX}/conf/lava %{_sysconfdir}/init.d

/sbin/ldconfig
# Register lava daemons
/sbin/chkconfig --add lava
/sbin/chkconfig lava on

%post master-config

##
## customize the lsf.cluster.clustername file
##
_lavatop=${RPM_INSTALL_PREFIX}
hostname=`hostname`
sed -i -e "s/XXX_lsfmc_XXX/$hostname/" ${_lavatop}/conf/lsf.cluster.clustername
mv ${_lavatop}/conf/lsf.cluster.clustername ${_lavatop}/conf/lsf.cluster.%{_clustername}

##
## customize the lava.sh file
##
_bindir=${_lavatop}/%{_lavaversion}/linux2.6-glibc2.3-x86_64/bin
_libdir=${_lavatop}/%{_lavaversion}/linux2.6-glibc2.3-x86_64/lib
_mandir=${_lavatop}/%{_lavaversion}/man
sed -i -e "s#__BINDIR__#${_bindir}#" %{_sysconfdir}/profile.d/lava.sh
sed -i -e "s#__LAVATOP__#${_lavatop}#" %{_sysconfdir}/profile.d/lava.sh
sed -i -e "s#__LIBDIR__#${_libdir}#" %{_sysconfdir}/profile.d/lava.sh
sed -i -e "s#__MANDIR__#${_mandir}#" %{_sysconfdir}/profile.d/lava.sh
sed -i -e "s#__LAVAVERSION__#%{_lavaversion}#" %{_sysconfdir}/profile.d/lava.sh

##
## customize the /etc/init.d/lava file
##
sed -i -e "s#__LAVATOP__#${_lavatop}#" %{_sysconfdir}/init.d/lava

##
## customize the lsf.conf file
##
_sbindir=${_lavatop}/%{_lavaversion}/linux2.6-glibc2.3-x86_64/etc
_logdir=${_lavatop}/log
sed -i  -e "s#__SBINDIR__#${_sbindir}#" \
	-e "s#__LAVAVERSION__#%{_lavaversion}#" \
	-e "s#__LAVATOP__#${_lavatop}#" \
	-e "s#__BINDIR__#${_bindir}#" \
	-e "s#__LIBDIR__#${_libdir}#" \
	-e "s#__LOGDIR__#${_logdir}#" \
	${_lavatop}/conf/lsf.conf

##
## customize the lsf.shared file
##
sed -i -e "s/__CLUSTERNAME__/%{_clustername}/" ${_lavatop}/conf/lsf.shared

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
%{_lavatop}/%{_lavaversion}/misc
%{_lavatop}/conf/lava
%{_lavatop}/conf/lava.sh
%{_lavatop}/conf/lava.csh
#%config(noreplace) %{_sysconfdir}/profile.d/lava.csh
#%config(noreplace) %{_sysconfdir}/profile.d/lava.sh
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
%{_mandir}/man1/bbot.1
%{_mandir}/man1/bchkpnt.1
%{_mandir}/man1/bhosts.1
%{_mandir}/man1/bjobs.1
%{_mandir}/man1/bkill.1
%{_mandir}/man1/bmgroup.1
%{_mandir}/man1/bmig.1
%{_mandir}/man1/bmod.1
%{_mandir}/man1/bparams.1
%{_mandir}/man1/bpeek.1
%{_mandir}/man1/bqueues.1
%{_mandir}/man1/brequeue.1
%{_mandir}/man1/brestart.1
%{_mandir}/man1/bresume.1
%{_mandir}/man1/bstop.1
%{_mandir}/man1/bsub.1
%{_mandir}/man1/btop.1
%{_mandir}/man1/bugroup.1
%{_mandir}/man1/busers.1
#%{_mandir}/man1/bswitch.1
%{_mandir}/man1/lsacct.1
%{_mandir}/man1/lseligible.1
%{_mandir}/man1/lsfbase.1
%{_mandir}/man1/lsfbatch.1
%{_mandir}/man1/lsfintro.1
%{_mandir}/man1/lshosts.1
%{_mandir}/man1/lsid.1
%{_mandir}/man1/lsinfo.1
%{_mandir}/man1/lsload.1
%{_mandir}/man1/lsloadadj.1
%{_mandir}/man1/lsmon.1
%{_mandir}/man1/lsplace.1
%{_mandir}/man1/lsrcp.1
%{_mandir}/man1/lstools.1
%{_mandir}/man5/lsb.acct.5
%{_mandir}/man5/lsb.events.5
%{_mandir}/man5/lsb.hosts.5
%{_mandir}/man5/lsb.params.5
%{_mandir}/man5/lsb.queues.5
%{_mandir}/man5/lsb.users.5
%{_mandir}/man8/badmin.8
%{_mandir}/man8/brun.8
%{_mandir}/man8/eauth.8
%{_mandir}/man8/lim.8
%{_mandir}/man8/lsadmin.8
%{_mandir}/man8/lsfinstall.8
%{_mandir}/man8/mbatchd.8
%{_mandir}/man8/nios.8
%{_mandir}/man8/pim.8
%{_mandir}/man8/res.8
%{_mandir}/man8/sbatchd.8
%{_mandir}/man5/install.config.5
%{_mandir}/man5/lim.acct.5
%{_mandir}/man5/lsf.acct.5
%{_mandir}/man5/lsf.cluster.5
%{_mandir}/man5/lsf.conf.5
%{_mandir}/man5/lsf.shared.5
%{_mandir}/man5/res.acct.5

#%config(noreplace) %{_lavatop}/lava/conf/lsf.shared
#%config(noreplace) %{_lavatop}/lava/conf/lsf.task
#%attr(0644,lavaadmin,lavaadmin) %{_lavatop}/lava/conf/lsf.shared
#%attr(0644,lavaadmin,lavaadmin) %{_lavatop}/lava/conf/lsf.task

%doc COPYING

%files master-config
%defattr(0644,lavaadmin,lavaadmin)
%config(noreplace) %{_lavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.params
%config(noreplace) %{_lavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.queues
%config(noreplace) %{_lavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.users
%config(noreplace) %{_lavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.modules
%config(noreplace) %{_lavatop}/conf/lsf.shared
%config(noreplace) %{_lavatop}/conf/lsf.conf
%config(noreplace) %{_lavatop}/conf/lsf.cluster.clustername
%config(noreplace) %{_lavatop}/conf/lsf.task
%attr(-,lavaadmin,lavaadmin) %{_lavatop}/work/*
%attr(-,lavaadmin,lavaadmin) %dir %{_logdir}

%files static
%{_libdir}/liblsf.a
%{_libdir}/liblsfbat.a

%files devel 
%{_includedir}/lsbatch.h
%{_includedir}/lsf.h
%{_libdir}/liblsf.so
%{_libdir}/liblsfbat.so
#%{_mandir}/man8/esub.8.gz
#%{_mandir}/man8/eexec.8.gz

%changelog
* Fri Apr 22 2011 Robert Stober <rmstober@gmail.com> 1.0-6.6
- Changed to install in /opt/lava
- Added support for autoconfig of various lava config files
- Removed creation of lavaadmin user
* Fri May 30 2008 Shawn Starr <sstarr@platform.com> 1.0-6
- Fix symlinks for MVAPICH1/2.
* Tue May 27 2008 Gerry Wen <gwen@platform.com> 1.0-2
- Add wrapper script for MPICH2 mpiexec
* Mon Feb 13 2008 Shawn Starr <sstarr@platform.com> 1.0-1
- Make home directory for lavaadmin user.
* Mon Jan 23 2008 Shawn Starr <sstarr@platform.com> 1.0-0
- Initial release of Lava 1.0
