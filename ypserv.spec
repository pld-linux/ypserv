Summary:	The NIS (Network Information Service) server
Summary(es):	Servidor NIS/YP
Summary(ja):	NIS(╔м╔ц╔х╔О║╪╔╞╬ПйС╔╣║╪╔с╔╧)╔╣║╪╔п║╪
Summary(pl):	Serwer NIS (Network Information Service)
Summary(pt_BR):	Servidor NIS/YP
Summary(ru):	Сервер NIS (Network Information Service)
Summary(uk):	Сервер NIS (Network Information Service)
Summary(zh_CN):	NIS(мЬбГпео╒╥ЧнЯ)╥ЧнЯфВ.
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
