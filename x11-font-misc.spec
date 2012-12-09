Name: x11-font-misc
Version: 1.0.0
Release: %mkrel 12
Summary: X11 misc fonts
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildArch: noarch
Requires: x11-font-arabic-misc
Requires: x11-font-cursor-misc
Requires: x11-font-daewoo-misc
Requires: x11-font-dec-misc
Requires: x11-font-isas-misc
Requires: x11-font-jis-misc
Requires: x11-font-micro-misc
Requires: x11-font-misc-misc
Requires: x11-font-mutt-misc
Requires: x11-font-schumacher-misc
Requires: x11-font-sony-misc
Requires: x11-font-sun-misc
Conflicts: xorg-x11 <= 6.9.0
Obsoletes: xorg-x11 <= 6.9.0

%description
misc fonts for X.org

%files
%defattr(-,root,root)


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.0-10mdv2011.0
+ Revision: 675584
- rebuild
- br fontconfig for fc-query used in new rpm-setup-build

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9
+ Revision: 671209
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2011.0
+ Revision: 524366
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 351290
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 225995
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.1
+ Revision: 179648
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2008.0
+ Revision: 75830
- rebuild


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

