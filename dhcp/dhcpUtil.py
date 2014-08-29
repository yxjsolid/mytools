#!/usr/bin/python
from pydhcplib.dhcp_packet import *
from pydhcplib.dhcp_network import *
from pydhcplib.dhcp_packet import DhcpPacket
from pydhcplib.type_strlist import strlist  
from pydhcplib.type_ipv4 import ipv4        
 

class MyDhcpPacket(DhcpPacket):
    def __init__(self):
        DhcpPacket.__init__(self)

        self.SetOption("htype",[1])
        self.SetOption("hlen",[6])
        self.SetOption("xid",[0x34,0x87,0x11,0x31])
        self.SetOption("host_name", strlist("xyang-test").list())

    def setRequest(self):
        self.SetOption("op",[1])

    def setTypeInfom(self):
        self.SetOption("dhcp_message_type",[8])

    def setReply(self):
        self.SetOption("op",[2])

    def setTypeOffer(self):
        self.SetOption("dhcp_message_type",[2])

    def setBootpFlag(self, isBoradCast):
        if isBoradCast:
            self.SetOption("flags",[0x80,0x00])

    def setClientMac(self, macStr):
        macList =  map(lambda x : int(x,16), macStr.split(":"))
        self.SetOption("chaddr",macList + [0] * 10)
        self.SetOption("client_identifier",[1] + macList)

    def setClientIp(self, ipStr):
        ipList =  map(lambda x : int(x,10), ipStr.split("."))
        self.SetOption("ciaddr",ipList)

    def setYiClientIp(self, ipStr):
        ipList =  map(lambda x : int(x,10), ipStr.split("."))
        self.SetOption("yiaddr",ipList)

    def setRequestOption(self, reqList):
        self.SetOption("parameter_request_list",reqList)

    def setRealyAgent(self, ipStr):
        ipList =  map(lambda x : int(x,10), ipStr.split("."))
        self.SetOption("giaddr", ipList)


class MyClient(DhcpClient):
   def __init__(self, netopt):
       DhcpClient.__init__(self,netopt["listen_address"],
                           netopt["client_listen_port"],
                           netopt["server_listen_port"])

   def HandleDhcpOffer(self, packet):
       print packet.str()
   def HandleDhcpAck(self, packet):
       print packet.str()
   def HandleDhcpNack(self, packet):
       print packet.str()        


def sendDhcpInformPacket(clientMac, clientIp, dstIp, reqList, isBroadCast):

    netopt = {'client_listen_port':68,'server_listen_port':67,'listen_address':"0.0.0.0"}

    client = MyClient(netopt)
    client.BindToAddress()
    packet = MyDhcpPacket()

    packet.setRequest()
    packet.setTypeInfom()

    packet.setClientMac(clientMac)
    packet.setClientIp(clientIp)
    packet.setBootpFlag(isBroadCast)
    packet.setRequestOption(reqList)
    client.SendDhcpPacketTo(packet, dstIp, 67)


def sendDhcpOfferPacket(clientMac, clientIp, dstIp, relayAgentIp, isBroadCast):

    netopt = {'client_listen_port':67,'server_listen_port':67,'listen_address':"0.0.0.0"}

    client = MyClient(netopt)
    client.BindToAddress()
    packet = MyDhcpPacket()

    packet.setReply()
    packet.setTypeOffer()

    packet.setClientMac(clientMac)
    packet.setYiClientIp(clientIp)
    packet.setBootpFlag(isBroadCast)
    packet.setRealyAgent(relayAgentIp)

    client.SendDhcpPacketTo(packet, dstIp, 67)



