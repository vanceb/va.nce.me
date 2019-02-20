Title: Setting up a Pi Zero W CCTV Camera
Modified: 2018-11-02 15:00
Tags: mqtt, Raspberry Pi, camera, cctv
Summary: Creating a home-grown CCTV system

# Setting up a Pi Zero W cctv system

## Install the OS

I have chosen Raspbian Stretch Lite as the base OS.  [Install
Guide](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md).

### Headless wifi setup

In order to get the pi to come up on the correct wireless network you need to
provide the details on the sdcard.  The full answer is
[here](https://www.raspberrypi.org/forums/viewtopic.php?t=191252), but the file
is included here for ease:

~~~
country=UK
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="your_real_wifi_ssid"
    scan_ssid=1
    psk="your_real_password"
    key_mgmt=WPA-PSK
}

To allow SSH access you also need to create an empty file namd `ssh` in the boot partition.

### Change the default passwords

`passwd`

### Configure OS options

Run the raspberry pi config tool `sudo raspi-config`

* Enable the camera: Option 5 Interfacing -> P1 Camera
* Expand the root file system: Option 7 Advanced Options -> A1 Expand root filesystem 

### Configure automatic OS updates

`sudo apt install unattended-upgrades`

then edit the `/etc/apt/apt.conf.d/50unattended upgrades`.  The lines I changed are as follows:

~~~
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "13:00";
~~~



