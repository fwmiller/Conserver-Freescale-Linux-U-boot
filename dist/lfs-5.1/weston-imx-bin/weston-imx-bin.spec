%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Weston
Name            : weston-imx-bin
Version         : 3.0.35
Release         : 4.0.0
License         : BSD
Vendor          : freedesktop.org
Packager        : Prabhu Sundararaj
Group           : System /servers
URL             : freedesktop.org
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
BuildRequires   : libjpeg cairo pixman mtdev libffi wayland libxcb libxkbcommon libpng zlib udev

%Description
The official package for Weston.

%Prep
%setup -n %{name}-%{version}-%{release}


mkdir -p $RPM_BUILD_ROOT/share/aclocal

%Build



%Install
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}
cp -rf * $RPM_BUILD_ROOT/%{pfx}
pwd
ls


%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
