# TODO
# - /usr/include/rpcsvc/ypxfrd.x should be in -devel package?
Summary:	The NIS (Network Information Service) server
Summary(es.UTF-8):	Servidor NIS/YP
Summary(ja.UTF-8):	NIS(ネットワーク情報サービス)サーバー
Summary(pl.UTF-8):	Serwer NIS (Network Information Service)
Summary(pt_BR.UTF-8):	Servidor NIS/YP
Summary(ru.UTF-8):	Сервер NIS (Network Information Service)
Summary(uk.UTF-8):	Сервер NIS (Network Information Service)
Summary(zh_CN.UTF-8):	NIS(网络信息服务)服务器
Name:		ypserv
Version:	2.31
Release:	3
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.linux-nis.org/download/ypserv/%{name}-%{version}.tar.bz2
# Source0-md5:	4537b8f0e917edca8f57b70b9cbc37f3
Source1:	%{name}-%{name}.init
Source2:	%{name}-yppasswdd.init
Source3:	%{name}-ypxfrd.init
Source4:	%{name}.sysconfig
Patch0:		%{name}-ypMakefile.patch
Patch1:		%{name}-path.patch
Patch2:		%{name}-nfsnobody.patch
Patch3:		%{name}-awk.patch
URL:		http://www.linux-nis.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7
BuildRequires:	gdbm-devel
BuildRequires:	libwrap-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	FHS >= 2.3-18
Requires:	glibc >= 2.2
Requires:	portmap
Requires:	rc-scripts >= 0.4.1.5
Obsoletes:	yppasswd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

mv -f etc/README etc/README.etc

%build
%configure \
	--enable-check-root \
	--enable-fqdn \
	--enable-yppasswd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	YPMAPDIR=/var/yp

install etc/ypserv.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/yppasswdd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/ypxfrd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/ypserv

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add ypserv
%service ypserv restart "YP server"

/sbin/chkconfig --add yppasswdd
%service yppasswdd restart "YP password changing server"

/sbin/chkconfig --add ypxfrd
%service ypxfrd restart "YP map server"

%triggerpostun -- yppasswd
/sbin/chkconfig --add yppasswdd

%preun
if [ "$1" = "0" ]; then
	%service ypserv stop
	/sbin/chkconfig --del ypserv

	%service yppasswdd stop
	/sbin/chkconfig --del yppasswdd

	%service ypxfrd stop
	/sbin/chkconfig --del ypxfrd
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO NEWS
%doc etc/ypserv.conf etc/securenets etc/README.etc
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/yp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ypserv.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ypserv
%config(noreplace) %verify(not md5 mtime size) /var/yp/Makefile
%attr(754,root,root) /etc/rc.d/init.d/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_includedir}/rpcsvc/ypxfrd.x
