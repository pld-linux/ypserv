Summary:	The NIS (Network Information Service) server
Summary(es):	Servidor NIS/YP
Summary(pl):	Serwer NIS (Network Information Service)
Summary(pt_BR):	Servidor NIS/YP
Summary(ru):	Сервер NIS (Network Information Service)
Summary(uk):	Сервер NIS (Network Information Service)
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
ypserv es una implementaciСn del protocolo padrСn de red NIS/YP.
Permite el uso distribuido de informaciСn como hostname, username,
etc.

%description -l pl
NIS (Network Information Service) to system dostarczaj╠cy informacje
sieciowe (nazwy u©ytkownikСw, hasЁa, katalogi domowe, informacje o
grupach) wszystkim maszynom w sieci. NIS mo©e pozwalaФ u©ytkownikom
logowaФ siЙ na dowolnej maszynie w sieci pod warunkiem, ©e maszyna ma
dziaЁaj╠ce programy klienckie NIS i hasЁo u©ytkownika jest zapisane w
bazie haseЁ NIS. NIS byЁ wcze╤niej znany jako YP (Sun Yellow Pages).

Ten pakiet zawiera serwer NIS, ktСry musi dziaЁaФ w sieci. Klienci nie
musz╠ dziaЁaФ na maszynie serwera.

%description -l pt_BR
ypserv И uma implementaГЦo do protocolo padrЦo de rede NIS/YP. Ele
permite o uso distribuМdo de informaГУes como hostname, username, etc.

%description -l ru
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

%description -l uk
Network Information Service (NIS) - це система, яка нада╓ мережеву
╕нформац╕ю (лог╕ни, парол╕, домашн╕ каталоги, групи ╕ т.╕.) вс╕м
машинам у мереж╕. NIS може дозволити користувачам вх╕д на будь-як╕й
машин╕ якщо на ц╕й машин╕ запущен╕ кл╕╓нтськ╕ програми NIS та пароль
користувача записаний у базу даних парол╕в NIS. NIS ран╕ше був в╕домий
як Sun Yellow Pages (YP).

Цей пакет м╕стить сервер NIS, який повинен бути запущений у ваш╕й
мереж╕. Кл╕╓нти NIS не повинн╕ запускати сервер NIS.

Встанов╕ть ypserv якщо вам потр╕бен сервер NIS для вашо╖ мереж╕. Вам
також треба буде встановити пакети yp-tools та ypbind на кожн╕й
машин╕, яка повинна бути кл╕╓нтом NIS.

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
