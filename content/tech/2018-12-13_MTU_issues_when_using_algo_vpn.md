Title: Creating an algo vpn server on google cloud (GCE)
Modified: 2018-12-13 15:00
Tags: gce, vpn
Summary: Setting up Algo VPN on Google Compute Engine (GCE)

# VPN server on GCE

I am running algo VPN on the free tier of Google Compute Engine (GCE).  This
generally works fine, but there have been problems accessing google related
sites when connected to the VPN.  This seems to be a [common
problem](https://github.com/trailofbits/algo/issues/210), which seems to relate
to MTU issues when using the VPN.

Using the advice on the above thread I identified the maximum working MTU was
1372, and I could reliably get connection once I had set this MTU on the IPSec
interface:

~~~
sudo ifconfig ipsec0 mtu 1372
~~~

But as the VPN comas up automatically when I am not on my home netowrk I wanted
to automate the application of the MTU.  When the ipsec0 interface comes up it
has an MTU of 1400...

## Automating MTU setting on connection of the VPN

[This
post](https://apple.stackexchange.com/questions/32354/how-do-you-run-a-script-after-a-network-interface-comes-up)
suggests a way of monitoring system files and running a script when they
change.  This requires 3 stages:

### plist file

The plist file provides the config which registers files to be monitored and
defines the script to run when they do.

~~~ xml

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" \
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>setMTU</string>

  <key>LowPriorityIO</key>
  <true/>

  <key>ProgramArguments</key>
  <array>
    <string>/Users/vance/bin/setMTU.sh</string>
  </array>

  <key>WatchPaths</key>
  <array>
    <string>/etc/resolv.conf</string>
    <string>/Library/Preferences/SystemConfiguration/NetworkInterfaces.plist</string>
    <string>/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist</string>
  </array>

  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>

~~~

Installing this file:

~~~ shell

launchctl load setMTU.plist
launchctl start setMTU

~~~

### The shell script

The shell script checks resolv.conf and if using the VPN nameserver 172.16.0.1
then it sets the MTU on the ipsec0 interface.

~~~ shell

#!/bin/sh
IPSEC_DNS="172.16.0.1"
grep "$IPSEC_DNS" /etc/resolv.conf
if [ $? -eq 0 ]; then
  sudo ifconfig ipsec0 mtu 1372
fi

~~~

### Allowing passwordless sudo

Edit the sudoers file `sudo visudo` and add the following lines:

~~~ shell

# Needed for automatic MTU modification
vance ALL = (root) NOPASSWD: /sbin/ifconfig
 
~~~
