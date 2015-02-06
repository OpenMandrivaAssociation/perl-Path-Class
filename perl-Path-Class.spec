%define	module	Path-Class
%define upstream_version 0.26

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Cross-platform path specification manipulation
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Path/%{module}-%{upstream_version}.tar.gz
BuildRequires: perl-devel

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
%{perl_vendorlib}/Path/f.pl
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.240.0-1
+ Revision: 768283
- cleanups
- new version

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 572224
- update to 0.21

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 552535
- update to 0.19

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 480734
- update to 0.18

* Mon Nov 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 469242
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 389936
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.16-3mdv2009.0
+ Revision: 241813
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.16-1mdv2008.0
+ Revision: 25189
- 0.16


* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- 0.15

* Fri Sep 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.13-1mdk
- 0.13

* Wed Jun 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- 0.12

* Wed Jun 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.11-1mdk
- 0.11

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- First Mandriva release

