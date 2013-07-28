%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Skelleton files for an embedded root filesystem
Name            : skell
Version         : 1.18
Release         : 2
License         : GPL
Vendor          : Freescale
Packager        : Steve Papacharalambous/Stuart Hughes
Group           : System Environment/Utilities
Source          : %{name}-%{version}.tar.gz
Patch1          : skell-1.18-dropbear_args.patch
Patch2          : skell-1.17-imx.patch
Patch3          : skell-1.16-imx-fsl-gstplugin.patch
Patch4          : skell-1.19-imx-fsl-gnome.patch
Patch5          : skell-1.19-imx-hal-messagebus.patch
Patch6          : skell-1.18-imx-add-ttymxc2n3.patch
Patch7          : skell-1.18-imx-add-ttymxc4n5.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%Build

%Install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT/%{pfx} install
if [ -z "$PKG_SKELL_WANT_TERMINFO" ]
then
    rm -rf $RPM_BUILD_ROOT/%{pfx}/usr/share/terminfo
fi

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%attr(0666, root, root) %dev(c, 5, 0) %{pfx}/dev/tty
%attr(0600, root, root) %dev(c, 5, 1) %{pfx}/dev/console
%attr(0666, root, root) %dev(c, 1, 3) %{pfx}/dev/null
%attr(0755, root, root) %{pfx}/usr/bin/startx
%{pfx}/*
