Summary:	A utility for retrieving files using the NNTP
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles NNTP
Summary(pl):	Wsadowy klient NNTP
Name:		nget
Version:	0.18.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.azstarnet.com/~donut/programs/nget/%{name}-%{version}%+uulib.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc

%description
nget retrieves messages matching a regular expression, and decodes any
files contained within. Multipart messages are automatically pieced
together.

%description -l pl
nget odczytuje wiadomo¶ci z serwera NNTP pasuj±ce do wyra¿enia
regularnego i dekoduje wszystkie pasuj±ce pliki. S± tak¿e obs³ugiwane
wieloczê¶ciowe wiadomo¶ci.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
CXXFLAGS="%{rpmcflags}" export CXXFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf FAQ README TODO .ngetrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man?/*
