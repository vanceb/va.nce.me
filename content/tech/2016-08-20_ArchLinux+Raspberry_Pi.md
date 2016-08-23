Title: Installing Arch Linux on Raspberry Pi with Wireless
Modified: 2016-08-20 15:00
Tags: linux, Raspberry Pi
Summary: Summary of setting up Arch Linux or Raspberry Pi B+ in preparation for the Landy Hi-fi

## Introduction

I am building a hi-fi for the Land Rover using a Raspberry Pi as an MP3 player and interface server.  It also contains a DAB radio development board and a self-designed board to act as a pre-amp for source selection and volume as well as controlling the power to the Pi.

## Installing Arch Linux

The Arch Linux for ARM team have a great guide to [installing on the Pi](https://wiki.archlinux.org/index.php/Raspberry_Pi) in the installation section.  You will need to follow the guide specific to the type of Pi you are installing on, in my case [B+](https://archlinuxarm.org/platforms/armv6/raspberry-pi).

Once you have installed the OS onto the SD card its time to boot.  After boot, I updated the system.

~~~ shell
pacman -Syu
~~~

## Setting the locale

Edit the file `/etc/locale.gen` and uncomment your locale, `en_GB.UTF-8` in my case.  Then regenerate the locales

~~~ shell
locale-gen
~~~

Set the Language for subsequent reboots by editing the file `/etc/locale.conf` to include:

~~~ shell
LANG=en_GB.UTF-8
LC_COLLATE=C
~~~

## Enabling wifi

I needed to get the wifi network working.  Although the drivers for the USB wifi dongle I was using were included in the install, `wpa_supplicant` was not installed, which meant I could not get it to join my WPA protected network.

Unfortunately this is a bit "chicken and egg" as I needed a network connection to be able to use the network card.  Back to the Ethernet cable...

After logging in I did the following to get the wifi working:

* Install some additional packages:
~~~ shell
pacman -S wpa_supplicant crda
~~~

* setup the initial wpa_supplicant config file with the following lines which will allow `wpa_cli` to create the connection config:

~~~ shell
ctrl_interface=/var/run/wpa_supplicant
update_config=1
~~~

* Setup the wifi manually:
~~~ shell
wpa_supplicant -B -i wlan0 -c wpa_supplicant.conf
wpa_cli
~~~

Follow the prompts through `wpa_cli` and it will put a `network` section into your `wpa_supplicant.conf` file.

I am not too familiar with `systemd`, so have been around the houses here.  I copied the `network` section into a new file called `/etc/wpa_supplicant/wpa_supplicant-wlan0.conf`, then enabled this interface-specific config, and dhcp for the interface using `systemd`:

~~~ shell
systemd enable wpa_supplicant@wlan0
systemd enable dhcpcd@wlan0
~~~

After a reboot I had a working wireless interface...

I followed a couple of guides to get this working, neither of which were very complete.  Although I now have a working config I am not sure this is the best way of getting networking up.  Maybe take a look at `netctl`...

After managing to get the wifi working I came across [this page](http://qdosmsq.dunbar-it.co.uk/blog/2013/06/beginners-guide-to-arch-linux-on-the-raspberry-pi-part-2/comment-page-1/), which gives a potentially simpler method.  However, I haven't tried it...
