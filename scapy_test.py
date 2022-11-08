from scapy.all import *


def test(src_ip, dest_ip, dest_port):
    packet = IP(src=src_ip, dst=dest_ip) / UDP(dport=dest_port) / Raw(load="abc")

    EtherDA()
    packet.show()
    for i in range(10):
        sendp(packet)


if __name__ == "__main__":
    ip_src = str(sys.argv[1])
    ip_dest = str(sys.argv[2])
    port_dest = int(sys.argv[3])
    test (ip_src, ip_dest,port_dest)
