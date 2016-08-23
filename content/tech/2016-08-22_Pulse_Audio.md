Title: Installing and testing PulseAudio on the Pi
Modified: 2016-08-22 16:00
Tags: linux, Raspberry Pi, audio
Summary: Installing and testing PulseAudio on the Pi in preparation for mpd install

## Install

Simple...

~~~ shell
pacman -S pulseaudio
~~~

As advised on the [Arch Linux wiki for pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio), I will test configuration changes on the per-user config file rather than the global one.  However, once configured I will need to copy the changes back into the global config as I will be running headless and there will be no "logged-in user"

~~~ shell
mkdir -p ~/.config/pulse
cd ~/.config/pulse
cp /etc/pulse/* .

## Getting the HiFiBerry DAC+ drivers working
Following [this guide](https://www.hifiberry.com/guides/configuring-linux-3-18-x/)

* Remove drivers from the blacklist - There were no blacklisted modules in `/etc/modprobe.d/`

* Remove the onboard sound driver by removing the line `snd_bcm2835` from the file `/etc/modules-load.d/raspberrypi.conf`

* configure device tree overlay, add the following lines to the `/boot/config.txt` file

~~~ shell
# Hifiberry DAC+
dtoverlay=hifiberry-dacplus
