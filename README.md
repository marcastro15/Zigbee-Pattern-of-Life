# Zigbee-Pattern-of-Life

ZigBee is a low-cost, low-power wireless protocol (IEEE 802.15.4) that is becoming increasingly popular in IOT and home automation markets.  Given the wide reliance throughout the home, commercial, and energy sectors on ZigBee technology, the significance of ensuring the security and privacy of this protocol cannot be overstated. Pattern of life traffic will be collected from ZigBee devices, analyzed via internally developed software, and used to identify privacy and security vulnerabilities.

#Mandatory PCAP Capture
-----------------------
- All pcaps must have identifiable zigbee layers when capturing traffic: The ZigBee specification is divided into five layers as shown below. Depending upon the nature and complexity of the of the devices, they use 2 - 5 layers using naming conventions.
   + the physical (PHY) layer
   + the medium access control (MAC) layer
   + the network (NWK) layer
   + the application support (APS) layer
   + and the application framework (AF) layer.
- Sample layers from zigbee_sample.pcap file
   - WPAN Layer, <ZBEE_NWK Layer>, <ZBEE_APS Layer>
   - WPAN Layer, 
   - WPAN Layer, , <ZBEE_NWK Layer>]
   - WPAN Layer, , <ZBEE_NWK Layer>]
   - WPAN Layer, <ZBEE_NWK Layer>]
- Sample captured layers from HP.pcapng
   + WPAN Layer, <ZBEE_NWK Layer>]
   + WPAN Layer,  <ZBEE_NWK Layer>]
   + WPAN Layer,  <ZBEE_NWK Layer>]
   + WPAN Layer,  <ZBEE_NWK Layer>]
- Ref: https://www.sciencedirect.com/topics/computer-science/zigbee-specification
 
#General Requirements
---------------------
- Any Linux environment
- Knowledge of Wireshark
- Knowledge of Python, Matplotlib

#Special Requirements
---------------------
- Very Important: Understand Pyshark API with the corresponding Zigbee field values
  + Read this paper first: https://www.sciencedirect.com/topics/computer-science/zigbee-specification#:~:text=The%20ZigBee%20specification%20is%20divided,application%20framework%20(AF)%20layer.

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
- Syntax: python3 program_file 
- Example: python3 <filename>.py  
- Note: You need to replace "d = Devices('z.pcap') #needs to replace this" with the correct pcap file.
  
#Future Update - Specify the requirement analysis
---------------------------------
I - Phase I
1. Requirements Analysis: Need to identify which field values to correlate to output to tables 
2. Create Plots based on #2 item
3. Create a baseline of a pattern of life of each device by using the values captured by Killerbee
II - Phase II
1. Machine Learning
