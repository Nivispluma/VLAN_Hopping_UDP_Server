from scapy.all import *


def test(src_ip, dest_ip, dest_port, network_broadcast):
    packet =IP(src=src_ip, dst=dest_ip)/UDP(dport=dest_port)/Raw(load="Layer 3 Packet")


# # Dot1Q(vlan=1)/\
    # working layer 2 packet
    ether_pack =Ether(src="aa:bb:cc:dd:ff:ee", dst="ff:ff:ff:ff:ff:ff")/IP(src=src_ip, dst=dest_ip)/UDP(dport=dest_port) /Raw(load="Standard Layer 2 Packet")

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
