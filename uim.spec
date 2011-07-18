Summary:	Multilingual input method library
Summary(pl.UTF-8):	Biblioteka obsługująca wejście w wielu językach
Name:		uim
Version:	1.7.0
Release:	1
License:	GPL or BSD
Group:		Libraries
Source0:	http://uim.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	1633f131ea58b34fd85e15411e3cc363
Source1:	%{name}.xinputd
Source2:	%{name}-init.el
Patch0:		%{name}-link.patch
Patch1:		%{name}-emacs-utf8.patch
Patch2:		%{name}-enable-libgcroots.patch
Patch3:		%{name}-qt-po.patch
URL:		http://uim.freedesktop.org/
BuildRequires:	Canna-devel
BuildRequires:	Qt3Support-devel
BuildRequires:	anthy-devel >= 9100h-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	eb-devel
BuildRequires:	expat-devel
BuildRequires:	gcc-objc
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	gtk+3-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libedit-devel
BuildRequires:	libffi-devel
BuildRequires:	libgcroots-devel
BuildRequires:	libgnome-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	m17n-lib-devel
BuildRequires:	mana
BuildRequires:	openssl-devel
BuildRequires:	qt-devel
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
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages. Currently, it can input to
applications which support Gtk+'s immodule, Qt's immodule and XIM.

This package provides the input method library, the XIM bridge and
most of the input methods.

For the Japanese input methods you need to install
- uim-anthy for Anthy
- uim-canna for Canna
- uim-skk for SKK.

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

%package gtk2
Summary:	GTK+2 support for Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
# for update-gtk-immodules
Requires(post):	gtk+2 >= 2.9.1-2
Requires(postun):	gtk+2

%description gtk2
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the Gtk IM module and helper program.

%package gtk3
Summary:	GTK+3 support for Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
# for update-gtk-immodules
Requires(post):	gtk+3
Requires(postun):	gtk+3

%description gtk3
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the Gtk IM module and helper program.

%package gnome
Summary:	GNOME Applet for Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	uim-gtk3

%description gnome
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the GNOME panel applet.

%package qt
Summary:	Qt4 support for Uim
Group:		X11/Applications

%description qt
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the Qt4 IM module and helper programs.

%package qt3
Summary:	Qt3 support for Uim
Group:		X11/Applications
Provides:	%{name}-qt-common = %{version}-%{release}

%description qt3
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the Qt3 IM module and helper programs.

%package kde
Summary:	KDE Applet for Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	uim-qt

%description kde
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the KDE applet.

%package -n emacs-uim
Summary:	Emacs support for Uim
Group:		Libraries
Requires:	emacs
Requires:	emacs-common-uim = %{version}-%{release}

%description -n emacs-uim
This package provides Emacs support.

%package -n emacs-common-uim
Summary:	Common package for Emacsen support for Uim
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n emacs-common-uim
This package provides an utility to use Emacsen support for Uim.

%package -n xemacs-uim
Summary:	XEmacs support for Uim
Group:		Libraries
Requires:	emacs-common-uim = %{version}-%{release}
Requires:	xemacs

%description -n xemacs-uim
This package provides XEmacs support.

%package anthy
Summary:	Anthy support for Uim
Group:		Libraries
Requires:	anthy >= 9100h
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{_bindir}/uim-module-manager
Requires(postun):	%{_bindir}/uim-module-manager

%description anthy
This package provides support for Anthy, a Japanese input method.

%package canna
Summary:	Canna support for Uim
Group:		Libraries
Requires:	Canna
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{_bindir}/uim-module-manager
Requires(postun):	%{_bindir}/uim-module-manager

%description canna
This package provides support for Canna, a Japanese input method.

%package mana
Summary:	Mana support for Uim
Group:		Libraries
Requires:	mana
Requires:	mana-uim
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{_bindir}/uim-module-manager
Requires(postun):	%{_bindir}/uim-module-manager

%description mana
This package provides support for mana, a Japanese input method.

%package prime
Summary:	PRIME support for Uim
Group:		Libraries
Requires:	prime
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{_bindir}/uim-module-manager
Requires(postun):	%{_bindir}/uim-module-manager

%description prime
This package provides support for PRIME, a Japanese input method.

%package skk
Summary:	SKK support for Uim
Group:		Libraries
Requires:	skkdic
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{_bindir}/uim-module-manager
Requires(postun):	%{_bindir}/uim-module-manager

%description skk
This package provides support for SKK, a Japanese input method.

%package m17n
Summary:	m17n-lib support for Uim
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{_bindir}/uim-module-manager
Requires(postun):	%{_bindir}/uim-module-manager

%description m17n
This package provides support for m17n-lib, which allows input of many
languages using the input table map from m17n-db.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cp -a fep/README fep/README.fep
cp -a fep/README.ja fep/README.fep.ja
cp -a fep/README.key fep/README.fep.key
cp -a xim/README xim/README.xim

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-openssl \
	--enable-gnome2-applet \
	--enable-gnome3-applet \
	--enable-qt4-qt3support \
	--enable-default-toolkit=gtk3 \
	--with-lispdir=%{_datadir}/emacs/site-lisp \
	--enable-dict \
	--enable-pref \
	--enable-notify=libnotify \
	--without-scim \
	--without-anthy \
	--with-anthy-utf8 \
	--with-canna \
	--with-m17nlib \
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
	--with-qt \
	--with-qt-immodule \
	--with-qt4 \
	--with-qt4-immodule \
	--enable-kde4-applet \
	--with-libedit \
	--with-eb

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d \
	$RPM_BUILD_ROOT%{_datadir}/{emacs/site-lisp,xemacs/site-packages/lisp}/site-start.d \
	$RPM_BUILD_ROOT%{_localstatedir}/lib/uim

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# For XEmacs
make install -C emacs \
	DESTDIR=$RPM_BUILD_ROOT \
	UIMEL_LISP_DIR=%{_datadir}/xemacs/site-packages/lisp/uim-el

%{__rm} $RPM_BUILD_ROOT%{_libdir}{,/gtk*/*/immodules,/uim/*}/*.la

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/uim.conf
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d/
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d/

mv $RPM_BUILD_ROOT%{_datadir}/uim/{installed-modules,loader}.scm $RPM_BUILD_ROOT%{_localstatedir}/lib/uim/
ln -sf %{_localstatedir}/lib/uim/installed-modules.scm $RPM_BUILD_ROOT%{_datadir}/uim/
ln -sf %{_localstatedir}/lib/uim/loader.scm $RPM_BUILD_ROOT%{_datadir}/uim/

# Register additional input methods
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
LIBUIM_SYSTEM_SCM_FILES=$RPM_BUILD_ROOT%{_datadir}/uim/lib \
LIBUIM_SCM_FILES=$RPM_BUILD_ROOT%{_datadir}/uim \
LIBUIM_PLUGIN_LIB_DIR=$RPM_BUILD_ROOT%{_libdir}/uim/plugin \
UIM_DISABLE_NOTIFY=1 \
$RPM_BUILD_ROOT%{_bindir}/uim-module-manager \
		--path $RPM_BUILD_ROOT%{_localstatedir}/lib/uim \
		--register tcode trycode hangul

# Unregister methods that come from separate packages
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
LIBUIM_SYSTEM_SCM_FILES=$RPM_BUILD_ROOT%{_datadir}/uim/lib \
LIBUIM_SCM_FILES=$RPM_BUILD_ROOT%{_datadir}/uim \
LIBUIM_PLUGIN_LIB_DIR=$RPM_BUILD_ROOT%{_libdir}/uim/plugin \
UIM_DISABLE_NOTIFY=1 \
$RPM_BUILD_ROOT%{_bindir}/uim-module-manager \
		--path $RPM_BUILD_ROOT%{_localstatedir}/lib/uim \
		--unregister anthy anthy-utf8 canna mana skk m17nlib

%find_lang %{name}
%find_lang %{name}-chardict-qt
%find_lang %{name}-chardict-qt4

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun gtk2
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun gtk3
%if "%{_lib}" != "lib"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%post anthy
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register anthy-utf8

%postun anthy
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister anthy-utf8
fi

%post canna
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register canna

%postun canna
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister canna
fi

%post prime
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register prime

%postun prime
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister prime
fi

%post mana
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register mana

%postun mana
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister mana
fi

%post skk
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register skk

%postun skk
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister skk
fi

%post m17n
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register m17nlib

%postun m17n
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister m17nlib
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%doc fep/README.fep fep/README.fep.ja fep/README.fep.key xim/README.xim
%{_sysconfdir}/X11/xinit/xinput.d/uim.conf
%attr(755,root,root) %{_bindir}/uim-fep
%attr(755,root,root) %{_bindir}/uim-fep-tick
%attr(755,root,root) %{_bindir}/uim-help
%attr(755,root,root) %{_bindir}/uim-module-manager
%attr(755,root,root) %{_bindir}/uim-sh
%attr(755,root,root) %{_bindir}/uim-xim
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.[0-9]
%attr(755,root,root) %{_libdir}/uim-helper-server
%dir %{_libdir}/uim
%dir %{_libdir}/uim/notify
%attr(755,root,root) %{_libdir}/uim/notify/libuimnotify*.so
%dir %{_libdir}/uim/plugin
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-curl.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-custom-enabler.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-eb.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-editline.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-expat.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-ffi.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-fileio.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-lolevel.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-look.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-openssl.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-process.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-socket.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-sqlite3.so
%dir %{_datadir}/uim
%{_datadir}/%{name}/*
%{_desktopdir}/uim.desktop
%{_mandir}/man1/*.1*
%dir %{_localstatedir}/lib/uim
%verify(not md5 mtime size) %{_localstatedir}/lib/uim/*.scm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-dict-gtk
%attr(755,root,root) %{_bindir}/uim-im-switcher-gtk
%attr(755,root,root) %{_bindir}/uim-input-pad-ja
%attr(755,root,root) %{_bindir}/uim-pref-gtk
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk-systray
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/*.so
%attr(755,root,root) %{_libdir}/uim-candwin-gtk
%attr(755,root,root) %{_libdir}/uim-candwin-tbl-gtk

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-dict-gtk3
%attr(755,root,root) %{_bindir}/uim-im-switcher-gtk3
%attr(755,root,root) %{_bindir}/uim-input-pad-ja-gtk3
%attr(755,root,root) %{_bindir}/uim-pref-gtk3
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk3
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk3-systray
%attr(755,root,root) %{_libdir}/gtk-3.0/*/immodules/*.so
%attr(755,root,root) %{_libdir}/uim-candwin-gtk3
%attr(755,root,root) %{_libdir}/uim-candwin-tbl-gtk3

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim-toolbar-applet-gnome3
%{_datadir}/dbus-1/services/org.gnome.panel.applet.UimAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/UimApplet.panel-applet

%files qt -f %{name}-chardict-qt4.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-chardict-qt4
%attr(755,root,root) %{_bindir}/uim-im-switcher-qt4
%attr(755,root,root) %{_bindir}/uim-pref-qt4
%attr(755,root,root) %{_bindir}/uim-toolbar-qt4
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/*.so
%attr(755,root,root) %{_libdir}/uim-candwin-qt4

%files qt3 -f %{name}-chardict-qt.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-chardict-qt
%attr(755,root,root) %{_bindir}/uim-im-switcher-qt
%attr(755,root,root) %{_bindir}/uim-pref-qt
%attr(755,root,root) %{_bindir}/uim-toolbar-qt
%attr(755,root,root) %{_libdir}/uim-candwin-qt

%files kde
%defattr(644,root,root,755)
%{_libdir}/kde4/plasma_applet_uim.so
%{_datadir}/kde4/services/plasma-applet-uim.desktop

%files -n emacs-uim
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/uim-el
%{_datadir}/emacs/site-lisp/site-start.d/uim-init.el

%files -n xemacs-uim
%defattr(644,root,root,755)
%{_datadir}/xemacs/site-packages/lisp/uim-el
%{_datadir}/xemacs/site-packages/lisp/site-start.d/uim-init.el

%files -n emacs-common-uim
%defattr(644,root,root,755)
%doc emacs/README
%lang(ja) %doc emacs/README.ja
%attr(755,root,root) %{_bindir}/uim-el-agent
%attr(755,root,root) %{_bindir}/uim-el-helper-agent

%files anthy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-anthy*.so
%{_datadir}/uim/anthy*.scm
%{_datadir}/uim/pixmaps/anthy*.png

%files canna
%defattr(644,root,root,755)
%{_datadir}/uim/canna*.scm
%{_datadir}/uim/pixmaps/canna.png

%files mana
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-mana.so
%{_datadir}/uim/mana*.scm
%{_datadir}/uim/pixmaps/mana.png

%files prime
%defattr(644,root,root,755)
%{_datadir}/uim/prime*.scm
%{_datadir}/uim/pixmaps/prime.png

%files skk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-skk.so
%{_datadir}/uim/skk*.scm
%{_datadir}/uim/pixmaps/skk*.png
%{_datadir}/uim/pixmaps/skk*.svg

%files m17n
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-m17nlib-relink-icons
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-m17nlib.so
%{_datadir}/uim/m17nlib.scm
%{_datadir}/uim/pixmaps/m17n*png
