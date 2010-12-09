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
