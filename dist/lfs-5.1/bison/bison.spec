%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A GNU general-purpose parser generator
Name            : bison
Version         : 2.6
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : Development/Tools
Source          : bison-2.6.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --mandir=%{_mandir}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


