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
	ROOT=$RPM_BUILD_ROOT \
	YPMAPDIR=/var/yp \
	MAN1DIR=%{_mandir}/man1 \
	MAN5DIR=%{_mandir}/man5 \
	MAN8DIR=%{_mandir}/man8

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
