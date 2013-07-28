%define base %(echo %{_prefix} | sed -e s,/usr.*$,,)
%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Advanced IP routing and network device configuration tools
Name            : iproute
Version         : 2.6.38
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Jaksa Djordjevic, Stuart Hughes
Group           : Applications/System
Source          : %{name}2-%{version}.tar.bz2
Patch0          : iproute2-do-not-build-arpd.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

The iproute package contains networking utilities (ip and rtmon, for
example) which are designed to use the advanced networking
capabilities of the Linux kernel.

%Prep
%setup -n %{name}2-%{version}
%patch0 -p1

%Build

make -j1 KERNEL_INCLUDE=$DEV_IMAGE/usr/src/linux HOSTCC="$BUILDCC"

%Install
rm -rf $RPM_BUILD_ROOT
make -j1 install SBINDIR=%{base}/sbin DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
