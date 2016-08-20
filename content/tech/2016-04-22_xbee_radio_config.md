Title: Trouble with XBee radios
Modified: 2016-04-22 15:00
Tags: XBee
Summary: Problems flashing XBee radios - They are not Bricked...

# Fun with XBee Zigbee Rasdios from Digi

I have successfully set up a pair of XBee Zigbee radios for use with a remote monitoring project.  It took ages to get reliable results and I made some notes which I have promptly lost.  I am now trying to get another pair working and am finding it difficult again, so need to make some more permanent notes and observations...

## Observations

* When you flash an "Endpoint" radio, the default config specifies that it uses "Cyclic Sleep" mode, which makes communication with it difficult.  If XCTU cannot communicate with it you need to "reset" the radio (Lift it out of its socket in my case)

* Flashing firmware often fails in XCTU, but don't despair you haven't bricked the radio!  Go to the "Tools" menu and select "XBee Recovery", which will walk you through flashing the software using the bootloader.

    - You also need to know the Product family for the flashing.

        - XBee Pro S2B = XBP24BZ7
        - XBee Series 2 = XB24-ZB

* On OSX at least the newer version of XCTU ( Version: 6.3.0 Build ID: 20151110-8) fails to recover some devices, but the older version (Version: 6.2.0 Build ID: 20150508-6) seems to work fine...
