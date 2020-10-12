# Airmonkey 2

![](https://github.com/cudy789/airmonkey2/blob/master/img/IMG_0145.jpg)

AirMonkey 2 is a two part command and control style tool used to gain access to wireless networks.  The first part is a Python software package running on a Raspberry Pi, dubbed the "Monkey".  Second is an Android app that manages and controls the Raspberry Pi called the "Zookeeper".  The Monkey and Zookeeper can gain access to WiFi networks much faster than conventional tools while improving ease of use and portability.

AirMonkey2 has all of the standard features of common WiFi auditing tools, including AP enumeration, probe detection, and multiple attack vectors (De-auth & EvilAP).  The important distinction between AirMonkey 2 and other tools is the ease of use.  Other programs require a desktop, SSH shell, or VNC connection for control and monitoring, whereas AirMonkey 2 is completely controlled with an Android app.  This means reduced configuration and setup times with instantaneous monitoring, all on an inconspicuous Android phone.

## The Zookeeper

Ready | Capturing | Captured
-------------|--------------|-------------
![](https://github.com/cudy789/airmonkey2/blob/master/img/20190109_110342.jpg)|![](https://github.com/cudy789/airmonkey2/blob/master/img/20190101_180029.jpg)|![](https://github.com/cudy789/airmonkey2/blob/master/img/20190101_175939.jpg)

The app is simple and easy to use, with lots of options under the hood to configure.  The pictures above show the Zookeeper interface as the Monkey captures a handshake from a wireless AP in the Stakeout mode.

The various options for the Zookeeper app include:
- Stakeout mode
  - This mode scans for, then targets a specific AP and attempts to capture a handshake by sending de-auth requests.  Additional options include:
    - Number of de-auth requests
    - Duration to wait to capture a handshake
    - Targeting specific clients *
  - MiTM Attack mode
- Wardrive mode*
  - This mode utilizes Kismet to setup a wardriving environment that provides real-time feedback of captured handshakes, while storing locations on Google Maps.

*Currently in development

## The Monkey

![](https://github.com/cudy789/airmonkey2/blob/master/img/20190101_152109.jpg)

The waterproof case and large battery make the Monkey ideal for long operations stuffed into a backpack or snowbank.  The battery lasts for approximately 14 hours at idle and 10 hours with active packet sniffing.

Hardware:

- Raspberry Pi 3B
- 16GB SD Card w/Raspbian
- TP-Link TL-WN722N High Gain Wireless Adapter
- Right Angle USB Extender
- Pelican 1040 Waterproof Case
- Custom 12,000 mAh Battery with charging/discharging circuitry
