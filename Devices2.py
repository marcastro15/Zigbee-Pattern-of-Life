#!/usr/bin/python3

import pyshark
import datetime as DT
import sys

class Devices:


    def __init__(self, pcap, fname):
        print(pcap)
        self.cap = pyshark.FileCapture(pcap) #initialize
        #stats range
        self.cap.load_packets()
        self.n = len(self.cap) # returns # of packets
        self.data_set_range = str(self.cap[0].frame_info.time+" - "+self.cap[self.n-1].frame_info.time)
        #duration 
        date_beg_str = str(self.cap[0].frame_info.time)
        date_end_str = str(self.cap[self.n-1].frame_info.time)
        self.duration = ""
        self.uniqueIP = []
        self.filename = fname

    #Show the number of layers and names
    #seq number - data sent and ack
    def showLayers(self,display):
        for pkt in self.cap:
            lyr = pkt.layers
            if (display.lower() == "yes" or display.lower() == "y"):
                    print(str(lyr))
            if(hasattr(pkt['WPAN'],'src64')):
                    source = pkt['WPAN'].src64
                    if source not in self.uniqueIP:
                        self.uniqueIP.append(source)
            self.openFile()

    #Date/Time Sample data set collected
    def getTimeRangeDataSet(self):
        return "DATE RANGE: "+self.data_set_range +"\nNO of Packets: "+str(self.n)+"\nDURATION: "+self.duration

    #Note that all the hubs have 0x0000 address
    #How many unique devices are communicating
    def getDeviceInfo(self):
        for pkt in self.cap:
            if (hasattr(pkt['WPAN'],'src16')):
                source = pkt['WPAN'].src16
                if source not in self.uniqueIP:
                    self.uniqueIP.append(source) 

    def extractData(self):
        for pkt in self.cap:
            lyr = pkt.layers
            dstpan = wpansrc = wpandst = zextendsrc = 'None';
            sec = data = ra = fcf = 'None';
            dstpan = pkt['WPAN'].dst_pan
            #print(str(pkt.layers))
            #print("WPAN" in str(pkt.layers))
            #print(str(hasattr(pkt['WPAN'],'src16')))
            if ("WPAN" in str(pkt.layers) and hasattr(pkt['WPAN'],'src16')):
                wpansrc =  pkt['WPAN'].src16
            if ("ZBEE_NWK" in str(pkt.layers) and hasattr(pkt['ZBEE_NWK'],'dst')):
                wpandst = pkt['ZBEE_NWK'].dst
            if ("ZBEE_NWK" in str(pkt.layers) and hasattr(pkt['ZBEE_NWK'],'ext_src')):
                zextendsrc = pkt['ZBEE_NWK'].ext_src
            if ("ZBEE_NWK" in str(pkt.layers) and hasattr(pkt['ZBEE_NWK'],'security')):
                sec = pkt['ZBEE_NWK'].security
            if ("ZBEE_NWK" in str(pkt.layers) and hasattr(pkt['ZBEE_NWK'],'data')): 
                data = pkt['ZBEE_NWK'].data
            if ("ZBEE_NWK" in str(pkt.layers) and hasattr(pkt['ZBEE_NWK'],'radius')):
                ra = pkt['ZBEE_NWK'].radius
            if ("ZBEE_NWK" in str(pkt.layers) and hasattr(pkt['ZBEE_NWK'],'fcf')):
                fcf = pkt['ZBEE_NWK'].fcf
            print(dstpan+" "+wpansrc+" "+wpandst+" "+zextendsrc+" "+sec+" "+data+" "+ra+" "+fcf)


    #0x0000ffff (broadcast)
    #0x00000000 (hub)
    #any other # is a device
    def mapDeviceInteractions(self):
        for pkt in self.cap:
            if (hasattr(pkt['WPAN'],'src16') and hasattr(pkt['WPAN'],'dst16')):
                source = pkt['WPAN'].src16
                destination = pkt['WPAN'].dst16
                pan_id =  pkt['WPAN'].dst_pan
                seqno = pkt['WPAN'].seq_no
                print(pkt.number+" "+seqno+" "+source+" "+destination+" "+pan_id)
 

    def openFile(self):
        with open(self.filename,'w') as f:
            for item in self.uniqueIP:
                f.write(item)
                f.write('\n')

def main(pcaps,fnames):
    print("Parsing pcap: "+pcaps+" "+fnames)
    d = Devices(''+pcaps+'',''+fnames+'')
    d.extractData()

if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2])


#print("DATA SET RANGE: "+d.getTimeRangeDataSet())
#print("\n No of Devices Scan")
#d.getDeviceInfo()
#print("")
#print(d.uniqueIP)
#print("")
#d.mapDeviceInteractions()

#References
#cap = pyshark.FileCapture('z.pcap')
#c = cap[0] -> first packet
#c[0] -> first layer in the packet
#c.highest_layer -> for each packet

#6lowpan - IPv6 over Low power WPAN
#"Transmission of IPv6 Packets over IEEE 802.15.4
#Networks" (RFC4944) which defines the format for the adaptation
#between IPv6 and 802.15.4.
#https://www.silabs.com/documents/public/white-papers/Thread-Stack-Fundamentals.pdf

#how to run it
#python3 Devices.py MLE_channel_14.pcapng crap.txt

#Requirement sample (extracting first row)
#c = cap[0]
#1. wpan.DestinationPan -> c.wpan.dst_pan 
#2. wpan.Source ->  c.zbee_nwk.src
#3. wpan.Destination -> c.zbee_nwk.dst
#4. zigbee.ExtendedSource -> c.zbee_nwk.ext_src
#5. zigbee.NetworkKey -> c.zbee_nwk.security
#6. zigbee.Data ->  c.zbee_nwk.data
#7. zigbee.radius -> c.zbee_nwk.radius 
#8. zigbee.FrameControlField ->c.zbee_nwk.fcf.


