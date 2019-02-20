Title: Building a TTN Gateway
Modified: 2019-02-20 15:00
Tags: ttn, lorawan, pi
Summary: Building and configuring a LoRaWAN TTN gateway using a Raspberry Pi and an IMST IC880A concentrator

# Building a TTN Gateway

## Introduction

I have been doing quite a bit of electronics recently using the ESP32 because
I like the connectivity it offers through wifi.  But it is only really usable
in the house when wired to the mains as it is not power efficient.  I wanted an
alternative which can operate at low power using a battery.

Looking around, you can go for the mobile phone networks, but again they are
not really that power efficient and they want to charge you for the privilege.
So I have settled on LoRaWan as the technology of choice, but there is no
coverage in my area.  Time to rectify that!

## The Things Network

[The Things Network](https://www.thethingsnetwork.org/) (TTN) aim to build
an open global network of gateways.  Obviously the cost model doesn't allow
them to flood the countryside with gateways so its up to the users to provide
the coverage.  You can buy ready built gateways or build one yourself.  As you
guessed I want for the second option.

At the moment there doesn't seem to be a single design that is winning out but
I settled on using a Raspberry Pi and an [IC880A LORA
concentrator](https://wireless-solutions.de/products/radiomodules/ic880a.html).

## How do I build a gateway...

The main repository for LoRa software seems to be the [Semtech LoRa network
Github](https://github.com/Lora-net), but there are many derived versions from
this.  A couple which directly target the Raspberry Pi and IC880A concentrator
are:

* [LoRaWAN Gateway build instructions from
ttn-zh](https://github.com/ttn-zh/ic880a-gateway/wiki)
* [LoRaWAN Gateway build by RS based on
ttn-zh](https://www.rs-online.com/designspark/building-a-raspberry-pi-powered-lorawan-gateway)
* [LoRaWAN Gateway based on using
Balena](https://www.instructables.com/id/Raspberry-Pi-LoRaWAN-Gateway/)
* [Jac Kersing's packet_forwarder](https://github.com/kersing/packet_forwarder)

I used all of these sources to get an overview of what I needed to build and
power the gateway.

For the hardware setup I used the [ttn-zh
guide](https://github.com/ttn-zh/ic880a-gateway/wiki).  For the software stack I
choose to use Jac Kersing's `packet_forwarder`
repository.  It has a good install script which clones
and builds each of the elements of software needed to get the gateway up and
running `packet_forwarder/mp_pkt_fwd/build-pi.sh`

## Configuration of the Gateway

### At the TTN website

Create an account and then [register
a gateway](https://www.thethingsnetwork.org/docs/gateways/registration.html).
Once registered you will need to remember the Gateway ID and the Gateway Key
from the web interface, as you will need these for your configuration.

### Configuring packet_forwarder

At the end of the build script you are told to [download the 
`global_config.json`](https://github.com/TheThingsNetwork/gateway-conf), 
and use the sample local_config.json to configure your specific router.

Both of these files should reside in the "install directory", which by default
is `/opt/ttn-gateway`.  The configuration inside of the `servers` json object
are the details from your gateway configuration page on the TTN website, except
that the server address isn't given.  A bit of searching brought this up as
[router.eu.thethings.network](https://www.thethingsnetwork.org/forum/t/new-addresses-for-cloud-services-update-your-gateways/1813)

### False start...

After the build and configuration I tried to start the `mp_pkt_fwd`, but this
failed with a fairly non-descript error message "failed to start the
concentrator", which after a bit of searching suggested that I hadn't reset the
IC880A board before trying to start the packet forwarder.  I thought I had done
this using the `/opt/ttn-gateway/dev/lora_gateway/reset_lgw.sh` script.  After
some investigation it turns out I fell for the old trick of using the GPIO pin
number instead of the GPIO#!  The correct command to reset the board using Pin
22 (GPIO#25) is:

~~~ shell
sudo /opt/ttn-gateway/dev/lora_gateway/reset_lgw.sh start 25
~~~

## Finishing up the build

To make sure that all of the files used on a daily basis were together
I symlinked the reset script into the top-level directory:

~~~
ln -s /opt/ttn-gateway/dev/lora_gateway/reset_lgw.sh /opt/ttn-gateway
~~~

To ensure that the gateway came up after a restart I created a systemd service
definition which includes pre and post tasks to reset the board:

~~~
[Unit]
Description=The Things Network Gateway Packet Forwarder
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/ttn-gateway
SyslogIdentifier=ttn-gateway

ExecStartPre=/opt/ttn-gateway/reset_lgw.sh start 25
ExecStart=/opt/ttn-gateway/mp_pkt_fwd -l /var/log/ttn-gateway.log

ExecStopPost=/opt/ttn-gateway/reset_lgw.sh stop 25

[Install]
WantedBy=multi-user.target
~~~

This was saved at `/etc/systemd/system/ttn-gateway.service`, which was then
installed and started:

~~~
sudo systemctl enable ttn-gateway
sudo systemctl start ttn-gateway
~~~
