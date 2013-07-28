%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Mtdev
Name            : mtdev
Version         : 1.1.3
Release         : 1
License         : X11
Vendor          : X.Org Foundation
Packager        : Prabhu Sundararaj
Group           : System Environment/Libraries
URL             : http://bitmath.org/code/mtdev/
Source          : %{name}-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
The mtdev is a stand-alone library which transforms all variants of kernel MT events to
the slotted type B protocol. The events put into mtdev may be from any MT device,
specifically type A without contact tracking, type A with contact tracking, or
type B with contact tracking. See the kernel documentation for further details.

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f
rm -f $RPM_BUILD_ROOT/%{pfx}/lib/*.la

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
