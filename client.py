import socket
import sys

def udp_client(ip, port): 
    msgFromClient       = "Hello UDP Server"
    bytesToSend         = str.encode(msgFromClient)
    serverAddressPort   = (ip, port)
    bufferSize          = 1024

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    

    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)


# start from command line with: python client.py <server ip> <server port>
# python client.py 192.168.178.2 50000

if __name__ == "__main__":
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    udp_client(ip, port)