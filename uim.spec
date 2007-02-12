Summary:	Multilingual input method library
Summary(pl.UTF-8):   Biblioteka obsługująca wejście w wielu językach
Name:		uim
Version:	0.3.2
Release:	2
License:	GPL or BSD
Group:		Libraries
Source0:	http://uim.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	fe363216c0b6ef90eeb7352721bd9fcc
Patch0:		%{name}-dont_run_gtk_query_immodules.patch
Patch1:		%{name}-immodules_dir.patch
URL:		http://uim.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libgnome-devel >= 2.4.0
BuildRequires:	libtool
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
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki uim
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for uim library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki uim.

%package static
Summary:	Static uim library
Summary(pl.UTF-8):   Statyczna biblioteka uim
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static uim library.

%description static -l pl.UTF-8
Statyczna biblioteka uim.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules

%postun
umask 022
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/uim-helper-applet
%attr(755,root,root) %{_libdir}/gtk*/*/immodules/*.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc doc/LIB
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
