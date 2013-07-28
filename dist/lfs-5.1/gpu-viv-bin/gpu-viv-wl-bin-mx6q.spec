%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GPU driver and app for mx6q
Name            : gpu-viv-wl-bin-mx6q
Version         : 3.0.35
Release         : 4.0.0
License         : Proprietary
Vendor          : Freescale
Packager        : Prabhu Sundararaj
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
(cd $RPM_BUILD_ROOT/%{pfx}/usr/lib/; rm libEGL.so;rm libEGL.so.1; ln -sf libEGL-wl.so libEGL.so; ln -sf libEGL-wl.so libEGL.so.1)
(cd $RPM_BUILD_ROOT/%{pfx}/usr/lib/; rm libGAL.so;ln -sf libGAL-wl.so libGAL.so)
(cd $RPM_BUILD_ROOT/%{pfx}/usr/lib/; rm libVIVANTE.so;ln -sf libVIVANTE-fb.so libVIVANTE.so)

pwd
ls

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
