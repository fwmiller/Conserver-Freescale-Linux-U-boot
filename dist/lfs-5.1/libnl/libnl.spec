%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A collection of libraries providing APIs to netlink protocol based Linux kernel interfaces
Name            : libnl
Version         : 1.1
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Terry Lv
Group           : System Environment/Libraries
Source          : %{name}-%{version}.tar.gz
Patch0          : libnl-1.1-netlink-local-fix.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
The libnl suite is a collection of libraries providing APIs to netlink protocol based Linux kernel interfaces. 

Netlink is a IPC mechanism primarly between the kernel and user space processes. It was designed to be a more flexible successor to ioctl to provide mainly networking related kernel configuration and monitoring interfaces. 

%Prep
%setup
%patch0 -p1

%Build
export CC="${TOOLCHAIN_PREFIX}gcc"
./configure --prefix="$RPM_BUILD_ROOT/%{pfx}" --host=${CFGHOST} --build=%{_build} 
make clean
make
unset CC

%Install
rm -rf $RPM_BUILD_ROOT
make install

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*

