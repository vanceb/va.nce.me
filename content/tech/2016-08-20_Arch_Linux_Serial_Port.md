Title: Setting up the Serial port on Raspberry Pi under Arch Linux
Modified: 2016-08-20 15:10
Tags: linux, Raspberry Pi
Summary: Getting the serial port working for communication with an Atmel 328P

## Introduction

The hifi in the landy is controlled by an Atmel 328P microcontroller.  I want the Raspberry Pi to be able to talk to the microcontroller using a serial port connection.  In order to do this I need to setup the serial port on the Pi

## Serial Console

By default the serial console is attached to the serial port.  To turn it off it's back to our old friend `systemctl`

~~~ shell
systemctl disable serial-getty@ttyAMA0
~~~

You also need to remove the console from the `/boot/cmdline.txt` file.  Edit the file and remove the following stanzas from the commandline:

~~~ shell
console=ttyAMA0,115200
kgdboc=ttyAMA0,115200
~~~

Then reboot...

## Listening to the serial port

Install `python`, `pip` and `pyserial`

~~~ shell
pacman -S python python-pip
pip install pyserial
~~~

The Atmel 328P is configured to send log messages out of its serial port.  I want a short python program to listen to them.

~~~ python
#!/usr/bin/python
import serial

with serial.Serial(port='/dev/ttyAMA0',baudrate=9600) as ser:
    while True:
        l = ser.readline()
        print(l.decode('UTF-8'))
~~~
