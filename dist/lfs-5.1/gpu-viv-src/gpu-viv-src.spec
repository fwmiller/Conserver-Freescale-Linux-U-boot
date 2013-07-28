%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GPU on imx6q that supports OpenGLES and OpenVG
Name            : gpu-viv-src
Version         : 3.0.35
Release         : 4.0.0
License         : Proprietary
Vendor          : Vivante
Packager        : Richard Zhao
Group           : Development/Libraries
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n %{name}-%{version}-%{release}

%Build
CROSS_COMPILE=${TOOLCHAIN_PREFIX}
export DFB_DIR=$DEV_IMAGE/usr
export ROOTFS_USR=${DEFPFX}/usr/ubuntu_arm_lib
cd driver
./driver_build_sample.sh clean
rm -Rf ../driver-x11
rm -Rf ../driver-dfb
rm -Rf ../driver-wl
cp -r ../driver ../driver-x11
cp -r ../driver ../driver-dfb
cp -r ../driver ../driver-wl
./driver_build_sample.sh
export X11_ARM_DIR=${DEFPFX}/usr/ubuntu_arm_lib
export ROOTFS_USR=
cd ../driver-x11
./driver_build_sample_x11.sh
unset X11_ARM_DIR

export BUILD_OPTION_EGL_API_FB=0
export EGL_API_DFB=1
cd ../driver-dfb
./driver_build_sample.sh
unset EGL_API_DFB
unset BUILD_OPTION_EGL_API_FB

export X11_ARM_DIR=
export DFB_DIR=
cd ../test
./test_build_sample.sh clean
#rm -Rf ../test-x11
#cp -r ../test ../test-x11
./test_build_sample.sh
#export X11_ARM_DIR=$DEV_IMAGE/usr
#cd ../test-x11
#./test_build_sample_x11.sh
#export X11_ARM_DIR=

export X11_ARM_DIR=
export DFB_DIR=
export ROOTFS_USR=


cd ../driver
export SDK_DIR="`pwd`/build/sdk"
cd ../driver-wl

cd driver/wl

mkdir -p $RPM_BUILD_ROOT/%{pfx}/share/aclocal
mkdir -p ${DEV_IMAGE}%{_prefix}/share/aclocal


export ACLOCAL="aclocal -I ${DEV_IMAGE}%{_prefix}/share/aclocal"

export PKG_CONFIG_LIBDIR=${DEV_IMAGE}%{_prefix}/lib/pkgconfig
export PKG_CONFIG_SYSROOT_DIR=${DEV_IMAGE}
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
export PKG_CONFIG_PATH=${DEV_IMAGE}%{_prefix}/lib/pkgconfig
export PKG_CONFIG_SYSROOT_DIR=${DEV_IMAGE}

export LD_LIBRARY_PATH="$SDK_DIR/drivers"
export LDFLAGS="-L$SDK_DIR/drivers -L$RPM_BUILD_ROOT/%{pfx}%{_prefix}"
export CFLAGS="-I $SDK_DIR/include -I $SDK_DIR/include/HAL -I $RPM_BUILD_ROOT/%{pfx}%{_prefix}/include/wayland-viv -I ${DEV_IMAGE}%{_prefix}/include"


./autogen.sh --prefix=%{_prefix} --host=$CFGHOST
make
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
cd ../../
export LDFLAGS=
#export CFLAGS="-I ${DEV_IMAGE}%{_prefix}/include"
export LIBS="-L ${DEV_IMAGE}%{_prefix}/lib"
export EGL_API_FB=1
export EGL_API_WL=1
export VIVANTE_NO_VG=1
target=drivers
export WAYLAND_DIR=$RPM_BUILD_ROOT/%{pfx}%{_prefix}
export LD_LIBRARY_PATH=$SDK_DIR/drivers
export WAYLAND_CLIENT_LIBS="-L$SDK_DIR/drivers -L$RPM_BUILD_ROOT/%{pfx}%{_prefix}/lib"
pwd
./driver_build_sample.sh clean
./driver_build_sample.sh
export EGL_API_WL=
export WAYLAND_DIR=


%Install
SOC=$(echo $PLATFORM | cut -d_ -f1 | cut -c2-)
OUTPUT_PKG="gpu-viv-bin-$SOC-%{version}-%{release}"
OUTPUT_PKG_WL="gpu-viv-wl-bin-$SOC-%{version}-%{release}"
NATIVE_BUILD_X11_ENV="remote-env"

rm -rf $RPM_BUILD_ROOT
GPU_VIV_DIR="`pwd`"
cd driver-wl/driver/wl
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
cd $GPU_VIV_DIR
install -d $RPM_BUILD_ROOT/%{pfx}
install -d $RPM_BUILD_ROOT/%{pfx}/usr/lib
install -d $RPM_BUILD_ROOT/%{pfx}/usr/lib/directfb-1.4-0
install -d $RPM_BUILD_ROOT/%{pfx}/usr/lib/directfb-1.4-0/gfxdrivers

cp -raf driver/build/sdk/drivers/* $RPM_BUILD_ROOT/%{pfx}/usr/lib
mv $RPM_BUILD_ROOT/%{pfx}/usr/lib/libEGL.so.1.0 $RPM_BUILD_ROOT/%{pfx}/usr/lib/libEGL-fb.so
mv $RPM_BUILD_ROOT/%{pfx}/usr/lib/libGAL.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libGAL-fb.so
mv $RPM_BUILD_ROOT/%{pfx}/usr/lib/libVIVANTE.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libVIVANTE-fb.so
cp -af driver-x11/build/sdk/drivers/libEGL.so.1.0 $RPM_BUILD_ROOT/%{pfx}/usr/lib/libEGL-x11.so
cp -af driver-x11/build/sdk/drivers/libGAL.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libGAL-x11.so
cp -af driver-x11/build/sdk/drivers/libVIVANTE.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libVIVANTE-x11.so
cp -af driver-dfb/build/sdk/drivers/libEGL.so.1.0 $RPM_BUILD_ROOT/%{pfx}/usr/lib/libEGL-dfb.so
cp -af driver-dfb/build/sdk/drivers/libGAL.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libGAL-dfb.so
cp -af driver-dfb/build/sdk/drivers/libVIVANTE.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libVIVANTE-dfb.so
cp -af driver-wl/build/sdk/drivers/libEGL.so.1.0 $RPM_BUILD_ROOT/%{pfx}/usr/lib/libEGL-wl.so
cp -af driver-wl/build/sdk/drivers/libGAL.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libGAL-wl.so
cp -af driver-wl/build/sdk/drivers/libVIVANTE.so $RPM_BUILD_ROOT/%{pfx}/usr/lib/libVIVANTE-wl.so
if [ ! -d "$TOP/rpm/${NATIVE_BUILD_X11_ENV}" ]; then
	mkdir -p $TOP/rpm/${NATIVE_BUILD_X11_ENV}
fi
cp -rf driver-x11/build/sdk $TOP/rpm/${NATIVE_BUILD_X11_ENV}/

(cd $RPM_BUILD_ROOT/%{pfx}/usr/lib/; ln -sf libEGL-fb.so libEGL.so; ln -sf libEGL-fb.so libEGL.so.1)
(cd $RPM_BUILD_ROOT/%{pfx}/usr/lib/; ln -sf libGAL-fb.so libGAL.so)
(cd $RPM_BUILD_ROOT/%{pfx}/usr/lib/; ln -sf libVIVANTE-fb.so libVIVANTE.so)
mv $RPM_BUILD_ROOT/%{pfx}/usr/lib/libdirectfb_gal.so \
   $RPM_BUILD_ROOT/%{pfx}/usr/lib/directfb-1.4-0/gfxdrivers/

install -d $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples
cp -af test/build/sdk/samples/* $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples/
#install -d $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples-x11
#cp -af driver-x11/build/sdk/samples/* $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples-x11/
#cp -af test-x11/build/sdk/samples/* $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples-x11/

install -d $RPM_BUILD_ROOT/%{pfx}/usr/include/
cp -af driver/build/sdk/include/* $RPM_BUILD_ROOT/%{pfx}/usr/include

# Package up the build results and leave in rpm/SOURCES
rm -rf $OUTPUT_PKG
rm -rf $OUTPUT_PKG_WL
install -d $OUTPUT_PKG
install -d $OUTPUT_PKG_WL
cp -rf $RPM_BUILD_ROOT/%{pfx}/* $OUTPUT_PKG
cp -rf $RPM_BUILD_ROOT/%{pfx}/* $OUTPUT_PKG_WL
tar -zcf $OUTPUT_PKG.tar.gz $OUTPUT_PKG
tar -zcf $OUTPUT_PKG_WL.tar.gz $OUTPUT_PKG_WL
# todo fix this to use rpmdir or something better than TOP:
install $OUTPUT_PKG.tar.gz $TOP/rpm/
install $OUTPUT_PKG.tar.gz $TOP/rpm/SOURCES
install $OUTPUT_PKG_WL.tar.gz $TOP/rpm/
install $OUTPUT_PKG_WL.tar.gz $TOP/rpm/SOURCES/

# Now delete everything we just tarred up.
rm -rf $RPM_BUILD_ROOT/%{pfx}
# Create an empty directory for rpm to have something install or it won't be happy.
install -d $RPM_BUILD_ROOT/%{pfx}/usr

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*
