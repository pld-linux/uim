#
# TODO:
#	- SPLIT IT!
#	--enable-kde4-applet
#
Summary:	Multilingual input method library
Summary(pl.UTF-8):	Biblioteka obsługująca wejście w wielu językach
Name:		uim
Version:	1.7.0
Release:	0.1
License:	GPL or BSD
Group:		Libraries
Source0:	http://uim.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	1633f131ea58b34fd85e15411e3cc363
Source1:	uim-init.el
Source2:	xinput.d-uim
Patch0:		%{name}-link.patch
Patch1:		%{name}-emacs-utf8.patch
Patch2:		%{name}-enable-libgcroots.patch
URL:		http://uim.freedesktop.org/
BuildRequires:	anthy-devel >= 9100h-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	Canna-devel
BuildRequires:	curl-devel
BuildRequires:	eb-devel
BuildRequires:	expat-devel
BuildRequires:	gcc-objc
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	gtk+3-devel
#BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libedit-devel
BuildRequires:	libffi-devel
BuildRequires:	libgcroots-devel
BuildRequires:	libgnome-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	m17n-lib-devel
BuildRequires:	mana
BuildRequires:	openssl-devel
BuildRequires:	qt4-qmake
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uim is a multilingual input method library. Uim's project goal is to
provide secure and useful input method for all languages.

%description -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznej i użytecznej metody dla
wszystkich języków.

%package devel
Summary:	Header files for uim libraryi
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki uim
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for uim library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki uim.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-openssl \
	--enable-gnome2-applet \
	--enable-gnome3-applet \
	--disable-qt4-qt3support \
	--enable-default-toolkit=gtk3 \
	--enable-dict \
	--enable-pref \
	--enable-notify=libnotify \
	--without-scim \
	--with-anthy-utf8 \
	--with-canna \
	--with-mana \
	--with-prime \
	--without-sj3 \
	--without-skk \
	--with-curl \
	--with-expat \
	--with-ssl-engine \
	--with-sqlite3 \
	--with-ffi \
	--with-x \
	--with-xft \
	--with-gtk2 \
	--with-gtk3 \
	--with-qt4 \
	--with-qt4-immodule \
	--with-libedit \
	--with-eb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}{,/gtk*/*/immodules,/uim/*}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun
umask 022
/sbin/ldconfig
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/uim-el-agent
%attr(755,root,root) %{_bindir}/uim-el-helper-agent
%attr(755,root,root) %{_bindir}/uim-fep
%attr(755,root,root) %{_bindir}/uim-fep-tick
%attr(755,root,root) %{_bindir}/uim-help
%attr(755,root,root) %{_bindir}/uim-input-pad-ja
%attr(755,root,root) %{_bindir}/uim-m17nlib-relink-icons
%attr(755,root,root) %{_bindir}/uim-module-manager
%attr(755,root,root) %{_bindir}/uim-sh
%attr(755,root,root) %{_bindir}/uim-xim
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.[0-9]
%attr(755,root,root) %{_libdir}/uim-helper-server
%attr(755,root,root) %{_libdir}/uim-toolbar-applet-gnome3
%dir %{_libdir}/uim
%dir %{_libdir}/uim/notify
%attr(755,root,root) %{_libdir}/uim/notify/libuimnotify*.so
%dir %{_libdir}/uim/plugin
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-anthy-utf8.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-anthy.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-curl.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-custom-enabler.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-eb.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-editline.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-expat.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-ffi.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-fileio.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-lolevel.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-look.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-m17nlib.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-mana.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-openssl.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-process.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-skk.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-socket.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-sqlite3.so
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%{_desktopdir}/uim.desktop
%{_datadir}/dbus-1/services/org.gnome.panel.applet.UimAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/UimApplet.panel-applet
%{_mandir}/man1/*.1*

%attr(755,root,root) %{_bindir}/uim-dict-gtk
%attr(755,root,root) %{_bindir}/uim-im-switcher-gtk
%attr(755,root,root) %{_bindir}/uim-pref-gtk
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk-systray
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/*.so
%attr(755,root,root) %{_libdir}/uim-candwin-gtk
%attr(755,root,root) %{_libdir}/uim-candwin-tbl-gtk

%attr(755,root,root) %{_bindir}/uim-dict-gtk3
%attr(755,root,root) %{_bindir}/uim-im-switcher-gtk3
%attr(755,root,root) %{_bindir}/uim-input-pad-ja-gtk3
%attr(755,root,root) %{_bindir}/uim-pref-gtk3
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk3
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk3-systray
%attr(755,root,root) %{_libdir}/gtk-3.0/*/immodules/*.so
%attr(755,root,root) %{_libdir}/uim-candwin-gtk3
%attr(755,root,root) %{_libdir}/uim-candwin-tbl-gtk3

%attr(755,root,root) %{_bindir}/uim-chardict-qt4
%attr(755,root,root) %{_bindir}/uim-im-switcher-qt4
%attr(755,root,root) %{_bindir}/uim-pref-qt4
%attr(755,root,root) %{_bindir}/uim-toolbar-qt4
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/*.so
%attr(755,root,root) %{_libdir}/uim-candwin-qt4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
