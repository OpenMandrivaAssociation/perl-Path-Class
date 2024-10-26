%define	module	Path-Class

Name:		perl-%{module}
Version:	0.37
Release:	1

Summary:	Cross-platform path specification manipulation
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/pod/Path::Class
Source0:	https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Perl::OSType)
BuildRequires:	perl(File::Spec::Win32)
BuildArch:	noarch

%description
Path::Class is a module for manipulation of file and directory specifications
(strings describing their locations, like '/home/ken/foo.txt' or
'C:\Windows\Foo.txt') in a cross-platform manner. It supports pretty much every
platform Perl runs on, including Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2,
and NetWare.

%prep
%autosetup -p1 -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/Path/Class/*
%{perl_vendorlib}/Path/Class.pm
%doc %{_mandir}/*/*
