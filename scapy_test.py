from scapy.all import *


def test(src_ip, dest_ip, dest_port, network_broadcast):
    packet = IP(src=src_ip, dst=dest_ip) / UDP(dport=dest_port) / Raw(load="abc")


    ether_pack = Ether(dst="ff:ff:ff:ff:ff:ff")/Dot1Q(vlan=1)/IP(src=src_ip, dst=dest_ip)/ UDP(dport=dest_port) / Raw(load="cooler_pack")

    
 
    packet.show()
    for i in range(10):
        send(packet)
        sendp(ether_pack)


if __name__ == "__main__":
    ip_src = str(sys.argv[1])
    ip_dest = str(sys.argv[2])
    port_dest = int(sys.argv[3])
    broadcast_ip = str(sys.argv[4])
    test (ip_src, ip_dest,port_dest, broadcast_ip)
