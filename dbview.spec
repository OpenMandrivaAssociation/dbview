%define name dbview
%define version 1.0.4
%define release %mkrel 5

Summary: Dbview - view dBase files
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Patch: %name-patch.bz2
License: GPL
Group: Databases
BuildRoot: %_tmppath/%{name}-buildroot

%description
Dbview is a little tool that will display dBase III and IV files. 
You can also use it to convert your old .dbf files for further use with Unix.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
make "CFLAGS=$RPM_OPT_FLAGS -pipe"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 dbview $RPM_BUILD_ROOT%{_bindir}
install -m 644 dbview.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README dBASE
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5mdv2011.0
+ Revision: 617520
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4-4mdv2010.0
+ Revision: 427638
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2009.0
+ Revision: 240586
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 53080
- New release 1.0.4
- Import dbview



* Thu Oct 06 2005 Lenny Cartier <lenny@mandriva.com> 1.0.3-2mdk
- rebuild

* Tue Jul 27 2004 Jerome Soyer <jeromesoyer@yahoo.fr> 1.0.3-1mdk
- 1.0.3
- rebuild and repatch

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-8mdk
- rebuild

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-7mdk
- rebuild

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-6mdk
- rebuild

* Mon Jul 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-5mdk
- rebuild

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-4mdk
- rebuild

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.0-3mdk
- BM

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-2mdk
- fix group
- spec helper fixes

* Wed Feb 09 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-1mdk
- mandrake build

* Wed May 12 1999 Peter Soos <sp@osb.hu>
Corrected the file and directory attributes to rebuild the package
under RedHat Linux 6.0
 
* Fri Dec 25 1998 Peter Soos <sp@osb.hu>
Corrected the file and directory attributes
 
* Mon Jun 22 1998 Peter Soos <sp@osb.hu>
Using %%attr
 
* Fri Dec 6 1997 Peter Soos <sp@osb.hu>
Recompiled under RedHat Linux 5.0   
