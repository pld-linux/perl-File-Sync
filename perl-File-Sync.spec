%include	/usr/lib/rpm/macros.perl
Summary:	File-Sync perl module
Summary(pl):	Modu³ perla File-Sync
Name:		perl-File-Sync
Version:	0.09
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Sync-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Sync - Perl access to fsync() and sync() function calls.

%description -l pl
File-Sync - umo¿liwia dostêp do funkcji fsync() i sync().

%prep
%setup -q -n File-Sync-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/File/Sync.pm
%dir %{perl_sitearch}/auto/File/Sync
%{perl_sitearch}/auto/File/Sync/autosplit.ix
%{perl_sitearch}/auto/File/Sync/Sync.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/Sync/Sync.so
%{_mandir}/man3/*
