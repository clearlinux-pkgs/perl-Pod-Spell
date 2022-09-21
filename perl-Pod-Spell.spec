#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Spell
Version  : 1.23
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Pod-Spell-1.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Pod-Spell-1.23.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod-spell-perl/libpod-spell-perl_1.20-1.debian.tar.xz
Summary  : 'a formatter for spellchecking Pod'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Pod-Spell-bin = %{version}-%{release}
Requires: perl-Pod-Spell-license = %{version}-%{release}
Requires: perl-Pod-Spell-man = %{version}-%{release}
Requires: perl-Pod-Spell-perl = %{version}-%{release}
Requires: perl(Pod::Parser)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Tiny)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Lingua::EN::Inflect)
BuildRequires : perl(Pod::Parser)

%description
NAME
Pod::Spell - a formatter for spellchecking Pod
VERSION
version 1.23
SYNOPSIS
use Pod::Spell;
Pod::Spell->new->parse_from_file( 'File.pm' );

%package bin
Summary: bin components for the perl-Pod-Spell package.
Group: Binaries
Requires: perl-Pod-Spell-license = %{version}-%{release}

%description bin
bin components for the perl-Pod-Spell package.


%package dev
Summary: dev components for the perl-Pod-Spell package.
Group: Development
Requires: perl-Pod-Spell-bin = %{version}-%{release}
Provides: perl-Pod-Spell-devel = %{version}-%{release}
Requires: perl-Pod-Spell = %{version}-%{release}

%description dev
dev components for the perl-Pod-Spell package.


%package license
Summary: license components for the perl-Pod-Spell package.
Group: Default

%description license
license components for the perl-Pod-Spell package.


%package man
Summary: man components for the perl-Pod-Spell package.
Group: Default

%description man
man components for the perl-Pod-Spell package.


%package perl
Summary: perl components for the perl-Pod-Spell package.
Group: Default
Requires: perl-Pod-Spell = %{version}-%{release}

%description perl
perl components for the perl-Pod-Spell package.


%prep
%setup -q -n Pod-Spell-1.23
cd %{_builddir}
tar xf %{_sourcedir}/libpod-spell-perl_1.20-1.debian.tar.xz
cd %{_builddir}/Pod-Spell-1.23
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Pod-Spell-1.23/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pod-Spell
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Pod-Spell/a0df58490c0905c7174d6dd7e71a21cfab6d3947 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/podspell

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Spell.3
/usr/share/man/man3/Pod::Wordlist.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pod-Spell/a0df58490c0905c7174d6dd7e71a21cfab6d3947

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/podspell.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
