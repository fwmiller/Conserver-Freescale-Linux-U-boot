%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : MBX 3D driver and app
Name            : mbx-bin
Version         : 3.0.35
Release         : 4.0.0
License         : Proprietary
Vendor          : Freescale
Packager        : Yi Li
Group           : System/Servers
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n %{name}-%{version}-%{release}

%Build

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}
cp -rf * $RPM_BUILD_ROOT/%{pfx}
pwd
ls

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
