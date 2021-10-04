# Zigbee-Pattern-of-Life

ZigBee is a low-cost, low-power wireless protocol (IEEE 802.15.4) that is becoming increasingly popular in IOT and home automation markets.  Given the wide reliance throughout the home, commercial, and energy sectors on ZigBee technology, the significance of ensuring the security and privacy of this protocol cannot be overstated. Pattern of life traffic will be collected from ZigBee devices, analyzed via internally developed software, and used to identify privacy and security vulnerabilities.

#Mandatory PCAP Capture
-----------------------
- All pcaps must have identifiable zigbee layers when capturing traffic: The ZigBee specification is divided into five layers.
   + the physical (PHY) layer
   = the medium access control (MAC) layer, the network (NWK) layer, the application support (APS) layer, and the application framework (AF) layer.
- Ref: https://www.sciencedirect.com/topics/computer-science/zigbee-specification
 
#Requirements
-------------
- Any Linux environment
- Knowledge of Wireshark
- Knowledge of Python, Matplotlib

#Installation
-------------
- sudo apt-get update
- sudo apt-get install python3.6
- sudo apt install python3-pip
- pip3 install python-csv
- pip3 install pyshark
- pip3 install matplotlib
- pip3 install thread

#How to run it?
---------------
- Syntax: python3 program_file, parameter2_pcap_name
- Example: python3 <filename>.py <pcap>
