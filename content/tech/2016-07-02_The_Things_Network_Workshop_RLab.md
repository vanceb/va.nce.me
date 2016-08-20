Title: Summary notes from the RLab LoRaWAN TTN Day
Modified: 2016-06-02 15:00
Tags: python, BBC Microbit, IOT, LoRaWAN
Summary: Brief notes from the RLab TTN Workshop

## TTN Hack Day

### Mark Stanley's Thingitude

[Thingithon links](https://github.com/Thingitude/thingithon01/wiki)

#### Mark's "Things Uno" Practical Walkthrough

Roughly following the [The Things Uno Tutorial](https://github.com/TheThingsNetwork/examples/tree/master/workshops/TheThingsUno).  

### LoRaWAN Hardware

* [Multitech mdot](http://www.multitech.co.uk/brands/multiconnect-mdot)
* [Link Labs Pi Hat LoRaWAN Gateway](https://www.amazon.co.uk/dp/B01G7G54O2/)

#### Arm M0 boards (Not LoRaWAN)

* [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/products/13664)

## Setting up the Microbit to talk LoRaWAN using the new protocol

Take [Richard's original Hackaday for LoRaWAN](https://hackaday.io/project/12164-ju`st-do-iot) and the example and library code for the [TheThingsUno](https://github.com/TheThingsNetwork/sdk/blob/master/devices/TheThingsUno/release/TheThingsUno.zip?raw=true).  Use the calls from the library code to update Richard's micropython script for the Microbit.

### Useful references

* [RN2483 Radio Module Serial Commands](http://ww1.microchip.com/downloads/en/DeviceDoc/40001784B.pdf)
* [Microbit Programming](https://www.microbit.co.uk/)
* [Microbit Micropython API](http://microbit-micropython.readthedocs.io/en/latest/)
* [Node-red](http://nodered.org/)
* [TTN Uno Example Setup](https://github.com/TheThingsNetwork/examples/tree/master/workshops/TheThingsUno)
* [Microbit Micropython API Ref](http://microbit-micropython.readthedocs.io/en/latest/index.html)
* [IFTTT Maker](https://ifttt.com/maker)

## Viewing packets from the ttn mqtt feed

Download ttnctl from [here](https://staging.thethingsnetwork.org/wiki/Backend/ttnctl/QuickStart) to get the password for mosquitto_sub

~~~ shell
mosquitto_sub -h staging.thethingsnetwork.org -t '70B3D57ED00005D0/devices/0004A30B001B2CD5/up' -u 70B3D57ED00005D0 -P 'EokMLv5CAarTUYU63nAq+8ZEhGVLms6cgQRbzZtBkqA='
~~~
