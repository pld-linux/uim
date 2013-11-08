#
# Conditional build:
%bcond_without	gnome	# GNOME panel applet
%bcond_without	kde	# KDE panel applet
%bcond_with	qt3	# Qt 3 support / immodule
%bcond_without	qt4	# Qt 4 support / immodule
%bcond_without	anthy	# Anthy IM and dictionary support
%bcond_without	canna	# Canna IM and dictionary support
%bcond_without	eb	# EB text search support
%bcond_without	m17n	# m17n IM support
%bcond_without	mana	# mana IM support
%bcond_with	scim	# scim support [broken acc. to configure]
%bcond_without	wnn	# Wnn IM support
#
Summary:	Multilingual input method library
Summary(pl.UTF-8):	Biblioteka obsługująca wejście w wielu językach
Name:		uim
Version:	1.8.6
Release:	1
License:	GPL or BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/uim/downloads/list
Source0:	http://uim.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ecea4c597bab1fd4ba98ea84edcece59
Source1:	%{name}.xinputd
Source2:	%{name}-init.el
Patch0:		%{name}-emacs-utf8.patch
URL:		http://uim.freedesktop.org/
%{?with_canna:BuildRequires:	Canna-devel}
%{?with_wnn:BuildRequires:	FreeWnn-devel}
%{?with_qt4:BuildRequires:	Qt3Support-devel >= 4}
%{?with_anthy:BuildRequires:	anthy-devel >= 9100h-2}
#BuildRequires:	autoconf >= 2.60b
#BuildRequires:	automake >= 1:1.10
%{?with_kde:BuildRequires:	automoc4}
%{?with_kde:BuildRequires:	cmake}
BuildRequires:	curl-devel >= 7.16.4
%{?with_eb:BuildRequires:	eb-devel}
BuildRequires:	expat-devel >= 1.95
BuildRequires:	gettext-devel >= 0.17
%{?with_gnome:BuildRequires:	gnome-panel-devel >= 3}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.36.3
%{?with_kde:BuildRequires:	kde4-kdelibs-devel}
BuildRequires:	libedit-devel
BuildRequires:	libffi-devel >= 3.0.0
BuildRequires:	libgcroots-devel >= 0.2.3
%{?with_gnome:BuildRequires:	libgnome-devel >= 2.4.0}
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:	libstdc++-devel
#BuildRequires:	libtool >= 2:1.5
%{?with_m17n:BuildRequires:	m17n-lib-devel >= 1.3.1}
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libffi) >= 3.0.0
%{?with_qt3:BuildRequires:	qt-devel >= 3.2.0}
%{?with_qt4:BuildRequires:	qt4-qmake >= 4}
%{?with_scim:BuildRequires:	scim-devel >= 1.3.0}
BuildRequires:	sqlite3-devel >= 3.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
Requires:	libgcroots >= 0.2.3
# for libuim-curl
Requires:	curl-libs >= 7.16.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages. Currently, it can input to
applications which support GTK+'s immodule, Qt's immodule and XIM.

This package provides the input method library, the XIM bridge and
most of the input methods.

For the Japanese input methods you need to install
- uim-anthy for Anthy
- uim-canna for Canna
- uim-skk for SKK.

%description -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków. Obecnie potrafi obsłużyć
aplikacje obsługujące moduły IM z GTK+, moduły IM z Qt oraz XIM.

Ten pakiet udostępnia bibliotekę metody wprowadzania, mostek XIM oraz
większość metod wprowadzania.

Do wprowadzania tekstu japońskiego trzeba zainstalować:
- uim-anthy dla metody Anthy
- uim-canna dla metody Canna
- uim-skk dla SKK.

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
Summary:	GTK+ 2 support for Uim
Summary(pl.UTF-8):	Obsługa GTK+ 2 dla biblioteki Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
# for update-gtk-immodules
Requires(post,postun):	gtk+2 >= 2:2.9.1-2
Requires:	gtk+2 >= 2:2.4.0

%description gtk2
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the GTK+ 2 IM module and helper program.

%description gtk2 -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków.

Ten pakiet zawiera moduł IM GTK+ 2 oraz program pomocniczy.

%package gtk3
Summary:	GTK+ 3 support for Uim
Summary(pl.UTF-8):	Obsługa GTK+ 3 dla biblioteki Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
# for update-gtk-immodules
Requires(post,postun):	gtk+3

%description gtk3
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the GTK+ 3 IM module and helper program.

%description gtk3 -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków.

Ten pakiet zawiera moduł IM GTK+ 3 oraz program pomocniczy.

%package gnome
Summary:	GNOME 3 Applet for Uim
Summary(pl.UTF-8):	Aplet GNOME 3 dla biblioteki Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gtk3 = %{version}-%{release}

%description gnome
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the GNOME 3 panel applet.

%description gnome -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków.

Ten pakiet zawiera aplet panelu GNOME 3.

%package qt3
Summary:	Qt 3 support for Uim
Summary(pl.UTF-8):	Obsługa Qt 3 dla biblioteki Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-qt-common = %{version}-%{release}

%description qt3
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the Qt 3 IM module and helper programs.

%description qt3 -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków.

Ten pakiet zawiera moduł IM Qt 3 oraz programy pomocnicze.

%package qt
Summary:	Qt 4 support for Uim
Summary(pl.UTF-8):	Obsługa Qt 4 dla biblioteki Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	qt >= 6:3.2.0

%description qt
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the Qt 4 IM module and helper programs.

%description qt -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków.

Ten pakiet zawiera moduł IM Qt 4 oraz programy pomocnicze.

%package kde
Summary:	KDE 4 Applet for Uim
Summary(pl.UTF-8):	Aplet KDE 4 dla biblioteki Uim
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}

%description kde
Uim is a multilingual input method library. Uim aims to provide secure
and useful input methods for all languages.

This package provides the KDE 4 applet.

%description kde -l pl.UTF-8
Uim jest biblioteką obsługującą wejście w wielu językach. Celem
projektu jest udostępnienie bezpiecznych i użytecznych metod
wprowadzania dla wszystkich języków.

Ten pakiet zawiera aplet KDE 4.

%package -n emacs-common-uim
Summary:	Common package for Emacsen support for Uim
Summary(pl.UTF-8):	Pakiet wspólny Uima dla emacsów
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n emacs-common-uim
This package provides an utility to use Emacsen support for Uim.

%description -n emacs-common-uim -l pl.UTF-8
Ten pakiet zawiera narzędzia pozwalające na używanie Uima w emacsach.

%package -n emacs-uim
Summary:	Emacs support for Uim
Summary(pl.UTF-8):	Obsługa Uima w Emacsie
Group:		Libraries
Requires:	emacs
Requires:	emacs-common-uim = %{version}-%{release}

%description -n emacs-uim
This package provides Emacs support for Uim.

%description -n emacs-uim
Ten pakiet zapewnia obsługę Uima w Emacsie.

%package -n xemacs-uim
Summary:	XEmacs support for Uim
Summary(pl.UTF-8):	Obsługa Uima w XEmacsie
Group:		Libraries
Requires:	emacs-common-uim = %{version}-%{release}
Requires:	xemacs

%description -n xemacs-uim
This package provides XEmacs support.

%description -n xemacs-uim -l pl.UTF-8
Ten pakiet zapewnia obsługę Uima w XEmacsie.

%package anthy
Summary:	Anthy support for Uim
Summary(pl.UTF-8):	Obsługa metody Anthy w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	anthy >= 9100h

%description anthy
This package provides support for Anthy, a Japanese input method.

%description anthy -l pl.UTF-8
Ten pakiet zawiera obsługę metody Anthy wprowadzania znaków
japońskich.

%package canna
Summary:	Canna support for Uim
Summary(pl.UTF-8):	Obsługa metody Canna w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	Canna

%description canna
This package provides support for Canna, a Japanese input method.

%description canna -l pl.UTF-8
Ten pakiet zawiera obsługę metody Canna wprowadzania znaków
japońskich.

%package eb
Summary:	EB search support for Uim
Summary(pl.UTF-8):	Obsługa wyszukiwania EB w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}

%description eb
This package provides support for searching text in books in EB
format.

%description eb -l pl.UTF-8
Ten pakiet zawiera obsługę wyszukiwania tekstu w książkach w formacie
EB.

%package m17n
Summary:	m17n-lib support for Uim
Summary(pl.UTF-8):	Obsługa m17n-lib w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	m17n-lib >= 1.3.1

%description m17n
This package provides support for m17n-lib, which allows input of many
languages using the input table map from m17n-db.

%description m17n -l pl.UTF-8
Ten pakiet zawiera obsługę m17n-lib, co pozwala na wprowadzanie znaków
wielu języków przy użyciu tablic wejściowych z m17n-db.

%package mana
Summary:	Mana support for Uim
Summary(pl.UTF-8):	Obsługa metody Mana w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	mana
Requires:	mana-uim

%description mana
This package provides support for mana, a Japanese input method.

%description mana -l pl.UTF-8
Ten pakiet zawiera obsługę metody Mana wprowadzania znaków
japońskich.

%package prime
Summary:	PRIME support for Uim
Summary(pl.UTF-8):	Obsługa metody PRIME w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	prime >= 0.8.5.2

%description prime
This package provides support for PRIME, a Japanese input method.

%description prime -l pl.UTF-8
Ten pakiet zawiera obsługę metody PRIME wprowadzania znaków
japońskich.

%package scim
Summary:	SCIM support for Uim
Summary(pl.UTF-8):	Obsługa metod SCIM w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	scim >= 1.3.0

%description scim
This package provides support for SCIM-provided input methods.

%description scim -l pl.UTF-8
Ten pakiet zawiera obsługę metod udostępnianych przez SCIM.

%package sj3
Summary:	SJ3 support for Uim
Summary(pl.UTF-8):	Obsługa metody SJ3 w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}

%description sj3
This package provides support for SJ3, a Japanese input method.

%description sj3 -l pl.UTF-8
Ten pakiet zawiera obsługę metody SJ3 wprowadzania znaków
japońskich.

%package skk
Summary:	SKK support for Uim
Summary(pl.UTF-8):	Obsługa metody SKK w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}
Requires:	skkdic

%description skk
This package provides support for SKK, a Japanese input method.

%description skk -l pl.UTF-8
Ten pakiet zawiera obsługę metody SKK wprowadzania znaków
japońskich.

%package wnn
Summary:	Wnn support for Uim
Summary(pl.UTF-8):	Obsługa metody Wnn w Uimie
Group:		Libraries
Requires(post,postun):	%{_bindir}/uim-module-manager
Requires:	%{name} = %{version}-%{release}

%description wnn
This package provides support for Wnn, a Japanese input method.

%description wnn -l pl.UTF-8
Ten pakiet zawiera obsługę metody Wnn wprowadzania znaków
japońskich.

%prep
%setup -q
%patch0 -p1

cp -a fep/README fep/README.fep
cp -a fep/README.ja fep/README.fep.ja
cp -a fep/README.key fep/README.fep.key
cp -a xim/README xim/README.xim

%build
%configure \
	MANA=/usr/bin/mana \
	--enable-default-toolkit=gtk3 \
	--enable-dict \
	--disable-gnome2-applet \
	%{?with_gnome:--enable-gnome3-applet} \
	%{?with_kde:--enable-kde4-applet} \
	--enable-notify=libnotify \
	--enable-openssl \
	--enable-pref \
	%{?with_qt4:--enable-qt4-qt3support} \
	--without-anthy \
	%{?with_anthy:--with-anthy-utf8} \
	%{?with_canna:--with-canna} \
	--with-curl \
	%{?with_eb:--with-eb} \
	--with-expat \
	--with-ffi \
	--with-gtk2 \
	--with-gtk3 \
	--with-libedit \
	--with-libgcroots=installed \
	--with-lispdir=%{_datadir}/emacs/site-lisp \
	%{!?with_m17n:--without-m17nlib} \
	%{?with_mana:--with-mana} \
	--with-prime \
	%{?with_qt3:--with-qt --with-qt-immodule} \
	%{?with_qt4:--with-qt4 --with-qt4-immodule} \
	%{?with_scim:--with-scim} \
	--with-sj3 \
	--with-skk \
	--with-sqlite3 \
	--with-ssl-engine \
	%{?with_wnn:--with-wnn --with-wnn-includes=/usr/include/wnn} \
	--with-x \
	--with-xft

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d \
	$RPM_BUILD_ROOT%{_datadir}/{emacs/site-lisp,xemacs-packages/lisp}/site-start.d \
	$RPM_BUILD_ROOT%{_localstatedir}/lib/uim

%{__make} -j1 install \
	QT_PLUGINSDIR=%{_libdir}/qt/plugins-mt \
	DESTDIR=$RPM_BUILD_ROOT

# For XEmacs
%{__make} -j1 install -C emacs \
	DESTDIR=$RPM_BUILD_ROOT \
	UIMEL_LISP_DIR=%{_datadir}/xemacs-packages/lisp/uim-el

%{__rm} $RPM_BUILD_ROOT%{_libdir}{,/gtk*/*/immodules,/uim/*%{?with_qt:,/qt/plugins-mt/*}}/*.la

%{__sed} -e 's|@@LIB@@|%{_lib}|g' %{SOURCE1} >$RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/uim.conf
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d/
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/

mv $RPM_BUILD_ROOT%{_datadir}/uim/{installed-modules,loader}.scm $RPM_BUILD_ROOT%{_localstatedir}/lib/uim/
ln -sf %{_localstatedir}/lib/uim/installed-modules.scm $RPM_BUILD_ROOT%{_datadir}/uim/
ln -sf %{_localstatedir}/lib/uim/loader.scm $RPM_BUILD_ROOT%{_datadir}/uim/

# OSX-specific
%{__rm} $RPM_BUILD_ROOT%{_datadir}/uim/annotation-osx-dcs.scm

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
		--unregister anthy-utf8 canna m17nlib mana prime scim sj3 skk wnn

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post gtk2
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%postun gtk2
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-2.0-64 > %{_sysconfdir}/gtk64-2.0/gtk.immodules
%else
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%endif

%post gtk3
%if "%{_lib}" == "lib64"
%{_bindir}/gtk-query-immodules-3.0-64 --update-cache
%else
%{_bindir}/gtk-query-immodules-3.0 --update-cache
%endif

%postun gtk3
%if "%{_lib}" == "lib64"
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

%post m17n
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register m17nlib

%postun m17n
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister m17nlib
fi

%post mana
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register mana

%postun mana
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister mana
fi

%post prime
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register prime

%postun prime
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister prime
fi

%post scim
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register scim

%postun scim
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister scim
fi

%post sj3
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register sj3

%postun sj3
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister sj3
fi

%post skk
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register skk

%postun skk
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister skk
fi

%post wnn
%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --register wnn

%postun wnn
if [ "$1" = "0" ]; then
	%{_bindir}/uim-module-manager --path %{_localstatedir}/lib/uim --unregister wnn
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
%attr(755,root,root) %{_libdir}/libuim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuim.so.8
%attr(755,root,root) %{_libdir}/libuim-custom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuim-custom.so.2
%attr(755,root,root) %{_libdir}/libuim-scm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuim-scm.so.0
%attr(755,root,root) %{_libdir}/uim-helper-server
%dir %{_libdir}/uim
%dir %{_libdir}/uim/notify
%attr(755,root,root) %{_libdir}/uim/notify/libuimnotify-libnotify.so
%dir %{_libdir}/uim/plugin
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-curl.so
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-custom-enabler.so
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
%{_datadir}/uim/byeoru-data
%{_datadir}/uim/helperdata
%{_datadir}/uim/lib
%{_datadir}/uim/pixmaps
%{_datadir}/uim/tables
%{_datadir}/uim/*.scm
# NOTE: scm and pixmaps files are always installed, even if particular part is disabled by bcond
# by using unconditional exclude we avoid packaging them if bcond is disabled
%exclude %{_datadir}/uim/pixmaps/anthy*.png
%exclude %{_datadir}/uim/pixmaps/canna.png
%exclude %{_datadir}/uim/pixmaps/m17n*png
%exclude %{_datadir}/uim/pixmaps/mana.png
%exclude %{_datadir}/uim/pixmaps/mana.svg
%exclude %{_datadir}/uim/pixmaps/prime*.png
%exclude %{_datadir}/uim/pixmaps/scim.png
%exclude %{_datadir}/uim/pixmaps/scim.svg
%exclude %{_datadir}/uim/pixmaps/sj3.png
%exclude %{_datadir}/uim/pixmaps/sj3.svg
%exclude %{_datadir}/uim/pixmaps/skk*.png
%exclude %{_datadir}/uim/pixmaps/skk*.svg
%exclude %{_datadir}/uim/pixmaps/wnn.png
%exclude %{_datadir}/uim/pixmaps/wnn.svg
%exclude %{_datadir}/uim/annotation-eb.scm
%exclude %{_datadir}/uim/anthy*.scm
%exclude %{_datadir}/uim/canna*.scm
%exclude %{_datadir}/uim/m17nlib*.scm
%exclude %{_datadir}/uim/mana*.scm
%exclude %{_datadir}/uim/prime*.scm
%exclude %{_datadir}/uim/scim.scm
%exclude %{_datadir}/uim/sj3*.scm
%exclude %{_datadir}/uim/skk*.scm
%exclude %{_datadir}/uim/wnn*.scm
%{_desktopdir}/uim.desktop
%{_mandir}/man1/uim-xim.1*
%dir %{_localstatedir}/lib/uim
%verify(not md5 mtime size) %{_localstatedir}/lib/uim/installed-modules.scm
%verify(not md5 mtime size) %{_localstatedir}/lib/uim/loader.scm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuim.so
%attr(755,root,root) %{_libdir}/libuim-custom.so
%attr(755,root,root) %{_libdir}/libuim-scm.so
%{_includedir}/%{name}
%{_pkgconfigdir}/uim.pc

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-dict-gtk
%attr(755,root,root) %{_bindir}/uim-im-switcher-gtk
%attr(755,root,root) %{_bindir}/uim-input-pad-ja
%attr(755,root,root) %{_bindir}/uim-pref-gtk
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk-systray
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/im-uim.so
%attr(755,root,root) %{_libdir}/uim-candwin-gtk
%attr(755,root,root) %{_libdir}/uim-candwin-tbl-gtk
%attr(755,root,root) %{_libdir}/uim-candwin-horizontal-gtk

%files gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-dict-gtk3
%attr(755,root,root) %{_bindir}/uim-im-switcher-gtk3
%attr(755,root,root) %{_bindir}/uim-input-pad-ja-gtk3
%attr(755,root,root) %{_bindir}/uim-pref-gtk3
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk3
%attr(755,root,root) %{_bindir}/uim-toolbar-gtk3-systray
%attr(755,root,root) %{_libdir}/gtk-3.0/*/immodules/im-uim.so
%attr(755,root,root) %{_libdir}/uim-candwin-gtk3
%attr(755,root,root) %{_libdir}/uim-candwin-tbl-gtk3
%attr(755,root,root) %{_libdir}/uim-candwin-horizontal-gtk3

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim-toolbar-applet-gnome3
%{_datadir}/dbus-1/services/org.gnome.panel.applet.UimAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/UimApplet.panel-applet
%endif

%if %{with qt3}
%files qt3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-chardict-qt
%attr(755,root,root) %{_bindir}/uim-im-switcher-qt
%attr(755,root,root) %{_bindir}/uim-pref-qt
%attr(755,root,root) %{_bindir}/uim-toolbar-qt
%attr(755,root,root) %{_libdir}/uim-candwin-qt
%attr(755,root,root) %{_libdir}/qt/plugins-mt/inputmethods/libquiminputcontextplugin.so
%endif

%if %{with qt4}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-chardict-qt4
%attr(755,root,root) %{_bindir}/uim-im-switcher-qt4
%attr(755,root,root) %{_bindir}/uim-pref-qt4
%attr(755,root,root) %{_bindir}/uim-toolbar-qt4
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/libuiminputcontextplugin.so
%attr(755,root,root) %{_libdir}/uim-candwin-qt4
%endif

%if %{with kde}
%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_uim.so
%{_datadir}/kde4/services/plasma-applet-uim.desktop
%endif

%files -n emacs-common-uim
%defattr(644,root,root,755)
%doc emacs/README
%lang(ja) %doc emacs/README.ja
%attr(755,root,root) %{_bindir}/uim-el-agent
%attr(755,root,root) %{_bindir}/uim-el-helper-agent

%files -n emacs-uim
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/uim-el
%{_datadir}/emacs/site-lisp/site-start.d/uim-init.el

%files -n xemacs-uim
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/uim-el
%{_datadir}/xemacs-packages/lisp/uim-init.el

%if %{with anthy}
%files anthy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-anthy-utf8.so
%{_datadir}/uim/anthy*.scm
%{_datadir}/uim/pixmaps/anthy*.png
%endif

%if %{with canna}
%files canna
%defattr(644,root,root,755)
%{_datadir}/uim/canna*.scm
%{_datadir}/uim/pixmaps/canna.png
%endif

%if %{with eb}
%files eb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-eb.so
%{_datadir}/uim/annotation-eb.scm
%endif

%if %{with m17n}
%files m17n
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uim-m17nlib-relink-icons
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-m17nlib.so
%{_datadir}/uim/m17nlib*.scm
%{_datadir}/uim/pixmaps/m17n*.png
%endif

%if %{with mana}
%files mana
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-mana.so
%{_datadir}/uim/mana*.scm
%{_datadir}/uim/pixmaps/mana.png
%{_datadir}/uim/pixmaps/mana.svg
%endif

%files prime
%defattr(644,root,root,755)
%{_datadir}/uim/prime*.scm
%{_datadir}/uim/pixmaps/prime*.png

%if %{with scim}
%files scim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-scim.so
%{_datadir}/uim/scim.scm
%{_datadir}/uim/pixmaps/scim.png
%{_datadir}/uim/pixmaps/scim.svg
%endif

%files sj3
%defattr(644,root,root,755)
%{_datadir}/uim/sj3*.scm
%{_datadir}/uim/pixmaps/sj3.png
%{_datadir}/uim/pixmaps/sj3.svg

%files skk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-skk.so
%{_datadir}/uim/skk*.scm
%{_datadir}/uim/pixmaps/skk.png
%{_datadir}/uim/pixmaps/skk.svg

%if %{with wnn}
%files wnn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/uim/plugin/libuim-wnn.so
%{_datadir}/uim/wnn*.scm
%{_datadir}/uim/pixmaps/wnn.png
%{_datadir}/uim/pixmaps/wnn.svg
%endif
