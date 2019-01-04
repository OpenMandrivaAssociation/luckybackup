%define name luckybackup
%define version 0.5.0

Summary:	A powerful, fast and reliable backup & sync tool
Name:		%{name}
Version:	%{version}
Release:	1
License:	GPLv3
Url:		http://luckybackup.sourceforge.net/
Group:		Archiving/Backup
Source0:	http://prdownloads.sourceforge.net/sourceforge/luckybackup/luckybackup-%{version}.tar.gz
#Patch0:		remove_old_menu_file.patch
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:  qmake5
Requires:	rsync

%description
luckyBackup is an application that backs-up and/or synchronizes any 
directories with the power of rsync.

It is simple to use, fast (transfers over only changes made and not 
all data), safe (keeps your data safe by checking all declared directories 
before proceeding in any data manipulation ), reliable and fully customizable.

%prep
%setup -q
#patch0 -p1

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



%changelog
* Mon Mar 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.7-1
+ Revision: 785767
- version update 0.4.7

* Sun Jun 12 2011 Juan Luis Baptiste <juancho@mandriva.org> 0.4.6-1
+ Revision: 684374
- Updated to 0.4.6

* Wed Mar 09 2011 Juan Luis Baptiste <juancho@mandriva.org> 0.4.5-1
+ Revision: 643180
- Updated to 0.4.5

* Sun Oct 31 2010 Juan Luis Baptiste <juancho@mandriva.org> 0.4.4-1mdv2011.0
+ Revision: 591215
- Updated to 0.4.4.

* Mon Sep 06 2010 Juan Luis Baptiste <juancho@mandriva.org> 0.4.3-1mdv2011.0
+ Revision: 576376
- Updated to 0.4.3, forgot to update sources
- Updated to 0.4.3

* Tue Aug 31 2010 Juan Luis Baptiste <juancho@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 574561
- Updated to 0.4.2

* Tue Jul 13 2010 Juan Luis Baptiste <juancho@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 551875
- Forgot to add 0.4.1 sources.
- updated to 0.4.1
- Updated to 0.4.0.

* Sat Dec 19 2009 Jérôme Brenier <incubusss@mandriva.org> 0.3.5-1mdv2010.1
+ Revision: 480228
- new version 0.3.5

* Thu Sep 17 2009 Juan Luis Baptiste <juancho@mandriva.org> 0.3.3-1mdv2010.0
+ Revision: 443873
- Initial Mandriva package

