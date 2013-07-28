%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Interfaces for accessibility support
Name            : elftosb
Version         : 3.0.35
Release         : 4.0.0
License         : Free BSD
Vendor          : Freescale
Packager        : Frank Li
Group           : System Environment/Libraries
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
Autoreq		: no
Autoreqprov	: no
Autoprov	: no
%Description
%{summary}

%Prep
%setup -n %{name}-%{version}-%{release}

%Build
make

%Install
install -d $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin
install bld/linux/elftosb $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin
install bld/linux/keygen  $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin
install bld/linux/sbtool  $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin

%Clean

%Files
%defattr(-,root,root)
%{pfx}/*


