#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kanagram
Version  : 21.12.3
Release  : 37
URL      : https://download.kde.org/stable/release-service/21.12.3/src/kanagram-21.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.3/src/kanagram-21.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.3/src/kanagram-21.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kanagram-bin = %{version}-%{release}
Requires: kanagram-data = %{version}-%{release}
Requires: kanagram-license = %{version}-%{release}
Requires: kanagram-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkeduvocdocument-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kanagram package.
Group: Binaries
Requires: kanagram-data = %{version}-%{release}
Requires: kanagram-license = %{version}-%{release}

%description bin
bin components for the kanagram package.


%package data
Summary: data components for the kanagram package.
Group: Data

%description data
data components for the kanagram package.


%package doc
Summary: doc components for the kanagram package.
Group: Documentation

%description doc
doc components for the kanagram package.


%package license
Summary: license components for the kanagram package.
Group: Default

%description license
license components for the kanagram package.


%package locales
Summary: locales components for the kanagram package.
Group: Default

%description locales
locales components for the kanagram package.


%prep
%setup -q -n kanagram-21.12.3
cd %{_builddir}/kanagram-21.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646537011
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1646537011
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kanagram
cp %{_builddir}/kanagram-21.12.3/COPYING %{buildroot}/usr/share/package-licenses/kanagram/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/kanagram-21.12.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/kanagram/1bd373e4851a93027ba70064bd7dbdc6827147e1
pushd clr-build
%make_install
popd
%find_lang kanagram

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kanagram

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kanagram.desktop
/usr/share/config.kcfg/kanagram.kcfg
/usr/share/icons/hicolor/128x128/apps/kanagram.png
/usr/share/icons/hicolor/16x16/apps/kanagram.png
/usr/share/icons/hicolor/24x24/apps/kanagram.png
/usr/share/icons/hicolor/32x32/apps/kanagram.png
/usr/share/icons/hicolor/48x48/apps/kanagram.png
/usr/share/icons/hicolor/64x64/apps/kanagram.png
/usr/share/icons/hicolor/80x80/apps/kanagram-harmattan.png
/usr/share/icons/hicolor/scalable/apps/kanagram.svgz
/usr/share/kanagram/ui/Blackboard.qml
/usr/share/kanagram/ui/LetterButton.qml
/usr/share/kanagram/ui/icons/1player.png
/usr/share/kanagram/ui/icons/2player.png
/usr/share/kanagram/ui/icons/about-kanagram.png
/usr/share/kanagram/ui/icons/about-kde.png
/usr/share/kanagram/ui/icons/arrow-light.svgz
/usr/share/kanagram/ui/icons/close.png
/usr/share/kanagram/ui/icons/hint.png
/usr/share/kanagram/ui/icons/kanagram-handbook.png
/usr/share/kanagram/ui/icons/left-arrow.png
/usr/share/kanagram/ui/icons/on-off-light.svgz
/usr/share/kanagram/ui/icons/question-light.svgz
/usr/share/kanagram/ui/icons/reveal.png
/usr/share/kanagram/ui/icons/right-arrow.png
/usr/share/kanagram/ui/icons/spanner-light.svgz
/usr/share/kanagram/ui/icons/timer.png
/usr/share/kanagram/ui/icons/wikipedia.png
/usr/share/kanagram/ui/images/background.jpg
/usr/share/kanagram/ui/images/chalkboard.png
/usr/share/kanagram/ui/images/header.png
/usr/share/kanagram/ui/main.qml
/usr/share/kanagram/ui/sounds/chalk.ogg
/usr/share/kanagram/ui/sounds/chalk.wav
/usr/share/kanagram/ui/sounds/right.ogg
/usr/share/kanagram/ui/sounds/right.wav
/usr/share/kanagram/ui/sounds/wrong.ogg
/usr/share/kanagram/ui/sounds/wrong.wav
/usr/share/knsrcfiles/kanagram.knsrc
/usr/share/metainfo/org.kde.kanagram.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kanagram/general-settings.png
/usr/share/doc/HTML/ca/kanagram/helpstates.png
/usr/share/doc/HTML/ca/kanagram/index.cache.bz2
/usr/share/doc/HTML/ca/kanagram/index.docbook
/usr/share/doc/HTML/ca/kanagram/kanagram-hint.png
/usr/share/doc/HTML/ca/kanagram/kanagram.png
/usr/share/doc/HTML/ca/kanagram/newstuff-dialog.png
/usr/share/doc/HTML/ca/kanagram/vocab-editor.png
/usr/share/doc/HTML/ca/kanagram/vocab-settings.png
/usr/share/doc/HTML/de/kanagram/general-settings.png
/usr/share/doc/HTML/de/kanagram/helpstates.png
/usr/share/doc/HTML/de/kanagram/index.cache.bz2
/usr/share/doc/HTML/de/kanagram/index.docbook
/usr/share/doc/HTML/de/kanagram/kanagram-hint.png
/usr/share/doc/HTML/de/kanagram/kanagram.png
/usr/share/doc/HTML/de/kanagram/newstuff-dialog.png
/usr/share/doc/HTML/de/kanagram/newstuff-settings.png
/usr/share/doc/HTML/de/kanagram/shortcuts-settings.png
/usr/share/doc/HTML/de/kanagram/vocab-editor.png
/usr/share/doc/HTML/de/kanagram/vocab-settings.png
/usr/share/doc/HTML/en/kanagram/general-settings.png
/usr/share/doc/HTML/en/kanagram/helpstates.png
/usr/share/doc/HTML/en/kanagram/index.cache.bz2
/usr/share/doc/HTML/en/kanagram/index.docbook
/usr/share/doc/HTML/en/kanagram/kanagram-hint.png
/usr/share/doc/HTML/en/kanagram/kanagram.png
/usr/share/doc/HTML/en/kanagram/newstuff-dialog.png
/usr/share/doc/HTML/en/kanagram/vocab-editor.png
/usr/share/doc/HTML/en/kanagram/vocab-settings.png
/usr/share/doc/HTML/es/kanagram/index.cache.bz2
/usr/share/doc/HTML/es/kanagram/index.docbook
/usr/share/doc/HTML/et/kanagram/index.cache.bz2
/usr/share/doc/HTML/et/kanagram/index.docbook
/usr/share/doc/HTML/it/kanagram/index.cache.bz2
/usr/share/doc/HTML/it/kanagram/index.docbook
/usr/share/doc/HTML/nl/kanagram/answer-highlight.png
/usr/share/doc/HTML/nl/kanagram/general-settings.png
/usr/share/doc/HTML/nl/kanagram/helpstates.png
/usr/share/doc/HTML/nl/kanagram/index.cache.bz2
/usr/share/doc/HTML/nl/kanagram/index.docbook
/usr/share/doc/HTML/nl/kanagram/kanagram-hint.png
/usr/share/doc/HTML/nl/kanagram/kanagram.png
/usr/share/doc/HTML/nl/kanagram/newstuff-dialog.png
/usr/share/doc/HTML/nl/kanagram/newstuff-settings.png
/usr/share/doc/HTML/nl/kanagram/shortcuts-settings.png
/usr/share/doc/HTML/nl/kanagram/vocab-editor.png
/usr/share/doc/HTML/nl/kanagram/vocab-settings.png
/usr/share/doc/HTML/pt/kanagram/index.cache.bz2
/usr/share/doc/HTML/pt/kanagram/index.docbook
/usr/share/doc/HTML/pt_BR/kanagram/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kanagram/index.docbook
/usr/share/doc/HTML/ru/kanagram/index.cache.bz2
/usr/share/doc/HTML/ru/kanagram/index.docbook
/usr/share/doc/HTML/sv/kanagram/answer-highlight.png
/usr/share/doc/HTML/sv/kanagram/general-settings.png
/usr/share/doc/HTML/sv/kanagram/helpstates.png
/usr/share/doc/HTML/sv/kanagram/index.cache.bz2
/usr/share/doc/HTML/sv/kanagram/index.docbook
/usr/share/doc/HTML/sv/kanagram/kanagram-hint.png
/usr/share/doc/HTML/sv/kanagram/kanagram.png
/usr/share/doc/HTML/sv/kanagram/newstuff-dialog.png
/usr/share/doc/HTML/sv/kanagram/newstuff-settings.png
/usr/share/doc/HTML/sv/kanagram/vocab-editor.png
/usr/share/doc/HTML/sv/kanagram/vocab-settings.png
/usr/share/doc/HTML/uk/kanagram/general-settings.png
/usr/share/doc/HTML/uk/kanagram/helpstates.png
/usr/share/doc/HTML/uk/kanagram/index.cache.bz2
/usr/share/doc/HTML/uk/kanagram/index.docbook
/usr/share/doc/HTML/uk/kanagram/kanagram-hint.png
/usr/share/doc/HTML/uk/kanagram/kanagram.png
/usr/share/doc/HTML/uk/kanagram/newstuff-dialog.png
/usr/share/doc/HTML/uk/kanagram/vocab-editor.png
/usr/share/doc/HTML/uk/kanagram/vocab-settings.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kanagram/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kanagram/1bd373e4851a93027ba70064bd7dbdc6827147e1

%files locales -f kanagram.lang
%defattr(-,root,root,-)

