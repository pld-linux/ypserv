Summary:	The NIS (Network Information Service) server
Summary(es):	Servidor NIS/YP
Summary(pl):	Serwer NIS (Network Information Service)
Summary(pt_BR):	Servidor NIS/YP
Summary(ru):	������ NIS (Network Information Service)
Summary(uk):	������ NIS (Network Information Service)
Name:		ypserv
Version:	1.3.12
Release:	6
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.us.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
Source1:	%{name}-%{name}.init
Source2:	%{name}-yppasswdd.init
Source3:	%{name}-yppaswd.sysconfig
Patch0:		%{name}-ypMakefile.patch
Patch1:		%{name}-conf.patch
Patch2:		%{name}-remember.patch
Patch3:		%{name}-libwrap.patch
Patch4:		%{name}-syslog.patch
Patch5:		%{name}-security.patch
Patch6:		%{name}-security-memory_leak_fix.patch
URL:		http://www-vt.uni-paderborn.de/~kukuk/linux/nis.html
BuildRequires:	gdbm-devel
BuildRequires:	libwrap-devel
Requires:	glibc >= 2.2
Requires:	portmap
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yppasswd
Conflicts:	glibc <= 2.1.3

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

%description -l es
ypserv es una implementaci�n del protocolo padr�n de red NIS/YP.
Permite el uso distribuido de informaci�n como hostname, username,
etc.

%description -l pl
NIS (Network Information Service) to system dostarczaj�cy informacje
sieciowe (nazwy u�ytkownik�w, has�a, katalogi domowe, informacje o
grupach) wszystkim maszynom w sieci. NIS mo�e pozwala� u�ytkownikom
logowa� si� na dowolnej maszynie w sieci pod warunkiem, �e maszyna ma
dzia�aj�ce programy klienckie NIS i has�o u�ytkownika jest zapisane w
bazie hase� NIS. NIS by� wcze�niej znany jako YP (Sun Yellow Pages).

Ten pakiet zawiera serwer NIS, kt�ry musi dzia�a� w sieci. Klienci nie
musz� dzia�a� na maszynie serwera.

%description -l pt_BR
ypserv � uma implementa��o do protocolo padr�o de rede NIS/YP. Ele
permite o uso distribu�do de informa��es como hostname, username, etc.

%description -l ru
Network Information Service (NIS) - ��� �������, ������� �������������
������� ���������� (������, ������, �������� ��������, ������ � �.�.)
���� ������� � ����. NIS ����� ��������� ������������� ���� �� �����
������ ���� �� ���� ������ �������� ���������� ��������� NIS � ������
������������ ������� � ���� ������ ������� NIS. NIS ����� ��� ��������
��� Sun Yellow Pages (YP).

���� ����� �������� ������ NIS, ������� ������ ���� ������� � �����
����. ������� NIS �� ������� ��������� ������ NIS.

���������� ypserv ���� ��� ����� ������ NIS ��� ����� ����. ��� �����
���� ����� ���������� ������ yp-tools � ypbind �� ������ ������,
������� ������ ���� �������� NIS.

%description -l uk
Network Information Service (NIS) - �� �������, ��� ����� ��������
�������æ� (��Ǧ��, ����̦, �����Φ ��������, ����� � �.�.) �Ӧ�
������� � ����֦. NIS ���� ��������� ������������ �Ȧ� �� ����-�˦�
����Φ ���� �� æ� ����Φ ������Φ �̦�����˦ �������� NIS �� ������
����������� ��������� � ���� ����� ����̦� NIS. NIS ��Φ�� ��� צ�����
�� Sun Yellow Pages (YP).

��� ����� ͦ����� ������ NIS, ���� ������� ���� ��������� � ��ۦ�
����֦. �̦���� NIS �� �����Φ ��������� ������ NIS.

������צ�� ypserv ���� ��� ���Ҧ��� ������ NIS ��� ���ϧ ����֦. ���
����� ����� ���� ���������� ������ yp-tools �� ypbind �� ���Φ�
����Φ, ��� ������� ���� �̦����� NIS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

mv etc/README etc/README.etc
%build
#aclocal
#autoconf
%configure2_13 \
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
	INSTALL="install -c"

install etc/ypserv.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/yppasswdd
install -d $RPM_BUILD_ROOT/etc/sysconfig/
install ${SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/yppasswdd

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add ypserv
if [ -f /var/lock/subsys/ypserv ]; then
	/etc/rc.d/init.d/ypserv restart >&2
else
	echo "Run '/etc/rc.d/init.d/ypserv start' to start NIS server." >&2
fi
/sbin/chkconfig --add yppasswdd
if [ -f /var/lock/subsys/yppasswdd ]; then
	/etc/rc.d/init.d/yppasswdd restart >&2
else
	echo "Run '/etc/rc.d/init.d/yppasswdd start' to start NIS password changing server." >&2
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
%doc README README.secure INSTALL ChangeLog TODO
%doc etc/ypserv.conf etc/securenets etc/README.etc
%config %{_sysconfdir}/sysconfig/yppasswdd
%config %{_sysconfdir}/ypserv.conf
%config %{_sysconfdir}/netgroup
%config /var/yp/*
%attr(754,root,root) /etc/rc.d/init.d/*
%dir /var/yp
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/yp/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_includedir}/*/*
