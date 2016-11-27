Title: Installing rune audio on Raspberry Pi 3 with IQaudIO Pi-DAC+
Modified: 2016-11-19 16:00
Tags: linux, Raspberry Pi, audio
Summary: Installing rune audio on a Pi 3 with IQaudIO Pi-DAC+

## Installing

Install rune audio on an SD card using [this guide](http://www.runeaudio.com/documentation/quick-start/sd-card-setup-mac/)

## Getting it to recognise the IQaudIO Pi-DAC+

I bought an [IQaudIO Pi-DAC+](http://www.iqaudio.co.uk/audio/8-pi-dac-0712411999643.html).  Really easy to connect up and sounds great once working.

Boot the Pi login as `root` using the password `rune`, and make sure that the standard sound modules are disabled by editing `/etc/modules-load.d/raspberrypi.conf` and comment out the following lines

~~~ shell
#snd_bcm2835
~~~

Edit the `/boot/config.txt` file to enable I2S and the device tree overlay for the DAC+, by uncommenting the following lines

~~~ shell
dtparam=i2s=on
...
device_tree_overlay=iqaudio-dacplus
~~~

Reboot the Pi...

## Configure through WebUI

Set up the wifi network - follow the prompts

Set up the sources - I am using a network drive using CIFS (SMB).  I had a few problems getting it to mount...  Until I put my password in Quotes!!!!
