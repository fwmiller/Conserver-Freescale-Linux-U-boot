%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : freescale xec source code
Name            : fsl-xec-src
Version         : 3.0.35
Release         : 4.0.0
License         : Proprietary
Vendor          : Freescale
Packager        : Katherine Lu
Group           : System/Servers
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
This package provides proprietary libraries, and
application sources.

%{summary}

%Prep
%setup -n %{name}-%{version}-%{release}

%Build
# build the libraries and kernel modules 
make all CROSS_COMPILE=$TOOLCHAIN_PREFIX

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr/local
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr/local/lib
make install_all ROOTFS=$RPM_BUILD_ROOT/%{pfx}

# Package up the build results and leave in rpm/SOURCES for fls-xec-bin spec file
rm -rf fsl-xec-bin-%{version}-%{release}
mkdir fsl-xec-bin-%{version}-%{release}
mv $RPM_BUILD_ROOT/%{pfx}/* fsl-xec-bin-%{version}-%{release}
tar -zcf fsl-xec-bin-%{version}-%{release}.tar.gz fsl-xec-bin-%{version}-%{release}
# todo fix this to use rpmdir or something better than TOP:
cp -f fsl-xec-bin-%{version}-%{release}.tar.gz $TOP/rpm/RPMS/"$LINTARCH"
cp -f fsl-xec-bin-%{version}-%{release}.tar.gz $TOP/rpm/SOURCES

# Now delete everything we just tarred up.  fsl-xec-bin spec file will install it.
rm -rf $RPM_BUILD_ROOT/%{pfx}
# Create an empty directory for rpm to have something install or it won't be happy.
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr



%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
