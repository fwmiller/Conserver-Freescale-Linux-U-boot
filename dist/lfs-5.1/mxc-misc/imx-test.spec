%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : platform specific unit tests for mxc platform
Name            : imx-test
Version         : 3.0.35
Release         : 4.0.0
License         : GPL/Other
Vendor          : Freescale
Packager        : Rob Herring
Group           : Test
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n %{name}-%{version}-%{release}

%Build
if [ -z "$PKG_KERNEL_KBUILD_PRECONFIG" ]
then
      KERNELDIR="$PWD/../linux"
      KBUILD_OUTPUT="$PWD/../linux"
else
      KERNELDIR="$PKG_KERNEL_PATH_PRECONFIG"
      KBUILD_OUTPUT="$(eval echo ${PKG_KERNEL_KBUILD_PRECONFIG})"
fi

if [ -n "$IMX_TEST_DIR" ]
then
	cd $IMX_TEST_DIR
fi

PLATFORM_UPPER="$(echo $PLATFORM | awk '{print toupper($0)}')"

# Build modules
make -C module_test KBUILD_OUTPUT=$KBUILD_OUTPUT LINUXPATH=$KERNELDIR

# Build test apps
INCLUDE="-I$DEV_IMAGE/usr/src/linux/include \
-I$KERNELDIR/drivers/mxc/security/rng/include \
-I$KERNELDIR/drivers/mxc/security/sahara2/include"
make -j1 PLATFORM=$PLATFORM_UPPER INCLUDE="$INCLUDE" test

%Install
if [ -z "$PKG_KERNEL_KBUILD_PRECONFIG" ]
then
      KERNELDIR="$PWD/../linux"
      KBUILD_OUTPUT="$PWD/../linux"
else
      KERNELDIR="$PKG_KERNEL_PATH_PRECONFIG"
      KBUILD_OUTPUT="$(eval echo ${PKG_KERNEL_KBUILD_PRECONFIG})"
fi

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/unit_tests

if [ -n "$IMX_TEST_DIR" ]
then
	cd $IMX_TEST_DIR
fi

# install modules
make -C module_test -j1 LINUXPATH=$KERNELDIR KBUILD_OUTPUT=$KBUILD_OUTPUT \
       DEPMOD=/bin/true INSTALL_MOD_PATH=$RPM_BUILD_ROOT/%{pfx} install

PLATFORM_UPPER="$(echo $PLATFORM | awk '{print toupper($0)}')"
make PLATFORM=$PLATFORM_UPPER DESTDIR=$RPM_BUILD_ROOT/%{pfx}/unit_tests install

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
