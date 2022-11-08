import socket
import sys
 
def udp_server(localIP,localPort):
    # localIP     = "127.0.0.1"
    # localPort   = 20001
    bufferSize  = 1024


    msgFromServer       = "Hello UDP Client"
    bytesToSend         = str.encode(msgFromServer)

    
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip

    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    # Listen for incoming datagrams

    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print()
        print(clientMsg)
        print(clientIP)

        # Sending a reply to client

        UDPServerSocket.sendto(bytesToSend, address)


# start from command line with: python main.py <server ip> <port>
# python main.py 192.168.178.61 50500

if __name__ == "__main__":
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    udp_server(ip, port)