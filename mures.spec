%define Summary Clone of Sega's "Chu Chu Rocket", a multi-player puzzle game

Summary:	%{Summary}
Name:		mures
Version:	0.5
Release:	%mkrel 7
License:	GPL
Group:		Games/Arcade
URL:		http://mures.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/mures/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.xpm
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	X11-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gcc
BuildRequires:	libSDL_ttf-devel
BuildRequires:	texinfo
BuildRequires:	ImageMagick
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

%build
%configure
make

%install
rm -rf %{buildroot}

%makeinstall

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

install -d %{buildroot}/%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%{name}
?package(%{name}): \
command="%{_bindir}/%{name}" \
icon="%{name}.png" \
needs="x11" \
section="More Applications/Games/Arcade" \
title="Mures" \
longtitle="%{Summary}"\
xdg="true"
EOF

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mures
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README TODO
%{_bindir}/*
%{_libdir}/%{name}
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


