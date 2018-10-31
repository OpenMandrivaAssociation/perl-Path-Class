%define	module	Path-Class
%define upstream_version 0.37

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Cross-platform path specification manipulation
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/%{module}-%{upstream_version}.tar.gz
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
%setup -q -n %{module}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Path/Class/*
%{perl_vendorlib}/Path/Class.pm
%{perl_vendorlib}/Path/README.pod
%{_mandir}/*/*

