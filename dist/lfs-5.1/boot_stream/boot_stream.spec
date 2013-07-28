%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : imx233/imx28-style boot stream image creation
Name            : imx-bootlets-src
Version         : 3.0.35
Release         : 4.0.0
License         : GPL
Vendor          : Freescale
Packager        : Terry Lv
Group           : Tools
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n %{name}-%{version}-%{release}

%Build
export CMDLINE1="$PKG_BOOT_STREAM_CMDLINE1"
export CMDLINE2="$PKG_BOOT_STREAM_CMDLINE2"
export CMDLINE3="$PKG_BOOT_STREAM_CMDLINE3"
export CMDLINE4="$PKG_BOOT_STREAM_CMDLINE4"

PLATFORMSHORTNAME=`echo $PLATFORM | sed "s,imx\([0-9]*\).*,MX\1,g"`
if [ "x$PLATFORMSHORTNAME" = "xMX233" ]
then
    make -j1 MEM_TYPE="${PKG_BOOT_STREAM_MEMTYPE_PRECONFIG}"
else
    make -j1 MEM_TYPE="${PKG_BOOT_STREAM_MEMTYPE_PRECONFIG}" BOARD=iMX28_EVK
fi

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/boot
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}/boot

%Clean
rm -rf $RPM_BUILD_ROOT
make clean

%Files
%defattr(-,root,root)
%{pfx}/*
