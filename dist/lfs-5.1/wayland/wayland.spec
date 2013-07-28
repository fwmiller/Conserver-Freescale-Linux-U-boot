%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Wayland
Name            : wayland
Version         : 1.0.3
Release         : 2
License         : X11
Vendor          : freedesktop.org
Packager        : ProFUSION embedded systems <contact@profusion.mobi>
Group           : System Environment/Libraries
URL             : freedesktop.org
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
The official package for Wayland.

%Prep
%setup

#cp src/wayland-scanner .
mkdir -p $RPM_BUILD_ROOT/share/aclocal

%Build
export PKG_CONFIG_PATH=${DEV_IMAGE}%{_prefix}/lib/pkgconfig
export PKG_CONFIG_LIBDIR=${DEV_IMAGE}%{_prefix}/lib/pkgconfig
export PKG_CONFIG_SYSROOT_DIR="$RPM_BUILD_ROOT"
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

mkdir -p $RPM_BUILD_ROOT/share/aclocal
export ACLOCAL="aclocal -I $RPM_BUILD_ROOT/share/aclocal"

if [ "$CFGHOST" = "arm-linux" ]
then
XTRA_OPTS=--disable-scanner
fi
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-documentation $XTRA_OPTS
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
rm -f $RPM_BUILD_ROOT/%{pfx}/lib/*.la
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*