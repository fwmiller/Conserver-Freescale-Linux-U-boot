%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : libxkbcommon
Name            : libxkbcommon
Version         : 0.2.0
Release         : 1
License         : GPLv2
Vendor          : Freescale
Packager        : Daniele Dall'Acqua
Group           : Applications/System
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{pfx}/%{_prefix}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib -name "*.la" | xargs rm -f
rm -f $RPM_BUILD_ROOT/%{pfx}/lib/*.la

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
