%define base %(echo %{_prefix} | sed -e s,/usr.*$,,)
%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Secure Sockets Layer toolkit
Name            : openssl
Version         : 1.0.1c
Release         : 1
License         : BSD style
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : System Environment/Libraries
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup 

%Build
case $ENDIAN in
    big)
        XTRA_OPTS="-DB_ENDIAN"
        ;;
    little)
        XTRA_OPTS="-DL_ENDIAN"
        ;;
    *)
        echo "Please set the ENDIAN environment variable to big|little"
        ;;
esac
case "$LINTARCH" in
    arm|m68k*)
       OSSL_ARCH="linux-generic32"
       ;;
    powerpc*)
       OSSL_ARCH="linux-ppc"
       ;;
    *)
       OSSL_ARCH="linux-$LINTARCH"
       ;;
esac
./Configure $OSSL_ARCH --prefix=%{_prefix} --install_prefix=$RPM_BUILD_ROOT/%{pfx} shared no-asm $XTRA_OPTS
make -j1

%Install
rm -rf $RPM_BUILD_ROOT
#SHLIB_VERSION_NUMBER=1.0.0
#for i in lib %{_prefix}/lib %{_prefix}/sbin %{_prefix}/include
#do
#    mkdir -p $RPM_BUILD_ROOT/%{pfx}/%{base}/$i
#done
#VER="`perl -e '$_  = shift; chop; print' %{version}`"
#for i in libcrypto.so libssl.so
#do 
#    cp -a $i.$SHLIB_VERSION_NUMBER $RPM_BUILD_ROOT/%{pfx}/%{base}/lib/
#    install -d $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib
#    ln -s ../../lib/$i.$SHLIB_VERSION_NUMBER $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/$i
#done
#cp -a apps/openssl $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/sbin
#cp -Lr include/openssl $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/include
#mkdir $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/pkgconfig
#cp openssl.pc $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/pkgconfig/

make install -j1

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
