Title: Neopixel clock - my first project at Reading Hackspace
image: {photo}espclock/esp_clock.jpg
Tags: esp8266, kicad, pcb, lasercutter, cad, platformio
Summary: The design, development and creation of a neopixel clock using the lasercutter at Reading Hackspace.  The electronics were prototyped then a PCB was designed in Kicad before being manufactured in China.  The ESP Arduino platform was used to brite the code and Platformio was used to manage, compile and upload the code to the ESP.  The code uses libraries to create a captive portal to set the wifi details and allow OTA programming.

## The idea

I joined the [Reading Hackspace](http://rlab.org.uk/) shortly before Christmas and wanted a project that would expose me to some of the tools and expertise I now had access to.  Some of the projects that drew my eye were those using [Neopixels](https://www.adafruit.com/category/168), and one or two people were doing projects using the [ESP8266](https://en.wikipedia.org/wiki/ESP8266).  I had done some Arduino prototyping before, mainly on breadboard or stripboard, so I wanted to use that knowledge and expand it.  I was encouraged to try and create my first PCB as part of the project.

I came up with the idea of creating a neopixel clock, where each neopixel shone into some frosted acrylic, red signifies hours, blue minutes and green seconds. The colours are mixed as they overlap creating a bit of art as well as being able to display the time.    The use of acrylic would expose me to some 2D CAD and laser cutting.

Before I get into detail, all of the files relating to this project, including the CAD designs, the PCB and schematic, and the code are all hosted on [Github](https://github.com/vanceb/NightClock) if you want to take a look.

## CAD

The core of my design was to start with the Neopixels.  I had bought some [60 LED/m strip](https://www.coolcomponents.co.uk/digital-rgb-led-weatherproof-strip-60-led-1m-black.html) that could be cut out of the protective casing.  The start point for my CAD design was to calculate the circle diameter needed to support 12 pixels; this came out at 64mm and was used as the diameter for the central ring of the clock.  

I initially used [LibreCAD](http://librecad.org/cms/home.html) to draw up the clock, but had some problems getting the design into the laser cutter (more on that later), so migrated to [QCAD](http://www.qcad.org/en/) for later revisions of the design.

![Prototype ESP CLock with stripboard electronics]({photo}espclock/clock_cad.png)

The base of the clock was redesigned from the original to accommodate the PCB I later designed.  Although not shown it is in a separate CAD file in the project's [Github repository](https://github.com/vanceb/NightClock).

## Electronics and the ESP8266

The electronics part of the project is the area I was most familiar with, having already created a couple of projects using Arduinos.  For the clock I needed a time reference, I thought about hooking up an real-time clock (RTC) chip to the ESP, but digging around in the [Library Documentation](http://www.pjrc.com/teensy/td_libs_Time.html) I identified that we could use NTP to get an accurate time reference, which was ideal as the ESP has wifi as standard.

I bought a few ESP12E boards from a cheap Chinese supplier, and waited the 6 weeks for them to be delivered.  Once I had them I created my prototype using stripboard.  It can be seen in the image below driving the partially constructed clock.

![Prototype of the clock and electronics, including ESP12E, light dependent resistor, and connections for the power and neopixels]({photo}espclock/clock_prototype.jpg)

Once proven, I started to create a schematic and PCB layout in [Kicad](http://kicad-pcb.org/).  The [Getting Started Tutorial](http://docs.kicad-pcb.org/en/getting_started_in_kicad.html) was a great introduction and I was able to design my PCB with minimal assistance from others in the Hackspace.  I did redesign the layout to keep the board dimensions below 50mm, as this was the cut off point for price changes on some of the Chinese PCB prototyping sites.  However in the end I used [PCBWay](http://www.pcbway.com/) on the advice of another Hackspace member, and I don't think it mattered there.  One great piece of advice I was given by a more experienced Hackspace member was to buy the components before sending the board away for manufacture.  Print out the board layout 1:1 and make sure the components you have bought fit the pads you allocated to each component.  Kicad lets you draw the schematic then before moving on to the board layout you need to assign a PCB footprint to each component.  This is the part I found hardest in the entire PCB process.  Finding the correct footprint for the component is a nightmare as I haven't found an easy way to search the footprints and if you don't know the name of the footprint you want you can be a bit stuck.  Thankfully most of the components I was using were surface mount and fairly standard sized, so once I had found one I could more easily identify the others.  The ESP8266 footprint and schematic was reused from [another Hackspace project](https://github.com/robot-army/ESP_WeatherStation)

The final board layout is shown below, together with a photo of the boards I got back, and a populated board mounted in the clock base.  Note that I haven't entirely populated the board as I had already purchased a 3.3v wall-wart power supply, so I didn't need to voltage regulator.

![board layout]({photo}espclock/esp_pcb_layout.png)
![boards]({photo}espclock/esp_pcb.jpg)
![populated board mounted in the clock]({photo}espclock/esp_pcb_populated.jpg)

## Lasercutting

The 2D cad designs were good, but getting them imported into the lasercutter software was not so simple.  The lasercutter uses [RDWorks 7](http://en.rd-acs.com/Private/Files/63570066677298250040209701.rar) which should import Version R14 dxf files, but every time I tried to import my CAD drawing it crashed.  I tried opening the CAD file in Inkscape and re-exporting it.  The lasercutter didn't crash this time, but when cut the pieces were the wring size (Oops!).  Finally I imported the CAD file into QCad and saves from there.  It uses R15 version of dxf, but this seemed to import correctly.  On closer inspection though it had moved the radius filets on the front of the clock.  The only way I found around this was to delete the filets and redraw them in RDWorks.  Not the best, but hey, that's what hacking is all about, finding solutions!

## Code

You can inspect the code on [Github](https://github.com/vanceb/NightClock), but I just wanted to highlight the use of [Platformio](http://platformio.org/), which I think is a great dev tool.  I had used the Arduino IDE, but got frustrated with the poor editor (specifically no line numbers!)  I know you can use an external editor and use the IDE for compiling and uploading, but it is a bit of a "halfway house".  Platformio works from the command line, and has a great integration with the [Atom editor](https://atom.io/), through the [Platformio IDE Package](https://atom.io/packages/platformio-ide) It allows for cross-platform building of code (i.e. same code base for Arduino and ESP8266), supports the Arduino core software model, and enforces a reasonable structure on your project as well as managing the libraries.

Talking of libraries, I used [WifiManager](https://github.com/tzapu/WiFiManager), Platformio library number 567, and the Arduino OTA programming libraries (core Arduino).  The WifiManager library turns your ESP design "consumer-ready" thing.  You can use it to create its own wifi network with captive portal, so you can connect to it with any wifi enabled laptop or phone to setup the ssid and password to allow it to connect to your home wifi - no need to get out the FTDI cable or hardcode the credentials!  Secondly, once I had built the clock I was more reluctant to keep taking it apart, hence the need for OTA programming.  So far this works seamlessly and is supported by Platformio.  I haven't yet managed to get mDNS working, but that is a minor issue.
