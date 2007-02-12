Summary:	A utility for retrieving files using the NNTP
Summary(fr.UTF-8):   Un utilitaire pour recuperer des fichiers en utilisant les protocoles NNTP
Summary(pl.UTF-8):   Wsadowy klient NNTP
Name:		nget
Version:	0.27.1
Release:	1
License:	GPL
Group:		Networking/Utilities
#Source0Download:	http://www.dakotacom.net/~donut/programs/nget.html
Source0:	http://www.dakotacom.net/~donut/programs/nget/%{name}-%{version}.tar.gz
# Source0-md5:	0710a25aebede4799bd9ca3756573f6a
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.dakotacom.net/~donut/programs/nget.html
BuildRequires:	libstdc++-devel
BuildRequires:	popt-devel
BuildRequires:	uudeview-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nget retrieves messages matching a regular expression, and decodes any
files contained within. Multipart messages are automatically pieced
together.

%description -l pl.UTF-8
nget odczytuje wiadomości z serwera NNTP pasujące do wyrażenia
regularnego i dekoduje wszystkie pasujące pliki. Są także obsługiwane
wieloczęściowe wiadomości.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog FAQ README TODO .ngetrc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
