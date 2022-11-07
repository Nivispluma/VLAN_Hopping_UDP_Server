from scapy.all import *

packet =Ether(dst="ff:ff:ff:ff:ff:ff")/\
        Dot1Q(vlan=1)/\
        Dot1Q(vlan=2)/\
        Dot1Q(vlan=2)/\
        IP(src="169.254.60.173", dst="192.168.178.61")/\
        UDP(dport=50500)/\
        Raw(load="abc") 


EtherDA()
packet.show()
for i in range(10):
    sendp(packet)