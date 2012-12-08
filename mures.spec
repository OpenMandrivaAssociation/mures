Summary:	Clone of Sega's "Chu Chu Rocket", a multi-player puzzle game
Name:		mures
Version:	0.5
Release:	17
License:	GPL
Group:		Games/Arcade
URL:		http://mures.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/mures/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.xpm
Patch0:		mures-0.5-linkage.patch
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	texinfo
BuildRequires:	imagemagick
# Author: Adam D'Angelo <dangelo@ntplx.net>

%description
Mures is a cross-platform clone of Sega's "Chu Chu Rocket" written using
C. To start the game, run "mures -hN -aiM" where N and M are the number of
human and computer players at the local computer. Press enter to start the
game, press P to pause, and Q to quit.
- Player 1: Use the mouse to target, and click and drag in the desired
direction to place an arrow.
- Player 2: Use the arrow keys to target, and the number keypad to place
arrows.
- Player 3: Use A,W,S,D to target and I,J,K,L to place arrows.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure2_5x
make

%install
rm -rf %{buildroot}

%makeinstall_std

mv %{buildroot}/%{_bindir}/%{name} %{buildroot}/%{_bindir}/%{name}.real
cat << EOF > %{buildroot}/%{_bindir}/%{name}
#!/bin/sh

pushd %{_libdir}/%{name}
    %{name}.real --no3d "\$@"
popd
EOF
chmod +x %{buildroot}/%{_bindir}/%{name}

mkdir -p %{buildroot}/%{_libdir}/%{name}
cp -a src/images src/maps src/sounds src/gui src/*.lua src/textures %{buildroot}/%{_libdir}/%{name}
rm -rf %{buildroot}/%{_libdir}/%{name}/{*,*/*}/Makefile*

install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

convert -size 48x48 %{SOURCE1} %{buildroot}/%{_liconsdir}/%{name}.png
convert -size 32x32 %{SOURCE1} %{buildroot}/%{_iconsdir}/%{name}.png
convert -size 16x16 %{SOURCE1} %{buildroot}/%{_miconsdir}/%{name}.png


# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mures
Comment=Multi-player puzzle game
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%doc AUTHORS ChangeLog INSTALL README TODO
%{_bindir}/*
%{_libdir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5-15mdv2011.0
+ Revision: 666500
- mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.5-14
+ Revision: 636321
- rebuild
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-13mdv2011.0
+ Revision: 606671
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-12mdv2010.1
+ Revision: 523404
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5-11mdv2010.0
+ Revision: 426201
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.5-10mdv2009.1
+ Revision: 351613
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.5-9mdv2009.0
+ Revision: 218425
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.5-9mdv2008.1
+ Revision: 153272
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Mar 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-7mdv2007.1
+ Revision: 146622
- fix summary

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-6mdv2007.1
+ Revision: 146181
- Import mures

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-6mdv2007.1
- use the %%mrel macro
- fix xdg menu
- fix icons

* Sun Jan 01 2006 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5-5mdk
- Rebuild

* Mon Sep 06 2004 Michael Scherer <misc@mandrake.org> 0.5-4mdk
- Rebuild

