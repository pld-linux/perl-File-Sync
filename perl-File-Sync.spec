Summary:	File-Sync perl module
Summary(pl):	Modu³ perla File-Sync
Name:		perl-File-Sync
Version:	0.06
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Sync-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
File-Sync - Perl access to fsync() and sync() function calls.

%description -l pl
File-Sync - umo¿liwia dostêp do funkcji fsync() i sync().

%prep
%setup -q -n File-Sync-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/File/Sync/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/Sync
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/File/Sync.pm

%dir %{perl_sitearch}/auto/File/Sync
%{perl_sitearch}/auto/File/Sync/.packlist
%{perl_sitearch}/auto/File/Sync/autosplit.ix
%{perl_sitearch}/auto/File/Sync/Sync.bs
%attr(755,root,root) %{perl_sitearch}/auto/File/Sync/Sync.so

%{_mandir}/man3/*
