%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : WPA Supplicant for wifi
Name            : wpa_supplicant
Version         : 0.5.9
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Sam Yang
Group           : Application/System
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
wpa_supplicant is an implementation of the WPA Supplicant component,
i.e., the part that runs in the client stations. It implements WPA key
negotiation with a WPA Authenticator and EAP authentication with
Authentication Server. In addition, it controls the roaming and IEEE
802.11 authentication/association of the wlan driver.

%{summary}

%Prep
%setup 

%Build
#Create .config file for build
cat > .config << EOF
#CONFIG_DRIVER_HOSTAP=n
#CONFIG_DRIVER_HERMES=n
#CONFIG_DRIVER_MADWIFI=n
#CONFIG_DRIVER_ATMEL=n
CONFIG_DRIVER_WEXT=y
#CONFIG_DRIVER_NDISWRAPPER=n
#CONFIG_DRIVER_BROADCOM=n
#CONFIG_DRIVER_IPW=n
#CONFIG_DRIVER_BSD=n
#CONFIG_DRIVER_NDIS=n

CONFIG_WIRELESS_EXTENSION=y
CONFIG_IEEE8021X_EAPOL=y

#CONFIG_EAP_MD5=y
#CONFIG_EAP_MSCHAPV2=y
#CONFIG_EAP_TLS=y
#CONFIG_EAP_PEAP=y
#CONFIG_EAP_TTLS=y
#CONFIG_EAP_GTC=y
#CONFIG_EAP_OTP=y
#CONFIG_EAP_SIM=y
#CONFIG_EAP_AKA=y
CONFIG_EAP_PSK=y
#CONFIG_EAP_SAKE=y
#CONFIG_EAP_GPSK=y
#CONFIG_EAP_PAX=y
#CONFIG_EAP_LEAP=y
#CONFIG_PCSC=y

CONFIG_CTRL_IFACE=y

CONFIG_L2_PACKET=linux
EOF

#Create a default ap config file
cat > ap_config.conf << EOF
ctrl_interface=/var/run/wpa_supplicant
update_config=1

network={
        ssid="cisco-2"
        key_mgmt=NONE
        auth_alg=OPEN
        disabled=1
        id_str="p2"
}
EOF

make CONFIG_L2_PACKET=linux

%Install
rm -rf $RPM_BUILD_ROOT
make install CONFIG_L2_PACKET=linux prefix=%{_prefix} DESTDIR=$RPM_BUILD_ROOT/%{pfx}
mkdir -p  $RPM_BUILD_ROOT/%{pfx}/usr/etc/unifi
cp ap_config.conf $RPM_BUILD_ROOT/%{pfx}/usr/etc/unifi


%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*
