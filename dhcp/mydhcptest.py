#!/usr/bin/python
from pydhcplib.dhcp_packet import *
from pydhcplib.dhcp_network import *
from pydhcplib.dhcp_packet import DhcpPacket
from pydhcplib.type_strlist import strlist  
from pydhcplib.type_ipv4 import ipv4        
 
 
packet = DhcpPacket()                                        

packet.SetOption("htype",[1])
packet.SetOption("hlen",[6])
packet.SetOption("xid",[0x34,0x87,0x11,0x31])


packet.SetOption("ciaddr",[0x3,0x3,0x3,0x5])
packet.SetOption("giaddr",[0x3,0x3,0x3,0x3])
#packet.SetOption("chaddr",hwmac("00:17:44:55:77:88").list())
packet.SetOption("chaddr",[00,0x17,0x44,0x55,0x77,0x88,0,0,0,0,0,0,0,0,0,0])
#packet.SetOption("chaddr","00:17:44:55:77:88")


packet.SetOption("flags",[0x80,0x00])
packet.SetOption("op",[1])
packet.SetOption("dhcp_message_type",[8])
packet.SetOption("client_identifier",[1,0x00,0x17,0x44,0x55, 0x77, 0x88])
packet.SetOption("host_name", strlist("xyang-test").list())


packet.SetOption("parameter_request_list",[1,15,3,6,44,46,47,31,33,121,249,43,244])





print packet.str()                                          

 

netopt = {'client_listen_port':68,
          'server_listen_port':67,
          'listen_address':"192.168.168.1"}


class Client(DhcpClient):
   def __init__(self, options):
       DhcpClient.__init__(self,options["listen_address"],
                           options["client_listen_port"],
                           options["server_listen_port"])

   def HandleDhcpOffer(self, packet):
       print packet.str()
   def HandleDhcpAck(self, packet):
       print packet.str()
   def HandleDhcpNack(self, packet):
       print packet.str()        

client = Client(netopt)
# Use BindToAddress if you want to emit/listen to an internet address (like 192.168.1.1)
# or BindToDevice if you want to emit/listen to a network device (like eth0)
client.BindToAddress()


client.SendDhcpPacketTo(packet, "255.255.255.255", 67)

while True :
   print "gogogog"
   print client.GetNextDhcpPacket() 
   print "done"   