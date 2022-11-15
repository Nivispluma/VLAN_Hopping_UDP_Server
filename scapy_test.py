from scapy.all import *


def test(src_ip, dest_ip, dest_port, network_broadcast):
    packet =IP(src=src_ip, dst=dest_ip)/UDP(dport=dest_port)/Raw(load="Layer 3 Packet")


# # Dot1Q(vlan=1)/\
    # working layer 2 packet
    #reference_layer_2 =Ether(src="aa:bb:cc:dd:ff:ee", dst="ff:ff:ff:ff:ff:ff")/IP(src=src_ip, dst=dest_ip)/UDP(dport=dest_port) /Raw(load="Standard Layer 2 Packet")
    test_layer_2 = Ether(src="40:b0:34:40:e7:af", dst="ff:ff:ff:ff:ff:ff")/Dot1Q(vlan=1)/Dot1Q(vlan=2)/IP(src=src_ip, dst=dest_ip)/UDP(dport=dest_port)/Raw(load="Test Layer 2 Packet")
    test_icmp = Ether(src="40:b0:34:40:e7:af", dst="ff:ff:ff:ff:ff:ff")/Dot1Q(vlan=1)/Dot1Q(vlan=2)/Dot1Q(vlan=2)/IP(src=src_ip, dst=dest_ip)/ICMP()

    packet.show()
    for i in range(3):
        print("-------------------------------------------")
        print("Layer 3")
        send(packet)
        print("Layer 2 - Referenz")
        # sendp(reference_layer_2)
        print("Layer 2 - Test")
        sendp(test_layer_2)
        print("Layer 2 - ICMP")
        sendp(test_icmp)
        print("-------------------------------------------")


# Usage
# sudo python scapy_test.py 192.168.1.37 192.168.1.33 50500 192.168.1.255

if __name__ == "__main__":
    ip_src = str(sys.argv[1])
    ip_dest = str(sys.argv[2])
    port_dest = int(sys.argv[3])
    broadcast_ip = str(sys.argv[4])
    test (ip_src, ip_dest,port_dest, broadcast_ip)
