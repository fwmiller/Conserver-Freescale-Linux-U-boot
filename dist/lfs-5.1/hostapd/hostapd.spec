%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : hostapd is a user space daemon for access point and authentication servers
Name            : hostapd
Version         : 1.1
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Terry Lv
Group           : System Environment/Libraries
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
cd ./hostapd
cp -f ./defconfig ./.config
sed -i 's,#CONFIG_IEEE80211N=y,CONFIG_IEEE80211N=y,' ./.config
make clean
export CFLAGS="-I${DEV_IMAGE}/include -I${DEV_IMAGE}/usr/include"
export LIBS="-L${DEV_IMAGE}/lib -L${DEV_IMAGE}/usr/lib"
make CC="${TOOLCHAIN_PREFIX}gcc"
unset CFLAGS
unset LIBS

%Install
rm -rf $RPM_BUILD_ROOT
cd ./hostapd
echo %{pfx}
echo %{_prefix}
echo $RPM_BUILD_ROOT
export DESTDIR="$RPM_BUILD_ROOT/%{pfx}"
make install

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*

