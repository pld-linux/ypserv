Summary:	The NIS (Network Information Service) server
Name:		ypserv
Version:	1.3.11a
Release:	2
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.us.kernel.org/pub/linux/utils/NIS/%{name}-1.3.11.tar.gz
Source1:	%{name}-ypserv.init
Source2:	%{name}-yppasswdd.init
Patch0:		%{name}-ypMakefile.patch
Patch1:		%{name}-conf.patch
Patch2:		%{name}-remember.patch
Patch3:		%{name}-libwrap.patch
Patch4:		%{name}-1.3.11a.diff
Patch5:		%{name}-syslog.patch
URL:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
BuildRequires:	gdbm-devel
BuildRequires:	libwrap-devel
Requires:	portmap
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yppasswd

%define		_libexecdir	/usr/lib/yp

%description
The Network Information Service (NIS) is a system which provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network. NIS can enable users
to login on any machine on the network, as long as the machine has the
NIS client programs running and the user's password is recorded in the
NIS passwd database. NIS was formerly known as Sun Yellow Pages (YP).

This package provides the NIS server, which will need to be running on
your network. NIS clients do not need to be running the server.

Install ypserv if you need an NIS server for your network. You'll also
need to install the yp-tools and ypbind packages onto any NIS client
machines.

%prep
%setup -q -n %{name}-1.3.11
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1

%build
cp etc/README etc/README.etc
rm -f config.cache
%{configure} \
	--enable-tcp-wrapper \
	--enable-fqdn \
	--enable-yppasswd 

%{__make} MAN1DIR=%{_mandir}/man1 \
	MAN5DIR=%{_mandir}/man5 \
	MAN8DIR=%{_mandir}/man8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	ROOT=$RPM_BUILD_ROOT \
	YPMAPDIR=/var/yp \
	MAN1DIR=%{_mandir}/man1 \
	MAN5DIR=%{_mandir}/man5 \
	MAN8DIR=%{_mandir}/man8 \
	INSTALL="/usr/bin/install -c"

install etc/ypserv.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/yppasswdd

gzip -9nf {README,README.secure,INSTALL,ChangeLog,TODO} \
	{etc/ypserv.conf,etc/securenets,etc/README.etc}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add ypserv
if [ -f /var/lock/subsys/ypserv ]; then
	/etc/rc.d/init.d/ypserv restart >&2
else
	echo "Run '/etc/rc.d/init.d/ypserv start' to start YP server." >&2
fi
/sbin/chkconfig --add yppasswdd
if [ -f /var/lock/subsys/yppasswdd ]; then
	/etc/rc.d/init.d/yppasswdd restart >&2
else
	echo "Run '/etc/rc.d/init.d/yppasswdd start' to start YP password changing server." >&2
fi

%triggerpostun -- ypserv <= ypserv-1.3.0-2
/sbin/chkconfig --add ypserv

%trigerpostun -- yppasswd
/sbin/chkconfig --add yppasswdd

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/ypserv ]; then
		/etc/rc.d/init.d/ypserv stop >&2
	fi
	/sbin/chkconfig --del ypserv
	if [ -f /var/lock/subsys/yppasswdd ]; then
		/etc/rc.d/init.d/yppasswdd stop >&2
	fi
	/sbin/chkconfig --del yppasswdd
fi
 
%files
%defattr(644,root,root,755)
%doc {README,README.secure,INSTALL,ChangeLog,TODO}.gz
%doc {etc/ypserv.conf,etc/securenets,etc/README.etc}.gz
%config %{_sysconfdir}/ypserv.conf
%config %{_sysconfdir}/netgroup
%config /var/yp/*
%attr(754,root,root) %config /etc/rc.d/init.d/*
%dir /var/yp
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/yp/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_includedir}/*/*
