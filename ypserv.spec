Summary:	The NIS (Network Information Service) server
Summary(es):	Servidor NIS/YP
Summary(ja):	NIS(�ͥåȥ�����󥵡��ӥ�)�����С�
Summary(pl):	Serwer NIS (Network Information Service)
Summary(pt_BR):	Servidor NIS/YP
Summary(ru):	������ NIS (Network Information Service)
Summary(uk):	������ NIS (Network Information Service)
Summary(zh_CN):	NIS(������Ϣ����)������.
Name:		ypserv
Version:	2.14
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
# Source0-md5:	e94688fb7ccf8fcc92821bdc08d40e36
Source1:	%{name}-%{name}.init
Source2:	%{name}-yppasswdd.init
Source3:	%{name}-ypxfrd.init
Patch0:		%{name}-ypMakefile.patch
Patch1:		%{name}-path.patch
Patch2:		%{name}-nfsnobody.patch
URL:		http://www.linux-nis.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gdbm-devel
BuildRequires:	libwrap-devel
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	glibc >= 2.2
Requires:	portmap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yppasswd

%define		_libexecdir	%{_libdir}/yp

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

mv -f etc/README etc/README.etc

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-check-root \
	--enable-fqdn \
	--enable-yppasswd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	YPMAPDIR=/var/yp

install etc/ypserv.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/yppasswdd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypxfrd

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
/sbin/chkconfig --add ypxfrd
if [ -f /var/lock/subsys/ypxfrd ]; then
	/etc/rc.d/init.d/ypxfrd restart >&2
else
	echo "Run '/etc/rc.d/init.d/ypxfrd start' to start YP map server." >&2
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
	if [ -f /var/lock/subsys/ypxfrd ]; then
		/etc/rc.d/init.d/ypxfrd stop >&2
	fi
	/sbin/chkconfig --del ypxfrd
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO NEWS
%doc etc/ypserv.conf etc/securenets etc/README.etc
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/yp
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ypserv.conf
%dir /var/yp
%config(noreplace) %verify(not size mtime md5) /var/yp/Makefile
%attr(754,root,root) /etc/rc.d/init.d/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_includedir}/rpcsvc/ypxfrd.x
