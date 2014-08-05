from fcntl import ioctl
import socket
import struct
 
SIOCGIFMTU = 0x8921
SIOCSIFMTU = 0x8922
 
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
ioctl(s, SIOCGIFMTU, struct.pack('<16sH', 'eth0', 0))
 
mtu = 1280
ioctl(s, SIOCSIFMTU, struct.pack('<16sH', 'eth0', mtu)+'\x00'*14)
