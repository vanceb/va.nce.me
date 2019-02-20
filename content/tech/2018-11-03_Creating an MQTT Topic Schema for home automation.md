Title: Creating a topic schema for home automation
Modified: 2018-11-03 15:00
Tags: mqtt, home automation
Summary: Creating a topic schema/format for home automation

# Creating a topic schema for home automation

## Consistency if possible

I am integrating a number of elements into a home automation system.  Each has their own format for topics and looking at the mqtt messages they don't really conform to a common pattern.  This can make filtering these messages a little more tricky.

Some fof the devices will have their topics fixed, and I will need to decide whether to create extra traffic and translate their topics to fit my schema.  Not really for discussion here, but it is possible.

The [Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota) firmware that I am running on a large number of my devices is configurable.  OOTB the topic format doesn't really make sense to me as it leads with the message type, and I have forced my hostname to provide additional information which should really be part of the topic hierarchy.  It is this that has led me to think about what the topic format should be...

## Hierarchy

example:

`ha/light/hall/cmnd/power1`

Broken down as follows:

1. ha - home automation prefix
2. light - subsystem
3. hall - device hostname or ID
4. cmnd - message type
5. power1 - device-specific if needed

## Expected subsystems and message types

Here are the subsystems and message types that I can think of off the top of my head.  It is unlikely to be a complete list of either.

### Subsystems

* light
* switch
* security
* entertainment

### Message types

* req - User requested state or action
* tele - telemetry
* cmnd - commanded action (the device should do something)
* stat - status update, in response to a cmnd