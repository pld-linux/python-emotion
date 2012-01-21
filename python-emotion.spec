Summary:	Python bindings for Emotion library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Emotion
Name:		python-emotion
Version:	0.7.3
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	9e4a63a5b6314c81225addd68e26bb69
Patch0:		%{name}-cython.patch
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	emotion-devel >= 0.2.0.52190
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-evas >= 0.7.3
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	emotion >= 0.2.0.52190
Requires:	evas >= 1.0.0
Requires:	python-evas >= 0.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Emotion library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Emotion.

%package devel
Summary:	Python bindings for Emotion library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Emotion - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	emotion-devel >= 0.2.0.52190
Requires:	evas-devel >= 1.0.0
Requires:	python-evas-devel >= 0.7.3

%description devel
Python bindings for Emotion library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Emotion - pliki programistyczne.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/emotion/c_emotion.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitedir}/emotion
%attr(755,root,root) %{py_sitedir}/emotion/c_emotion.so
%{py_sitescriptdir}/emotion
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/python-emotion.pc
