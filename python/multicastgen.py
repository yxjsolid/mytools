##Author: Codey Shriner
##Date: 11-15-2012
##Copyright: Codey Shriner


##Import modules
##------------------------
import sys
import socket
import binascii
import os
from time import sleep
##-------------------------


os.system('cls')		##Clear screen before running


##Instantiate variables
##-----------------------------------------------------------------
strIP="225.1.1.1"		##Multicast (destination) IP to which data will be sent
intPort="8194"			##UDP port pair with the destination IP
strData=binascii.unhexlify('280000006d08000003f49451016f4e1531000000000401460800000000000001005e010548000001')  ##Data to send to multicast address
strData=binascii.unhexlify('280000006d08000003f49451016f4e1531000000000401460800000000000001005e010548000001')
intSleepTime=100		##The script will wait for X milliseconds before next packet is sent; the default is 100ms.
intTTL=5				##IP header TTL
intPacketCount=0		##Basic counter of packets sent
strStdOut=""			##Used to send messages to stdout
##-----------------------------------------------------------------

def genData(len):
    num_inc_list = range(256)
    
    if len%256 > 0:
        num = len/256 + 1
    else:
        num = len/256  
    #sample_list = [num_inc_list]*i
    #sample_list =  sample_list[:2]
        
    sample_list = [num_inc_list for i in range(num)]   
    
    ret = []
    
    for elem in sample_list:
         ret += elem  
        
        
    ret =  ret[:len]
    
    print ret
    
    retstr = ""
    
    for elem in ret:
        #retstr += "%02x" % hex(elem).strip('0x')
        
        retstr += "%02x" % elem
        
        #print binascii.unhexlify(str(bin(elem)))
    print retstr
    
    datar = binascii.unhexlify(retstr)
    print "%r" % datar
    return datar

##Stdin
##----------------------------------------------------------------------------------
##strIP = str(raw_input('Enter the destination IP: '))
##os.system('cls')
##
##intPort = int(raw_input('Enter the destination port number: '))
##os.system('cls')
##
##strData=binascii.unhexlify(str(raw_input('Enter the packet payload in Hex: ')))
##os.system('cls')

##print 'Generating Multicast packets, and sending them on port ' + str(intPort) + ' to IP ' + strIP + '...'
##----------------------------------------------------------------------------------


##Work
##-----------------------------------------------------------------
intSleepTime = intSleepTime *0.001	##The script will wait for X milliseconds before next packet is sent. Modify intSleepTime in variables section to increase/decrease.

strData = genData(1500)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)					##Create socket
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, intTTL)		##Socket type is Multicast
sock.bind()


while True:
  try:
    sock.sendto (strData, (strIP, int(intPort)))			##Send packets
    intPacketCount = intPacketCount + 1						##Increment packet counter
    strStdOut = "Packets Sent: " + str(intPacketCount)		##Stdout message
    sys.stdout.write(strStdOut + '\x08'*len(strStdOut))		##Update stdout
    sleep(intSleepTime)										##Wait before sending next packet

  except KeyboardInterrupt:									##On Ctrl+C, print new line and break
    ##os.system('cls')
    print '\x0D'
    break
##-----------------------------------------------------------------


