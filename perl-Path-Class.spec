%define	module	Path-Class
%define upstream_version 0.24

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Cross-platform path specification manipulation
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Path/%{module}-%{upstream_version}.tar.gz

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
%{_mandir}/*/*
