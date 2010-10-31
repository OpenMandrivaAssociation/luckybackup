%define name luckybackup
%define version 0.4.4

Summary:	A powerful, fast and reliable backup & sync tool
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPLv3
Url:		http://luckybackup.sourceforge.net/
Group:		Archiving/Backup
Source:		http://prdownloads.sourceforge.net/sourceforge/luckybackup/luckybackup-%{version}.tar.gz
Patch0:		remove_old_menu_file.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
Requires:	rsync

%description
luckyBackup is an application that backs-up and/or synchronizes any 
directories with the power of rsync.

It is simple to use, fast (transfers over only changes made and not 
all data), safe (keeps your data safe by checking all declared directories 
before proceeding in any data manipulation ), reliable and fully customizable.

%prep
%setup -q
%patch0 -p1

%build
qmake

%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=$RPM_BUILD_ROOT install

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif
 
%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}/translations/*
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man8/*
%{_defaultdocdir}/%{name}/*

