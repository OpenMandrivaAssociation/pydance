%define	name	pydance
%define	version	1.0.3
%define	release	%mkrel 6
%define	Summary	A Dance Dance Revolution simulator

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Url:		http://icculus.org/pyddr/
Source0:	%{name}-%{version}.tar.bz2
Source2:	%{name}-README.mandrake.bz2
#Patch0:	%{name}-0.8.1-no-djtheme.patch.bz2
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
pyDDR is fun dancing game for experience asian dance beat!
Showing friends your hot move with big score!
 
Highly configurable, colorful animated arrow motion, limitless
numbers of dance steps, 1 or 2 players, professionally written
music, laughter provoking sound effects, and yes, even graphical
transitions.

%prep
%setup -q
#%patch0
bzcat %{SOURCE2} > README.mandrake

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install-zip DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

#(peroyvind) remove announcer which uses non-free files
%{__rm} -rf $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/themes/dj/mrt

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}		
Icon=%{name}				
Categories=Game;		
Name=%{name}
Comment=%{Summary}
EOF

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
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/*/*
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%{_bindir}/*

