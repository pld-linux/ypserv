Summary:	The NIS (Network Information Service) server
Summary(es):	Servidor NIS/YP
Summary(ja):	NIS(ネットワ〖ク攫鼠サ〖ビス)サ〖バ〖
Summary(pl):	Serwer NIS (Network Information Service)
Summary(pt_BR):	Servidor NIS/YP
Summary(ru):	笈易乓 NIS (Network Information Service)
Summary(uk):	笈易乓 NIS (Network Information Service)
Summary(zh_CN):	NIS(网络信息服务)服务器.
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

%description -l es
ypserv es una implementaci髇 del protocolo padr髇 de red NIS/YP.
Permite el uso distribuido de informaci髇 como hostname, username,
etc.

%description -l pl
NIS (Network Information Service) to system dostarczaj眂y informacje
sieciowe (nazwy u縴tkownik體, has砤, katalogi domowe, informacje o
grupach) wszystkim maszynom w sieci. NIS mo縠 pozwala� u縴tkownikom
logowa� si� na dowolnej maszynie w sieci pod warunkiem, 縠 maszyna ma
dzia砤j眂e programy klienckie NIS i has硂 u縴tkownika jest zapisane w
bazie hase� NIS. NIS by� wcze秐iej znany jako YP (Sun Yellow Pages).

Ten pakiet zawiera serwer NIS, kt髍y musi dzia砤� w sieci. Klienci nie
musz� dzia砤� na maszynie serwera.

%description -l pt_BR
ypserv � uma implementa玢o do protocolo padr鉶 de rede NIS/YP. Ele
permite o uso distribu韉o de informa珲es como hostname, username, etc.

%description -l ru
Network Information Service (NIS) - 茉� 由釉磐�, 讼韵伊� 幸拍嫌粤滋雅�
优耘渍� 晌葡彝撩衫 (滔巧钨, 辛蚁躺, 南土畚膳 肆粤滔巧, 且招匈 � �.�.)
子磐 土凵瘟� � 优陨. NIS 拖峙� 伊谝袍稍� 邢特谙琢耘萄� 兹夏 瘟 汤孪�
土凵闻 庞躺 瘟 茉鲜 土凵闻 诹姓菖钨 颂膳卧铀膳 幸锨伊屯� NIS � 辛蚁特
邢特谙琢耘萄 诹猩恿� � 铝谡 牧挝偃 辛蚁膛� NIS. NIS 伊闻� 沦� 哨着釉盼
肆� Sun Yellow Pages (YP).

显 辛伺� 酉呐抑稍 优易乓 NIS, 讼韵屹� 南讨盼 沦载 诹姓菖� � 琢叟�
优陨. 胩膳卧� NIS 闻 下掩廖� 诹姓铀猎� 优易乓 NIS.

跤粤蜗咨耘 ypserv 庞躺 琢� 握峙� 优易乓 NIS 奶� 琢叟� 优陨. 髁� 粤酥�
瘟南 抡呐� 沼粤蜗咨载 辛伺再 yp-tools � ypbind 瘟 肆帜鲜 土凵闻,
讼韵伊� 南讨瘟 沦载 颂膳卧贤 NIS.

%description -l uk
Network Information Service (NIS) - 门 由釉磐�, 阉� 瘟牧� 团遗峙渍
ξ葡彝撩 (滔铅紊, 辛蚁苔, 南土畚� 肆粤滔巧, 且招� � �.�.) 子ν
土凵瘟� � 团遗枝. NIS 拖峙 南谧咸稍� 讼疑釉兆赁镣 兹δ 瘟 抡呢-阉κ
土凵桅 阉菹 瘟 忙� 土凵桅 诹姓菖桅 颂Δ卧迂甩 幸锨伊蜕 NIS 粤 辛蚁特
讼疑釉兆赁� 诹猩恿紊� � 铝谡 牧紊� 辛蚁苔� NIS. NIS 伊桅叟 抡� 爪南蜕�
阉 Sun Yellow Pages (YP).

闩� 辛伺� 挺釉稍� 优易乓 NIS, 阉墒 邢咨闻� 抡陨 诹姓菖紊� � 琢郐�
团遗枝. 胩Δ卧� NIS 闻 邢咨挝� 诹姓铀猎� 优易乓 NIS.

饔粤蜗爪载 ypserv 阉菹 琢� 邢砸β盼 优易乓 NIS 奶� 琢巯� 团遗枝. 髁�
粤讼� 砸怕� 抡呐 子粤蜗咨陨 辛伺陨 yp-tools 粤 ypbind 瘟 讼治κ
土凵桅, 阉� 邢咨挝� 抡陨 颂Δ卧贤 NIS.

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
