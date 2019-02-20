Title: Creating an Access Point on wlan0
Modified: 2016-08-23 16:00
Tags: linux, Raspberry Pi, wireless
Summary: Setting up hostapd on wlan0 and moving client wireless config to wlan1 so in the car with a single wlan the system creates a wireless access point.  When at home we can add an additional wireless dingle and connect to the home network and upgrade the system

## Setting a static IP for wlan0

Edit the `/etc/systemd/network/wlan0.network` to give the interface a static IP

~~~ shell
[Match]
Name=wlan0

[Network]
Address=192.168.90.1/24
~~~

Restart the `systemd-networkd.service`

~~~ shell
systemctl restart systemd-networkd
~~~


## Installing hostapd

~~~ shell
pacman -S hostapd
~~~

Configure hostapd by following [this guide](https://wiki.archlinux.org/index.php/Software_access_point) and [the hostapd site](https://wireless.wiki.kernel.org/en/users/Documentation/hostapd), creating the following config.

~~~ shell
# Basics
interface=wlan0
driver=nl80211
ssid=landy
hw_mode=g
channel=1

# Security Settings - wpa2 only
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=*****REPLACE_ME*******
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
~~~

Enable the hostapd service

~~~ shell
systemctl enable hostapd
~~~

## Configure dhcp on the interface

Set up dhcpd following the [Arch Linux dhcp guide](https://wiki.archlinux.org/index.php/Dhcpd).  Note that I only want this to be enabled on wlan0 and not other interfaces, so I followed the specifics of [Listening on only one interface](https://wiki.archlinux.org/index.php/Dhcpd#Listening_on_only_one_interface)

So create a new unit definition file for the service in `/etc/systemd/system/dhcpd4@.service` The contents of this file differ from the example as I want the wlan0 interface to be up before dhcpd4 starts

~~~ shell
[Unit]
Description=IPv4 DHCP server on %I
Wants=network.target
After=network.target

[Service]
Type=forking
PIDFile=/run/dhcpd4.pid
ExecStart=/usr/bin/dhcpd -4 -q -pf /run/dhcpd4.pid %I
KillSignal=SIGINT

[Install]
WantedBy=multi-user.target
~~~


Edit the config file `/etc/dhcpd.conf`

~~~ shell
# dhcpd.conf
#
# Sample configuration file for ISC dhcpd
#

# option definitions common to all supported networks...
default-lease-time 600;
max-lease-time 7200;

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.
authoritative;

# This is a very basic subnet declaration.

subnet 192.168.90.0 netmask 255.255.255.0 {
  range 192.168.90.2 192.168.90.5;
}
~~~

Enable the service on the single interface:

~~~ shell
systemctl enable dhcpd4@wlan0
~~~
