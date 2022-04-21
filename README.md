# bee-temperature-check
Temperature check device for a beehive using a Raspberry Pi. Used as a
teaching project to an elementary school student.

## Bill of materials
This is what you'll need to complete this project

1. Raspberry Pi (TODO: version specs)
   - A powerful, internet-convient Pi is useful for setup (Pi 3, Pi 4)
   - A basic Zero was used in final deployment (Zero v1.2)
2. (DHT 11)[https://www.adafruit.com/product/386]
3. Small breadboard, wires
4. RPi peripherals - development is done directly in Raspbian. Stuff
   like mouse, HDMI monitor, etc.

### Raspberry Pi setup
In addition to the materials (hardware) above, you'll need the following
installed on the Raspberry Pi (based on the (legacy Adafruit DHT11 
library)[https://github.com/mlhDevelopment/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py]):

- Python 3
  `sudo apt install python3`
- Python Pip
  `sudo apt install python3-pip`
- Pip Setuptools & Wheel
  `sudo python3 -m pip install --upgrade pip setuptools wheel`
- Legacy Adafruit DHT library
  `sudo pip3 install Adafruit_DHT`


## This repository
This repository is broken out into lessons based on how I presented the
material. 
