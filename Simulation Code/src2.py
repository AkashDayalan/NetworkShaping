import socket
import struct
import time
import random
import sys

# Define the packet structure
class Packet:
    def __init__(self, src_id, dest_id, type_, length, buffer):
        self.src_id = src_id.encode()
        self.dest_id = dest_id.encode()
        self.type = type_.encode()
        self.length = length
        self.buffer = buffer.encode()

if __name__ == '__main__':

    params = [float(p) if '.' in p else int(p) for p in sys.argv[1:]]
    # print(params)

    destinations = ["D1", "D2", "D3"]
    types = ["T1","T2","T3","T4","T5","T6","T7","T8"]

    # Initialize the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # # Build the packet
    # pkt = Packet("Source Host1", "D1", "T1", 10, "Data")

    # Destination host information
    dest_addr = ("127.0.0.1", 8888)

    while(True):

        # Build the packet
        # pkt = Packet("Source Host1", random.choice(destinations), random.choice(types), 10, "Data")
        pkt = Packet("Source Host1", random.choice(destinations), "T2", 10, "Data")

        # Convert the packet to a bytes object
        pkt_bytes = struct.pack("32s32s16si4096s", pkt.src_id, pkt.dest_id, pkt.type, pkt.length, pkt.buffer)

        # Send the packet
        bytes_sent = sock.sendto(pkt_bytes, dest_addr)
        if bytes_sent == 0:
            print("Error sending packet")
        else:
            print("Packet sent successfully, bytes sent: ", bytes_sent)

        # time.sleep(0.07) #ideal
        time.sleep(params[0])

    # Cleanup
    sock.close()