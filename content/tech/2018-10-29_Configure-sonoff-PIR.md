Title: Configuring sonoff basic to handle PIR input
Modified: 2018-10-29 15:00
Tags: sonoff, tasmota, mqtt
Summary: Sonoff Tasmota, open-source firmware for iTead sonoff devices has
support for integration of other sensors using spare GPIO pins.  This requires
some additional configuration.

# Configuring sonoff basic to handle PIR input

## Introduction

[Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota), an open-source
firmware for iTead sonoff devices has support for integration of other sensors
using spare GPIO pins.  This requires some additional configuration.  This
documents the configuration of a [Sonoff
Basic](https://github.com/arendst/Sonoff-Tasmota/wiki/Sonoff-Basic).

## Configuration

The [documentation](https://github.com/arendst/Sonoff-Tasmota/wiki/Commands) is
a little short on examples, so here's what I did.  To handle the extra input
I need to configure an additional "switch" on GPIO14, and then configure it to
send a custom mqtt message when the "switch" is triggered by movement detected
on a connected PIR.

* Configure GPIO14 to trigger "switch2" - You can choose a different switch,
  but the number here and the number for switchmode<x> need to match...
* Set switchtopic = [device]/movement - This enables mqtt on sensor trigger and
  sets the topic
* Set switchmode2 to appropriate value for your sensor

Configuration can be set and checked with mqtt messages.  It helps to have
`mosquitto_sub` running in another terminal so you can see the responses:

~~~
mosquitto_pub -t cmnd/[device]/gpio14 -m "10"
mosquitto_pub -t cmnd/[device]/switchtopic -m "[device]/movement"
mosquitto_pub -t cmnd/[device]/switchmode2 -m "1"
~~~

As a result of this configuration, when movement is detected mqtt messages
are sent for movement detected and movement stopped respectively:

~~~
cmnd/[device]/movement/POWER2 ON
cmnd/[device]/movement/POWER2 OFF
~~~
