%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Weston
Name            : weston-imx
Version         : 3.0.35
Release         : 4.0.0
License         : X11
Vendor          : freedesktop.org
Packager        : Prabhu Sundararaj
Group           : System Environment/Libraries
URL             : freedesktop.org
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
BuildRequires   : libjpeg cairo pixman mtdev libffi wayland libxkbcommon libpng zlib udev

%Description
The official package for Weston.

%Prep
%setup -n %{name}-%{version}-%{release}


mkdir -p $RPM_BUILD_ROOT/share/aclocal

%Build


export ACLOCAL="aclocal -I ${DEV_IMAGE}%{_prefix}/share/aclocal"
export WLD=${DEV_IMAGE}%{_prefix}

export COMPOSITOR_LIBS="-lGLESv2 -lEGL -lGAL -lwayland-server -lxkbcommon -lpixman-1 -lffi"
export COMPOSITOR_CFLAGS="-I $WLD/include -I $WLD/include/pixman-1 -DLINUX=1 -DEGL_API_FB -DEGL_API_WL"
export CLIENT_CFLAGS="-I $WLD/include -I $WLD/include/cairo -I $WLD/include/pixman-1"
export CLIENT_LIBS="-lGLESv2 -lEGL -lwayland-client -lwayland-cursor -lxkbcommon"
export SIMPLE_EGL_CLIENT_CFLAGS="-DLINUX=1 -DEGL_API_FB -DEGL_API_WL -I $WLD/include"
export SIMPLE_EGL_CLIENT_LIBS="-lGLESv2 -lEGL -lwayland-client -lwayland-cursor"
export IMAGE_LIBS="-lwayland-cursor"
export WESTON_INFO_LIBS="-lwayland-client"
export LIBDIR=${DEV_IMAGE}%{_prefix}

./autogen.sh --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}

make


%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
BIN_DIR=$RPM_BUILD_ROOT/%{pfx}%{_prefix}/bin/
mkdir -p $BIN_DIR
cp clients/simple-egl $BIN_DIR
cp clients/simple-shm $BIN_DIR
cp clients/simple-touch $BIN_DIR
cp clients/flower $BIN_DIR
cp clients/smoke $BIN_DIR
cp clients/resizor $BIN_DIR
cp clients/keyboard $BIN_DIR
cp clients/clickdot $BIN_DIR
cp clients/cliptest $BIN_DIR

mkdir $RPM_BUILD_ROOT/%{pfx}/usr/share/X11
tar xvvf xkb.tar.gz
mv xkb $RPM_BUILD_ROOT/%{pfx}/usr/share/X11/

mkdir -p $RPM_BUILD_ROOT/%{pfx}/root/.config
cp weston.ini $RPM_BUILD_ROOT/%{pfx}/root/.config/

cat <<EOF > $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/start-weston
#!/bin/sh

export LD_LIBRARY_PATH="/usr/lib"
export XDG_RUNTIME_DIR="/tmp"
mkdir -p XDG_RUNTIME_DIR
export GAL2D_DISPLAY=1
export XDG_CONFIG_HOME=/root/.config

weston&

EOF
chmod +x $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/start-weston
OUTPUT_PKG="%{name}-bin-%{version}-%{release}"
# Package up the build results and leave in rpm/SOURCES
rm -rf $OUTPUT_PKG
install -d $OUTPUT_PKG
cp -rf $RPM_BUILD_ROOT/%{pfx}/* $OUTPUT_PKG
tar -zcf $OUTPUT_PKG.tar.gz $OUTPUT_PKG
# todo fix this to use rpmdir or something better than TOP:
install $OUTPUT_PKG.tar.gz $TOP/rpm/
install $OUTPUT_PKG.tar.gz $TOP/rpm/SOURCES

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
