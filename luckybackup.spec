%define name luckybackup
%define version 0.4.7

Summary:	A powerful, fast and reliable backup & sync tool
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPLv3
Url:		http://luckybackup.sourceforge.net/
Group:		Archiving/Backup
Source0:	http://prdownloads.sourceforge.net/sourceforge/luckybackup/luckybackup-%{version}.tar.gz
Patch0:		remove_old_menu_file.patch
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
%makeinstall INSTALL_ROOT=%{buildroot} install

%files
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}/translations/*
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man8/*
%{_defaultdocdir}/%{name}/*

