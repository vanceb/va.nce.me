Title: Setting up the Monkeyboard DAB Radio on the Raspberry Pi
Modified: 2016-08-20 16:00
Tags: linux, Raspberry Pi, DAB
Summary: Getting the DAB radio working on the Pi

## DAB Radio

I bought a DAB radio development board from [cool components](https://www.coolcomponents.co.uk/dab-dab-fm-digital-radio-development-board-pro-with-slideshow.html), which should connect to the Pi over USB.  The board is made by an Australian company called [Monkeyboard](http://www.monkeyboard.org/products/85-developmentboard/85-dab-dab-fm-digital-radio-development-board-pro).  I have reached out to their support folks and found them very helpful.

## Install the build tools

The build tools are not installed by default.  The equivalent of the `build-essential` packaged from Debian is `base-devel`:

~~~ shell
pacman -S base-devel
~~~

## Follow the handy guide...

Monkeyboard have a guide to [setting up Monkeyboard DAB Radio on the Raspberry Pi](http://www.monkeyboard.org/tutorials/78-interfacing/87-raspberry-pi-linux-dab-fm-digital-radio), so here goes...

~~~ shell
curl -O http://www.monkeyboard.org/images/products/dab_fm/raspberrypi_keystone.tgz
tar -zxvpf raspberrypi_keystone.tgz
cd keystone/KeyStoneCOMM
make install
cd ../app
make
./testdab
~~~

Contrary to the `README.txt` file, the library is provided already built and the Makefile in `/keystone/KeyStoneCOMM` cannot build the library as the source file is missing.
