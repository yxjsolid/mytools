from dhcpUtil import *


if __name__ == "__main__":
    clientMac = "78:2b:cb:c9:e8:41"
    clientIp = "3.3.3.5"
    dstIp = "255.255.255.255"
    #dstIp = "192.168.168.2"

    reqList = [1,15,3,6,44,46,47,31,33,121,249,43,244]
    isBroadcast = 1

    sendDhcpInformPacket(clientMac, clientIp, dstIp , reqList, isBroadcast)