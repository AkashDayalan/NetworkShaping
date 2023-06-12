import socket
import struct

class Packet:
    def __init__(self, src_id, dest_id, type, buffer):
        self.src_id = src_id
        self.dest_id = dest_id
        self.type = type
        self.length = len(buffer)
        self.buffer = buffer

def main():
    # Initialize socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 8891))
    
    num_packets = 0

    # Receive packets
    while True:
        data, address = sock.recvfrom(8192)
        pkt = struct.unpack('32s32s16si4096s', data)
        num_packets += 1

        print("Packet received from {}, bytes received: {}".format(address[0], len(data)))
        print("src_id: {}".format(pkt[0].decode().strip('\x00')))
        print("dest_id: {}".format(pkt[1].decode().strip('\x00')))
        print("type: {}".format(pkt[2].decode().strip('\x00')))
        print("length: {}".format(pkt[3]))
        print("buffer: {}".format(pkt[4].decode().strip('\x00')))
        print("Packets received: {}\n".format(num_packets))

if __name__ == '__main__':
    main()