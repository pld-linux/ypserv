Summary:	The NIS (Network Information Service) server
Summary(es.UTF-8):   Servidor NIS/YP
Summary(ja.UTF-8):   NIS(ネットワーク情報サービス)サーバー
Summary(pl.UTF-8):   Serwer NIS (Network Information Service)
Summary(pt_BR.UTF-8):   Servidor NIS/YP
Summary(ru.UTF-8):   Сервер NIS (Network Information Service)
Summary(uk.UTF-8):   Сервер NIS (Network Information Service)
Summary(zh_CN.UTF-8):   NIS(网络信息服务)服务器.
Name:		ypserv
Version:	2.6
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
Source1:	%{name}-%{name}.init
Source2:	%{name}-yppasswdd.init
Source3:	%{name}-ypxfrd.init
Patch0:		%{name}-ypMakefile.patch
Patch1:		%{name}-syslog.patch
Patch2:		%{name}-path.patch
Patch3:		%{name}-nfsnobody.patch
URL:		http://www.linux-nis.org/
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

%description -l es.UTF-8
ypserv es una implementación del protocolo padrón de red NIS/YP.
Permite el uso distribuido de información como hostname, username,
etc.

%description -l pl.UTF-8
NIS (Network Information Service) to system dostarczający informacje
sieciowe (nazwy użytkowników, hasła, katalogi domowe, informacje o
grupach) wszystkim maszynom w sieci. NIS może pozwalać użytkownikom
logować się na dowolnej maszynie w sieci pod warunkiem, że maszyna ma
działające programy klienckie NIS i hasło użytkownika jest zapisane w
bazie haseł NIS. NIS był wcześniej znany jako YP (Sun Yellow Pages).

Ten pakiet zawiera serwer NIS, który musi działać w sieci. Klienci nie
muszą działać na maszynie serwera.

%description -l pt_BR.UTF-8
ypserv é uma implementação do protocolo padrão de rede NIS/YP. Ele
permite o uso distribuído de informações como hostname, username, etc.

%description -l ru.UTF-8
Network Information Service (NIS) - это система, которая предоставляет
сетевую информацию (логины, пароли, домашние каталоги, группы и т.п.)
всем машинам в сети. NIS может разрешить пользователям вход на любой
машине если на этой машине запущены клиентские программы NIS и пароль
пользователя записан в базу данных паролей NIS. NIS ранее был известен
как Sun Yellow Pages (YP).

Этот пакет содержит сервер NIS, который должен быть запущен в вашей
сети. Клиенты NIS не обязаны запускать сервер NIS.

Установите ypserv если вам нужен сервер NIS для вашей сети. Вам также
надо будет установить пакеты yp-tools и ypbind на каждой машине,
которая должна быть клиентом NIS.

%description -l uk.UTF-8
Network Information Service (NIS) - це система, яка надає мережеву
інформацію (логіни, паролі, домашні каталоги, групи і т.і.) всім
машинам у мережі. NIS може дозволити користувачам вхід на будь-якій
машині якщо на цій машині запущені клієнтські програми NIS та пароль
користувача записаний у базу даних паролів NIS. NIS раніше був відомий
як Sun Yellow Pages (YP).

Цей пакет містить сервер NIS, який повинен бути запущений у вашій
мережі. Клієнти NIS не повинні запускати сервер NIS.

Встановіть ypserv якщо вам потрібен сервер NIS для вашої мережі. Вам
також треба буде встановити пакети yp-tools та ypbind на кожній
машині, яка повинна бути клієнтом NIS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv etc/README etc/README.etc
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
%doc README INSTALL ChangeLog TODO NEWS
%doc etc/ypserv.conf etc/securenets etc/README.etc
%config %{_sysconfdir}/ypserv.conf
%config /var/yp/*
%attr(754,root,root) /etc/rc.d/init.d/*
%dir /var/yp
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/yp/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_includedir}/*/*
