#
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

%define major 1
%define minor 0
%define release 1

%define version %{major}.%{minor}
%define _openlavatop /opt/openlava-%{version}
%define _clustername openlava
%define _libdir %{_openlavatop}/lib
%define _bindir %{_openlavatop}/bin
%define _sbindir %{_openlavatop}/sbin
%define _mandir %{_openlavatop}/share/man
%define _logdir %{_openlavatop}/log
%define _includedir %{_openlavatop}/include
%define _etcdir %{_openlavatop}/etc

Summary: openlava Distributed Batch Scheduler
Name: openlava
Version: 1.0
Release: 1
License: GPLv2
Group: Applications/Productivity
Vendor: openlava foundation
ExclusiveArch: x86_64
URL: http://www.openlava.net/
Source: %{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gcc, tcl-devel, ncurses-devel
Requires: ncurses, tcl
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Prefix: /opt

%description
openlava Distributed Batch Scheduler

#
# PREP
#
%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

#
# BUILD
#
%build
./bootstrap.sh
make

#
# CLEAN
#
%clean
/bin/rm -rf $RPM_BUILD_ROOT

#
# INSTALL
#
%install

# Install binaries, daemons
make install INSTALL_PREFIX=$RPM_BUILD_ROOT

# install directories and files
install -d $RPM_BUILD_ROOT%{_openlavatop}/bin
install -d $RPM_BUILD_ROOT%{_openlavatop}/etc
install -d $RPM_BUILD_ROOT%{_openlavatop}/include
install -d $RPM_BUILD_ROOT%{_openlavatop}/lib
install -d $RPM_BUILD_ROOT%{_openlavatop}/log
install -d $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -d $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -d $RPM_BUILD_ROOT%{_openlavatop}/share/man/man3
install -d $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -d $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -d $RPM_BUILD_ROOT%{_openlavatop}/work/logdir

# in openlava root
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/COPYING  $RPM_BUILD_ROOT%{_openlavatop}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/README  $RPM_BUILD_ROOT%{_openlavatop}

# bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/badmin  $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bbot    $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/bhist/bhist   $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bhosts  $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bjobs   $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bkill   $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bmgroup $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bmig    $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bmod    $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bparams $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bpeek   $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bqueues $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/brequeue $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/brestart $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/brun     $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bsub     $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bswitch  $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/btop     $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/busers   $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/lam-mpirun $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsacct     $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lsadm/lsadmin    $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lseligible $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lshosts    $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsid       $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsinfo     $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsload     $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsloadadj  $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsmon      $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsplace    $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsrcp      $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/mpich2-mpiexec $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/mpich-mpirun   $RPM_BUILD_ROOT%{_openlavatop}/bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/openmpi-mpirun $RPM_BUILD_ROOT%{_openlavatop}/bin

# etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.cluster.openlava $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.conf $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.task $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.shared $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.params $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.queues $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.hosts $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.users $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.setup $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.sh $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.csh $RPM_BUILD_ROOT%{_openlavatop}/etc

# include
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lsf.h $RPM_BUILD_ROOT%{_openlavatop}/include
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/lsbatch.h $RPM_BUILD_ROOT%{_openlavatop}/include

# lib
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lib/liblsf.a  $RPM_BUILD_ROOT%{_openlavatop}/lib
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/lib/liblsbatch.a  $RPM_BUILD_ROOT%{_openlavatop}/lib

# sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/eauth/eauth  $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lim/lim  $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/daemons/mbatchd  $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/res/nios  $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/pim/pim  $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/res/res $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/daemons/sbatchd $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/chkpnt/echkpnt          $RPM_BUILD_ROOT%{_openlavatop}/sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/chkpnt/erestart         $RPM_BUILD_ROOT%{_openlavatop}/sbin

# share
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bbot.1    $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bchkpnt.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bhosts.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bjobs.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bkill.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bmgroup.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bmig.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bmod.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bparams.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bpeek.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bqueues.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/brequeue.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/brestart.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bresume.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bstop.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bsub.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/btop.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bugroup.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/busers.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bswitch.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsacct.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lseligible.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsfbase.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/lsfbatch.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsfintro.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lshosts.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsid.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsinfo.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsload.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsloadadj.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsmon.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsplace.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsrcp.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lstools.1 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.acct.5  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.events.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.hosts.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.params.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.queues.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.users.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lim.acct.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.acct.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.cluster.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.conf.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.shared.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/res.acct.5 $RPM_BUILD_ROOT%{_openlavatop}/share/man/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/badmin.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/brun.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/eauth.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/eexec.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/esub.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/lim.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/lsadmin.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/lsfinstall.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/mbatchd.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/nios.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/pim.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/res.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/sbatchd.8  $RPM_BUILD_ROOT%{_openlavatop}/share/man/man8

#
# PRE
#
%pre

#
# Add "openlava" user
#
/usr/sbin/groupadd -f openlava
/usr/sbin/useradd -c "openlava Administrator" -g openlava -m -d /home/openlava openlava 2> /dev/null || :
#
# POST
#
%post

#
# set variables
#
_openlavatop=${RPM_INSTALL_PREFIX}/openlava-1.0
# create the symbolic links
ln -sf ${_openlavatop}/bin/bkill  ${_openlavatop}/bin/bstop
ln -sf ${_openlavatop}/bin/bkill  ${_openlavatop}/bin/bresume
ln -sf ${_openlavatop}/bin/bkill  ${_openlavatop}/bin/bchkpnt
ln -sf ${_openlavatop}/bin/bmgroup  ${_openlavatop}/bin/bugroup
chown -h openlava:openlava ${_openlavatop}/bin/bstop
chown -h openlava:openlava ${_openlavatop}/bin/bresume
chown -h openlava:openlava ${_openlavatop}/bin/bchkpnt
chown -h openlava:openlava ${_openlavatop}/bin/bugroup
#
cp ${_openlavatop}/etc/openlava.sh %{_sysconfdir}/profile.d
cp ${_openlavatop}/etc/openlava.csh %{_sysconfdir}/profile.d
cp ${_openlavatop}/etc/openlava %{_sysconfdir}/init.d

# Register lava daemons
/sbin/chkconfig --add openlava
/sbin/chkconfig openlava on

%preun
/sbin/service openlava stop > /dev/null 2>&1
/sbin/chkconfig openlava off
/sbin/chkconfig --del openlava


%postun
_openlavatop=${RPM_INSTALL_PREFIX}/openlava-1.0
rm -f /etc/init.d/openlava
rm -f /etc/profile.d/openlava.*
rm -rf ${_openlavatop}

#
# FILES
#
%files
%defattr(-,openlava,openlava)
%attr(0755,openlava,openlava) %{_openlavatop}/etc/openlava
%{_openlavatop}/etc/openlava.sh
%{_openlavatop}/etc/openlava.csh
%{_openlavatop}/etc/openlava.setup
%{_sbindir}/eauth
%{_sbindir}/echkpnt
%{_sbindir}/erestart
%{_sbindir}/mbatchd
%{_sbindir}/sbatchd
%{_sbindir}/lim
%{_sbindir}/res
%{_sbindir}/pim
%{_sbindir}/nios
%{_bindir}/badmin
%{_bindir}/lsadmin
%{_bindir}/bbot
%{_bindir}/bhist
%{_bindir}/bhosts
%{_bindir}/bjobs
%{_bindir}/bkill
%{_bindir}/bmgroup
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
%{_mandir}/man1/bswitch.1
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
%{_mandir}/man8/eexec.8
%{_mandir}/man8/esub.8
%{_mandir}/man8/lim.8
%{_mandir}/man8/lsadmin.8
%{_mandir}/man8/lsfinstall.8
%{_mandir}/man8/mbatchd.8
%{_mandir}/man8/nios.8
%{_mandir}/man8/pim.8
%{_mandir}/man8/res.8
%{_mandir}/man8/sbatchd.8
%{_mandir}/man5/lim.acct.5
%{_mandir}/man5/lsf.acct.5
%{_mandir}/man5/lsf.cluster.5
%{_mandir}/man5/lsf.conf.5
%{_mandir}/man5/lsf.shared.5
%{_mandir}/man5/res.acct.5

# libraries
%{_libdir}/liblsf.a
%{_libdir}/liblsbatch.a

# headers
%{_includedir}/lsbatch.h
%{_includedir}/lsf.h

# docs
%doc COPYING

%defattr(0644,openlava,openlava)
%config(noreplace) %{_openlavatop}/etc/lsb.params
%config(noreplace) %{_openlavatop}/etc/lsb.queues
%config(noreplace) %{_openlavatop}/etc/lsb.hosts
%config(noreplace) %{_openlavatop}/etc/lsb.users
%config(noreplace) %{_openlavatop}/etc/lsf.shared
%config(noreplace) %{_openlavatop}/etc/lsf.conf
%config(noreplace) %{_openlavatop}/etc/lsf.cluster.%{_clustername}
%config(noreplace) %{_openlavatop}/etc/lsf.task
%config(noreplace) %{_openlavatop}/README
%config(noreplace) %{_openlavatop}/COPYING
%attr(0755,openlava,openlava) %{_openlavatop}/bin
%attr(0755,openlava,openlava) %{_openlavatop}/etc
%attr(0755,openlava,openlava) %{_openlavatop}/include
%attr(0755,openlava,openlava) %{_openlavatop}/lib
%attr(0755,openlava,openlava) %{_openlavatop}/log
%attr(0755,openlava,openlava) %{_openlavatop}/sbin
%attr(0755,openlava,openlava) %{_openlavatop}/share
%attr(0755,openlava,openlava) %{_openlavatop}/work
%attr(0755,openlava,openlava) %{_openlavatop}/work/logdir

%changelog
* Sun Oct 30 2011 modified the spec file so that autoconf creates
- openlava configuration files and use the outptu variables to make
- the necessary subsititution in the them. Change the post install
- to just erase the package without saving anything.
- Removed the symbolic link as that is something sites have to
- do as they may want to run more versions together, also
- in now the lsf.conf has the version in the openlava
- fundamental variables clearly indicating which version is in use.
* Sun Sep 4 2011 David Bigagli restructured to follow the new directory layout after
the GNU autoconf project.
* Thu Jul 14 2011 Robert Stober <robert@openlava.net> 1.0-1
- Enhanced support for RPM uninstall. rpm -e openlava
- will now stop the openlava daemons and then completely
- remove openlava.
- openlava configuration files and log files are saved to
- /tmp/openlava.$$.tar.gz
- Uninstallation supports shared and non-shared file system
- installations
* Sat Jul 9 2011 Robert Stober <robert@openlava.net> 1.0-1
- Added the following files so that they're installed by the RPM:
- lsb.hosts
- openmpi-mpirun
- mpich-mpirun
- lam-mpirun
- mpich2-mpiexec
- The RPM installer now uses the template files that are in the
- scripts directory instead of the standard files that are installed
- by make:
- lsf.cluster.openlava
- lsf.conf
- lsf.shared
- openlava
- openlava.csh
- openlava.sh
* Thu Jun 16 2011 Robert Stober <robert@openlava.net> 1.0-1
- Changed name of openlava startup script from "lava" to "openlava"
- Changed the name of the linux service from "lava" to openlava in
- the openlava startup script
- Changed the name of the openlava shell initialization scripts
- from lava.sh and lava.csh to openlava.sh and openlava.csh respectively.
- Changed the openlava.spec file to install the README and COPYING files.
- Added the openlava.setup script, which streamlines openlava setup
- on compute servers.
* Sat Jun 11 2011 Robert Stober <robert@openlava.net> 1.0-1
- Changed default install directory to /opt/openlava-1.0
- Installation now creates a symbolic link openlava -> openlava-1.0
- RPM is now relocatable. Specify --prefix /path/to/install/dir
- for example, rpm -ivh --prefix /opt/test openlava-1.0-1.x86_64.rpm installs
- /opt/test/openlava -> /opt/test/openlava-1.0
- Added creation of openlava user
- Changed default cluster name to "openlava"
- Added support for cstomizing the cluster name
- For example, export OPENLAVA_CLUSTER_NAME="bokisius"
- then rpm -ivh openlava-1.0-1.x86_64.rpm this will:
- 1. Set the cluster name in the lsf.shared file
- 2. renames the "clustername" directories
- The LSF binaries are now statically linked instead of being
- dynamically linked.
- Renamed /etc/init.d/lava.sh to /etc/init.d/lava
- The openlava shell initialization files lava.sh and lava.csh
- are now installed in /etc/profile.d
* Fri Apr 22 2011 Robert Stober <rmstober@gmail.com> 1.0-6.6
- Changed to install in /opt/lava
- Added support for autoconfig of various lava config files
- Removed creation of openlava user
* Fri May 30 2008 Shawn Starr <sstarr@platform.com> 1.0-6
- Fix symlinks for MVAPICH1/2.
* Tue May 27 2008 Gerry Wen <gwen@platform.com> 1.0-2
- Add wrapper script for MPICH2 mpiexec
* Mon Feb 13 2008 Shawn Starr <sstarr@platform.com> 1.0-1
- Make home directory for openlava user.
* Mon Jan 23 2008 Shawn Starr <sstarr@platform.com> 1.0-0
- Initial release of Lava 1.0
