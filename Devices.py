#python version 3
#pyshark 
import pyshark
import datetime as DT

class Devices:


    def __init__(self, pcap):
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
        #print???????????????????????????

    #Show the number of layers and names
    #seq number - data sent and ack
    def showLayers(self,display):
        for x in self.cap:
            lyr = x.layers
            if (display.lower() == "yes" or display.lower() == "y"):
                if x.highest_layer != "ZBEE_BEACON":
                    print(x.number+" "+x['WPAN'].seq_no+" "+x.length+" "+str(len(x.layers))+" Layers identified: "+str(lyr))

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
 

    def idHub():
        print("")

    def getHubInfo():
        print("")



d = Devices('z.pcap') #needs to replace this 
print('------------')
packet_amount = d.showLayers("y")
print("DATA SET RANGE: "+d.getTimeRangeDataSet())
print("\n No of Devices Scan")
print("---------------------")
d.getDeviceInfo()
print("")
print(d.uniqueIP)
print("")
print("---------------------")
print("Show capture IPs/Source Interaction")
d.mapDeviceInteractions()

#References
#cap = pyshark.FileCapture('z.pcap')
#c = cap[0] -> first packet
#c[0] -> first layer in the packet
#c.highest_layer -> for each packet
