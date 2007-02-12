#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Sync
Summary:	File::Sync - Perl access to fsync() and sync() function calls
Summary(pl.UTF-8):   File::Sync - dostęp z Perla do funkcji fsync() i sync()
Name:		perl-File-Sync
Version:	0.09
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f5aca0ccff4bf28ca1d039e5ed01fa2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Sync module provides Perl access to fsync() and sync() function
calls.

%description -l pl.UTF-8
Moduł File::Sync umożliwia dostęp do funkcji fsync() i sync() z
poziomu Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/File/Sync.pm
%dir %{perl_vendorarch}/auto/File/Sync
%{perl_vendorarch}/auto/File/Sync/autosplit.ix
%{perl_vendorarch}/auto/File/Sync/Sync.bs
%attr(755,root,root) %{perl_vendorarch}/auto/File/Sync/Sync.so
%{_mandir}/man3/*
