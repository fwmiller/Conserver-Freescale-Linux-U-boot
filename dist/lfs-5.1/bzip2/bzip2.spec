%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A file compression utility.
Name            : bzip2
Version         : 1.0.2
Release         : 2
License         : BSD
URL             : ftp://sources.redhat.com/pub/bzip2/v102/ 
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : Applications/File
Source          : %{name}-%{version}.tar.gz 
Patch0          : %{name}-%{version}-notest.patch
Patch1          : %{name}-%{version}-mandir.patch
Patch2          : %{name}-%{version}-armv7a-cross-compile-fix.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%Build
make -f Makefile-libbz2_so
make clean
make

%Install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/%{pfx}/%{_prefix}

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


