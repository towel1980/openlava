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

%define _openlavaversion 1.0
%define _openlavatop /opt/openlava-%{_openlavaversion}
%define _clustername openlava
%define _libdir %{_openlavatop}/lib
%define _bindir %{_openlavatop}/bin
%define _sbindir %{_openlavatop}/etc
%define _mandir %{_openlavatop}/man
%define _logdir %{_openlavatop}/log
%define _includedir %{_openlavatop}/include/lsf

Summary: OpenLava(tm) Batch Scheduling and management
Name: openlava
Version: 1.0
Release: 1
License: GPLv2
Group: Applications/Productivity
Vendor: OpenLava Inc.
ExclusiveArch: x86_64
URL: http://www.openlava.net/
Source: %{name}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: gcc, tcl-devel, ncurses-devel
Requires: ncurses, tcl
Requires(pre): /usr/sbin/useradd
Requires(post): chkconfig
Requires(preun): chkconfig
Prefix: /opt

%description
OpenLava(tm) Batch scheduling

##
## PREP
##
%prep
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT

%setup -q -n %{name}

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

# Install binaries, daemons
make install INSTALL_PREFIX=$RPM_BUILD_ROOT

# overwrite files with templates
install -m 644 $RPM_BUILD_DIR/openlava/rpms/lsf.cluster.openlava $RPM_BUILD_ROOT%{_openlavatop}/conf
install -m 644 $RPM_BUILD_DIR/openlava/rpms/lsf.conf $RPM_BUILD_ROOT%{_openlavatop}/conf
install -m 644 $RPM_BUILD_DIR/openlava/rpms/lsf.shared $RPM_BUILD_ROOT%{_openlavatop}/conf
install -m 755 $RPM_BUILD_DIR/openlava/rpms/openlava $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 755 $RPM_BUILD_DIR/openlava/rpms/openlava.sh $RPM_BUILD_ROOT%{_openlavatop}/etc
install -m 755 $RPM_BUILD_DIR/openlava/rpms/openlava.csh $RPM_BUILD_ROOT%{_openlavatop}/etc

##
## PRE
##
%pre

##
## Add "openlava" user
##
/usr/sbin/useradd -c "OpenLava Administrator" -m -d /home/openlava openlava 2> /dev/null || :

##
## POST
##
%post

##
## set variables
##
_openlavatop=${RPM_INSTALL_PREFIX}/openlava-1.0
_symlink=${RPM_INSTALL_PREFIX}/openlava

##
## set the clustername if the OPENLAVA_CLUSTER_NAME is set
##
if [ x"${OPENLAVA_CLUSTER_NAME}" = x ]; then
	_clustername=%{_clustername}
else
	_clustername=${OPENLAVA_CLUSTER_NAME}
	mv ${_openlavatop}/work/openlava ${_openlavatop}/work/${_clustername}
	mv ${_openlavatop}/conf/lsbatch/openlava ${_openlavatop}/conf/lsbatch/${_clustername}
	mv ${_openlavatop}/conf/lsf.cluster.openlava ${_openlavatop}/conf/lsf.cluster.${_clustername}
fi
 
##
## create the symbolic link
##
ln -sf ${_openlavatop} ${_symlink}

##
## customize the openlava.sh file
##
sed -i -e "s#__LAVATOP__#${_symlink}#" ${_symlink}/etc/openlava.sh
sed -i -e "s#__LAVATOP__#${_symlink}#" ${_symlink}/etc/openlava.csh

##
## customize the openlava startup file
##
sed -i -e "s#__LAVATOP__#${_symlink}#" ${_symlink}/etc/openlava

##
## copy scripts into the relevant directories
##
cp ${_symlink}/etc/openlava.sh %{_sysconfdir}/profile.d
cp ${_symlink}/etc/openlava.csh %{_sysconfdir}/profile.d
cp ${_symlink}/etc/openlava %{_sysconfdir}/init.d

# Register lava daemons
/sbin/chkconfig --add openlava
/sbin/chkconfig openlava on

##
## customize the lsf.cluster.clustername file
##
hostname=`hostname`
sed -i -e "s/__HOSTNAME__/$hostname/" ${_symlink}/conf/lsf.cluster.${_clustername}

##
## customize the lsf.conf file
##
sed -i -e "s#__LAVATOP__#${_symlink}#" ${_symlink}/conf/lsf.conf

##
## customize the lsf.shared file
##
sed -i -e "s/__CLUSTERNAME__/${_clustername}/" ${_symlink}/conf/lsf.shared

##
## PREUN
##
%preun
if [ $1 = 0 ]; then
   /sbin/service openlava stop > /dev/null 2>&1
   /sbin/chkconfig openlava off
   /sbin/chkconfig --del openlava
fi

##
## POSTUN
##
%postun

# lets clean up everything else
_openlavatop=${RPM_INSTALL_PREFIX}/openlava-1.0
_symlink=${RPM_INSTALL_PREFIX}/openlava
_savedir=openlava.$$

mkdir -p ${_savedir}
mv -f ${_openlavatop}/log/* ${_savedir} >/dev/null 2>&1
mv -f ${_openlavatop}/conf/* ${_savedir} >dev/null 2>&1
mv -f ${_openlavatop}/work/openlava/logdir/lsb.acct ${_savedir} >/dev/null 2>&1
mv -f ${_openlavatop}/work/openlava/logdir/lsb.events ${_savedir} >/dev/null 2>&1

# remove the scripts
rm -f /etc/init.d/openlava
rm -f /etc/profile.d/openlava.*

tar cvzf ${_savedir}.tar.gz ${_savedir} >/dev/null 2>&1
rm -rf ${_savedir}
mv -f ${_savedir}.tar.gz /tmp

echo
echo "Thank you for using openlava!" 
echo "Your openlava configuration and log files have been saved to /tmp/${_savedir}.tar.gz"

rm -rf ${_openlavatop}
rm -f ${_symlink} 

##
## FILES
##
%files
%defattr(-,root,root)
#%{_openlavatop}/%{_openlavaversion}/misc
%attr(0755,root,root) %{_openlavatop}/etc/openlava
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
#%{_bindir}/mvapich2-mpiexec
#%{_bindir}/mvapich1-mpirun
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

# libraries
%{_libdir}/liblsf.a
%{_libdir}/liblsfbat.a

# headers
%{_includedir}/lsbatch.h
%{_includedir}/lsf.h

# docs
%doc COPYING

%defattr(0644,openlava,openlava)
%config(noreplace) %{_openlavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.params
%config(noreplace) %{_openlavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.queues
%config(noreplace) %{_openlavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.hosts
%config(noreplace) %{_openlavatop}/conf/lsbatch/%{_clustername}/configdir/lsb.users
%config(noreplace) %{_openlavatop}/conf/lsf.shared
%config(noreplace) %{_openlavatop}/conf/lsf.conf
%config(noreplace) %{_openlavatop}/conf/lsf.cluster.%{_clustername}
%config(noreplace) %{_openlavatop}/conf/lsf.task
%config(noreplace) %{_openlavatop}/conf/README
%config(noreplace) %{_openlavatop}/conf/COPYING
%attr(-,openlava,openlava) %{_openlavatop}/work/*
%attr(-,openlava,openlava) %dir %{_logdir}

%changelog
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
