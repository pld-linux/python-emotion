# NOTE: for EFL >= 1.8.0 version see python-efl.spec
Summary:	Python bindings for Emotion library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Emotion
Name:		python-emotion
Version:	1.7.0
Release:	6
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	ac7197ce2617a87fad3dd134a98ad01f
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	emotion-devel >= 1.7.0
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	python-Cython >= 0.15.1
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-evas >= 1.7.0
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	emotion >= 1.7.0
Requires:	evas >= 1.7.0
Requires:	python-evas >= 1.7.0
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
Requires:	emotion-devel >= 1.7.0
Requires:	evas-devel >= 1.7.0
Requires:	python-evas-devel >= 1.7.0

%description devel
Python bindings for Emotion library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Emotion - pliki programistyczne.

%prep
%setup -q

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
%{py_sitedir}/emotion/__init__.py[co]
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/python-emotion.pc
