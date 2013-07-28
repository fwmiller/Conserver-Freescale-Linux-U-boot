%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : TrueType font rasterizer
Name            : freetype
Version         : 2.3.9
Release         : 1
License         : GPL or FTL
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : System Environment/Libraries
Source          : %{name}-%{version}.tar.gz
Patch1          : proper-armel-asm-declaration.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1

%Build
export CC_BUILD="$BUILDCC"
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}
make 

%Install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT/%{pfx} install
rm -f $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/*.la

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*

