Title: Google Home controlling sonoff lights via mqtt
Modified: 2018-10-22 15:00
Tags: mqtt, Kappelt gBridge, Google Home, sonoff, tasmota
Summary: Voice control of existing Sonoff lights through Kappelt gBridge and mqtt

# Voice control of Sonoff mqtt lights via mqtt

## Why not use the itead sonoff app?

I am an engineer and hacker (as in hackspace not black-hat).  I want to understand, control and improve stuff.  But in this case, I want a single user interface for my home automation stuff and I don't want to be tied into a single supplier's products because I am using their app.  So from the outset I chose message queue telemetry transport (mqtt) to be the integration point for all of my home automation projects.  Once messages are arriving on my mqtt broker I can write simple python scripts to tie things together or I can use heavierweight solutions like [Home Assistant](https://www.home-assistant.io/) where appropriate.

As an aside, I also want to use open source whenever possible.  There is an open source firmware for the sonoff products called [Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota) which allows control of these devices through mqtt.  I installed this firmware on all of my sonoff devices, and have had them working through the Home Assistant UI for 12 months or so.  Obviously the flashing of this firmware also renders use of the itead application impossible.

## Google Home Mini

I recently got a Google Home Mini and have been using it to control the music around the house (playing through Chromecast Audios), and to time my tea brewing :-)  Google Home also allows control of existing manufacturers devices such as Philips Hue, and others.  I wanted it to control my existing home automation setup.  

[Others](http://tinkerman.cat/using-google-assistant-control-your-esp8266-devices/) have linked Google Assistant to control a light, but the most usual route is IFTTT to a webhooks service which directly controls the device, not via mqtt!  I would have to write a clunky webhooks to mqtt service to get this to work.  The IFTTT service uses semi-fixed phrases to trigger specific events, and is not directly linked to the Google Home part of the assistant or its configuration.  In summary, most of the existing solutions didn't make me smile as an engineer they were too clunky, relied on too many services which would reduce uptime, and were potentially insecure in their communication.  

## Google Home to mqtt - Kappelt gBridge

After a long search looking for a solution to get Google Home to talk to an mqtt server, I found [Kappelt gBridge](https://gbridge.kappelt.net).  This looks fairly new, but very professional.  The software can be run on your own server or you can register to use the online service (currently free in beta test).  This ticks my boxes for needing to be open source as the project is on [github](https://github.com/kservices/gBridge). When I registered to use the online service I was user number 37...

Using the online UI to create devices and link it to my Google Home account worked well, until my complex setup caused some issues [#7](https://github.com/kservices/gBridge/issues/7) [#9](https://github.com/kservices/gBridge/issues/9).  The first was an incompatible configuration in my mqtt bridge config, and the second a complication of having multiple Google accounts, so neither was really a problem with the gBridge software itself.

## Translation needed...

So, once I had managed to connect my Google Home instance to gBridge and set up my devices, I was getting messages on my mqtt server from voice commands spoken to my Google Assistant - Fantastic!  But...

The messages coming in from gBridge are in the form:

~~~
gBridge/<user-number>/<device-number>/onoff
~~~

and the mqtt messages needed to turn on the lights are in the form:

~~~
cmnd/<device-name>/POWER
~~~

Similar translation would be needed to get the status messages back to gBridge so when I ask "OK Google, is the hall light on?" it can answer with the actual state of the light, not it's last position requested through Google Home - I can turn them on and off by other means!

You can now modify the topics that gBridge issues for each device, but it still has the prefix `gBridge/<user-number>`, and so would still not be possible to use without some translation.

So I wrote a short [python script - mqtt_babelfish](https://github.com/vanceb/mqtt_babelfish/), which runs in a Docker container on my server. It subscribes to the appropriate messages and translates them and their payloads, so that the whole system can work end-to-end.

## This is not a "Howto"

I did not intend this to be a walk-through or howto.  Let's face it anyone attempting to do this will need some prior knowledge, including how to "Google" for stuff and how to extract useful information from other's posts, but I will provide links to relevant documentation, and some of my working configs to help those who want to try to recreate this setup.

* [Kappelt gBridge service](https://gbridge.kappelt.net) 
* [Kappelt gBridge documentation](https://doc.gbridge.kappelt.net/html/index.html)
* [mqtt_bablefish](https://github.com/vanceb/mqtt_babelfish)

~~~ /etc/mosquitto/conf.d/60_bridge.conf
# =================================================================
# Bridges to Kappelt gBridge for Google Home Automation linkup
# =================================================================

connection gbridge
address mqtt.gbridge.kappelt.net:8883
remote_username gbridge-u37
remote_password <redacted>

# Specifying which topics are bridged
topic gBridge/u37/+/+ in 0
topic gBridgei/u37/+/+/set out 0

# Bridge settings
bridge_attempt_unsubscribe true

# Need to force version 3.1 or you will get socket errors!
#bridge_protocol_version mqttv311 # Doesn't work with gBridge
bridge_protocol_version mqttv31 # Force version 3.1

bridge_insecure false
bridge_capath /etc/ssl/certs
bridge_tls_version tlsv1.2

# enabling the connection automatically when the broker starts.
start_type automatic
try_private true
cleansession true
notifications false
log_type all
~~~