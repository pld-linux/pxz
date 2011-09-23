%define		snap	20100608
Summary:	Parallel LZMA compressor using XZ
Summary(pl.UTF-8):	Wielowątkowy kompresor LZMA wykorzystujący XZ
Name:		pxz
Version:	4.999.9
Release:	0.%{snap}.2
License:	GPL v2
Group:		Applications/File
#Source0:	http://jnovy.fedorapeople.org/pxz/%{name}-%{version}beta.%{snap}git.tar.xz
Source0:	%{name}-%{version}beta.%{snap}git.tar.xz
# Source0-md5:	734645e5f147678fe77e66db2a579360
URL:		http://jnovy.fedorapeople.org/pxz/
BuildRequires:	gcc >= 6:4.2
BuildRequires:	libgomp-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parallel XZ is a compression utility that takes advantage of running
XZ compression simultaneously on different parts of an input file on
multiple cores and processors. This significantly speeds up
compression time.

%description -l pl.UTF-8
Parallel XZ to program kompresujący wykorzystujący możliwość
wykonywania kompresji XZ jednocześnie na różnych częściach pliku
wejściowego przy użyciu wielu rdzeni i procesorów. Znacząco
przyspiesza to czas kompresji.

%prep
%setup -q -n %{name}-%{version}beta

%build
%{__make} \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -fopenmp" \
	LDFLAGS="%{rpmldflags} -llzma"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pxz
%{_mandir}/man1/pxz.1*
