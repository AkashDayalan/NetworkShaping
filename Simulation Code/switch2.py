import socket
import struct
import time

class Packet:
    def __init__(self, src_id, dest_id, type, buffer):
        self.src_id = src_id
        self.dest_id = dest_id
        self.type = type
        self.length = len(buffer)
        self.buffer = buffer

def main():
    # Initialize socket
    sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_receive.bind(('127.0.0.1', 8895))
    
    # Initialize the socket
    sock1_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock2_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock3_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    

    # Destination host information
    dest1_addr = ("127.0.0.1", 8890)
    dest2_addr = ("127.0.0.1", 8891)
    dest3_addr = ("127.0.0.1", 8892)


    num_packets = 0

    # Receive packets
    while True:
        data, address = sock_receive.recvfrom(8192)
        pkt = struct.unpack('32s32s16si4096s', data)
        num_packets += 1

        print("Packet received from {}, bytes received: {}".format(address[0], len(data)))
        print("src_id: {}".format(pkt[0].decode().strip('\x00')))
        print("dest_id: {}".format(pkt[1].decode().strip('\x00')))
        print("type: {}".format(pkt[2].decode().strip('\x00')))
        print("length: {}".format(pkt[3]))
        print("buffer: {}".format(pkt[4].decode().strip('\x00')))
        print("Packets received: {}\n".format(num_packets))

        # Convert the packet to a bytes object
        pkt_bytes = struct.pack("32s32s16si4096s", pkt[0], pkt[1], pkt[2], pkt[3], pkt[4])

        dest = pkt[1].decode().strip('\x00')

        if(dest == 'D1'):
        # Send the packet
            bytes_sent = sock1_send.sendto(pkt_bytes, dest1_addr)
            if bytes_sent == 0:
                print("Error sending packet")
            else:
                print("Packet sent successfully, bytes sent: ", bytes_sent)
        elif(dest == 'D2'):
        # Send the packet
            bytes_sent = sock2_send.sendto(pkt_bytes, dest2_addr)
            if bytes_sent == 0:
                print("Error sending packet")
            else:
                print("Packet sent successfully, bytes sent: ", bytes_sent)
        elif(dest == 'D3'):
        # Send the packet
            bytes_sent = sock3_send.sendto(pkt_bytes, dest3_addr)
            if bytes_sent == 0:
                print("Error sending packet")
            else:
                print("Packet sent successfully, bytes sent: ", bytes_sent)

if __name__ == '__main__':
    main()