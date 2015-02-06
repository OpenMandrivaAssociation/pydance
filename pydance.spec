%define	name	pydance
%define	version	1.0.3
%define release	8
%define	Summary	A Dance Dance Revolution simulator

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Url:		http://icculus.org/pyddr/
Source0:	%{name}-%{version}.tar.bz2
Source2:	%{name}-README.mandrake.bz2
Patch0:		pydance-1.0.3-fix-desktop-file.patch
Group:		Games/Other
Summary:	%{Summary}
BuildArch:	noarch
Requires:	pygame
Provides:	pyddr
Obsoletes:	pyddr
BuildRequires:	python imagemagick
BuildRequires:  zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
pyDDR is a fun dancing game to experience asian dance beat!
Showing friends your hot move with big score!
 
Highly configurable, colorful animated arrow motion, limitless
numbers of dance steps, 1 or 2 players, professionally written
music, laughter provoking sound effects, and yes, even graphical
transitions.

%prep
%setup -q
%patch0 -p1
bzcat %{SOURCE2} > README.mandrake

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install-zip DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

#(peroyvind) remove announcer which uses non-free files
%{__rm} -rf $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/themes/dj/mrt

%{__install} -d $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -size 16x16 icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert -size 32x32 icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -size 48x48 icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%{__install} -m644 desktop.pydance -D $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif
											  
%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc CREDITS ChangeLog LICENSE README TODO
%doc README.mandrake docs/*.txt docs/*.html
%{_gamesdatadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/*/*
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%{_bindir}/*



%changelog
* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 1.0.3-7mdv2010.0
+ Revision: 375617
- remove redundant desktop file (#49387)
- fix desktop file

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-6mdv2009.0
+ Revision: 259403
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-5mdv2009.0
+ Revision: 247260
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 25 2008 Funda Wang <fundawang@mandriva.org> 1.0.3-3mdv2008.1
+ Revision: 157783
- fix desktop entry

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-2mdv2008.1
+ Revision: 135456
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import pydance


* Fri Sep 30 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.0.3-2mdk
 - Buildrequires fix 

* Wed Apr 06 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.3-1mdk
- 1.0.3

* Thu Aug 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-2mdk
- rebuild for new menu

* Thu Jul 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-1mdk
- 1.0.2

* Fri Apr 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.1-1mdk
- 1.0.1

* Tue Mar 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.0-1mdk
- 1.0.0
- use zip install
- use provided icon
- add kde .desktop entry

* Thu Feb 12 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-1mdk
- 0.9.1

* Tue Feb 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.0-2mdk
- add more docs as requested by Joe Wreschnig <piman@debian.org>

* Wed Feb 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.0-1mdk
- 0.9.0
- drop buildrequires

* Mon Jan 12 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.4-1mdk
- 0.8.4

* Mon Jan 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8.3-1mdk
- 0.8.3

* Mon Nov 17 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.2-1mdk
- 0.8.2
- drop P0
- fix buildrequires (lib64..)

* Sun Sep 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.1-1mdk
- 0.8.1
- regenerate P0

* Wed Jul 30 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.7.4-1mdk
- 0.7.4
- package has been renamed to pydance
- don't use soundwrapper

* Thu Jul 03 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.7.1-1mdk
- 0.7.1

* Fri Jun 06 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.7.0-1mdk
- 0.7.0
- drop stefile.txt from %%doc, no longer in source
- fix file permissions

* Tue Jun 03 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6.5-1mdk
- 0.6.5

* Fri May 30 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6.4-1mdk
- 0.6.4

* Tue May 20 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6.3-1mdk
- 0.6.3
- dropped ddrmat and pyddr.txt from docs as they're no longer included
  in the source
- added docs/README.html to docs
- removed pygame from BuildRequires

* Mon Apr 28 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6.2-1mdk
- 0.6.2

* Thu Apr 10 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.6.1-1mdk
- initial release
