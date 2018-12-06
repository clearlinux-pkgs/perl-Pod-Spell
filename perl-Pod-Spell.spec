#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Spell
Version  : 1.20
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/Pod-Spell-1.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/Pod-Spell-1.20.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod-spell-perl/libpod-spell-perl_1.20-1.debian.tar.xz
Summary  : 'a formatter for spellchecking Pod'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Pod-Spell-bin = %{version}-%{release}
Requires: perl-Pod-Spell-license = %{version}-%{release}
Requires: perl-Pod-Spell-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Tiny)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Lingua::EN::Inflect)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Test::Deep)

%description
NAME
Pod::Spell - a formatter for spellchecking Pod
VERSION
version 1.20
SYNOPSIS

%package bin
Summary: bin components for the perl-Pod-Spell package.
Group: Binaries
Requires: perl-Pod-Spell-license = %{version}-%{release}
Requires: perl-Pod-Spell-man = %{version}-%{release}

%description bin
bin components for the perl-Pod-Spell package.


%package dev
Summary: dev components for the perl-Pod-Spell package.
Group: Development
Requires: perl-Pod-Spell-bin = %{version}-%{release}
Provides: perl-Pod-Spell-devel = %{version}-%{release}

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


%prep
%setup -q -n Pod-Spell-1.20
cd ..
%setup -q -T -D -n Pod-Spell-1.20 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Pod-Spell-1.20/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pod-Spell
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Pod-Spell/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Pod-Spell/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1Pod/Spell.pm
/usr/lib/perl5/vendor_perl/5.28.1Pod/Wordlist.pm
/usr/lib/perl5/vendor_perl/5.28.1auto/share/dist/Pod-Spell/wordlist

%files bin
%defattr(-,root,root,-)
/usr/bin/podspell

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Spell.3
/usr/share/man/man3/Pod::Wordlist.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pod-Spell/LICENSE
/usr/share/package-licenses/perl-Pod-Spell/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/podspell.1
