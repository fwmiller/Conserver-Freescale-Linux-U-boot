%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : libffi
Name            : libffi
Version         : 3.0.11
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

%Build
ACLOCAL="aclocal -I $RPM_BUILD_ROOT/share/aclocal"
#./configure
#make
echo $CROSS_COMPILE
echo $TOOLCHAIN
echo $CC
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-dependency-tracking
make clean
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
rm -f $RPM_BUILD_ROOT/%{pfx}/lib/*.la

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*