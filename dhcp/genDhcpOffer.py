from dhcpUtil import *


if __name__ == "__main__":
    clientMac = "78:2b:cb:c9:e8:41"
    clientIp = "10.39.1.125"
    #dstIp = "255.255.255.255"
    dstIp = "10.39.1.1"
    relayAgentIp = "10.39.1.1"


    reqList = [1,15,3,6,44,46,47,31,33,121,249,43,244]
    isBroadcast = 0

    sendDhcpOfferPacket(clientMac, clientIp, dstIp , relayAgentIp, isBroadcast)