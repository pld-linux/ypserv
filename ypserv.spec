Summary:	The NIS (Network Information Service) server.
Url:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
Name:		ypserv
Version:	1.3.6.94
Release:	1
Copyright:	GNU
Group:		System Environment/Daemons
Source0:	ftp://ftp.us.kernel.org/pub/linux/utils/NIS/%{name}-%{version}.tar.gz
Source1:	ypserv-ypserv.init
Source2:	ypserv-yppasswdd.init
Requires:	portmap tcp_wrappers
Prereq:		/sbin/chkconfig
Buildroot:	/tmp/%{name}-%{version}-root
Obsoletes:	yppasswd

%description
The Network Information Service (NIS) is a system which provides network
information (login names, passwords, home directories, group information)
to all of the machines on a network.  NIS can enable users to login on
any machine on the network, as long as the machine has the NIS client
programs running and the user's password is recorded in the NIS passwd
database.  NIS was formerly known as Sun Yellow Pages (YP).

This package provides the NIS server, which will need to be running on
your network.  NIS clients do not need to be running the server.

Install ypserv if you need an NIS server for your network.  You'll also
need to install the yp-tools and ypbind packages onto any NIS client
machines.

%prep
%setup -q

%build
cp etc/README etc/README.etc
CFLAGS=$RPM_OPT_FLAGS \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--enable-tcp-wrapper \
	--enable-fqdn \
	--enable-yppasswd 

make MAN1DIR=%{_mandir}/man1 \
	MAN5DIR=%{_mandir}/man5 \
	MAN8DIR=%{_mandir}/man8

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	YPMAPDIR=$RPM_BUILD_ROOT/var/yp \
	MAN1DIR=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	MAN5DIR=$RPM_BUILD_ROOT/%{_mandir}/man5 \
	MAN8DIR=$RPM_BUILD_ROOT/%{_mandir}/man8

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install etc/ypserv.conf $RPM_BUILD_ROOT/etc
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/yppasswdd

strip --strip-unneeded $RPM_BUILD_ROOT/%{_sbindir}/* \
	$RPM_BUILD_ROOT/usr/lib/yp/* || :

gzip -9nf {README,README.secure,INSTALL,ChangeLog,TODO} \
	{etc/ypserv.conf,etc/securenets,etc/README.etc} \
	$RPM_BUILD_ROOT/%{_mandir}/man{5,8}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add ypserv
/sbin/chkconfig --add yppasswdd

%triggerpostun -- ypserv <= ypserv-1.3.0-2
/sbin/chkconfig --add ypserv

%trigerpostun -- yppasswd
/sbin/chkconfig --add yppasswdd

%postun
if [ $1 = 0 ]; then
	/sbin/chkconfig --del ypserv
	/sbin/chkconfig --del yppasswdd
fi
 
%files
%defattr(644,root,root,755)
%doc {README,README.secure,INSTALL,ChangeLog,TODO}.gz
%doc {etc/ypserv.conf,etc/securenets,etc/README.etc}.gz
%config /etc/ypserv.conf
%config /var/yp/*
%attr(754,root,root) %config /etc/rc.d/init.d/*
%dir /var/yp
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) /usr/lib/yp/*
%{_mandir}/man5/*
%{_mandir}/man8/*
/usr/include/*/*

%changelog
* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- version 1.3.6.91

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Mon Feb  8 1999 Bill Nottingham <notting@redhat.com>
- move to start before ypbind

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1
- upgraded to 1.3.5

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- yppasswd.init: lock file must have same name as init.d script, not daemon

* Sat Jul 11 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.3.4
- fixed the fubared Makefile
- link against gdbm instead of ndbm (it seems to work better)

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.3.1
- enhanced init scripts

* Fri May 01 1998 Jeff Johnson <jbj@redhat.com>
- added triggerpostun
- Use libdb fro dbp_*().

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 13 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.3.0

* Wed Dec 03 1997 Cristian Gafton <gafton@redhat.com>
- updated to 1.2.5
- added buildroot; updated spec file
- added yppasswdd init file

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- init script shouldn't set the domain name

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>
- supports chkconfig
- updated initscript for status and restart
- turned off in all runlevels, by default
- removed postinstall script which didn't do anything

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- added patch to build against later glibc

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Apr 23 1997 Erik Troan <ewt@redhat.com>
- updated to 1.1.7.

* Fri Mar 14 1997 Erik Troan <ewt@redhat.com>
- Updated to ypserv 1.1.5, ported to Alpha (glibc).

* Fri Mar 07 1997 Erik Troan <ewt@redhat.com>
- Removed -pedantic which confuses the SPARC :-(
