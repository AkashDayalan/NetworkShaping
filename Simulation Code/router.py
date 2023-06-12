import socket
import struct
import time
from ctypes import *
from queue import Queue
from threading import Thread
import threading
import datetime
import openpyxl

NUM_INGRESS_QUEUES = 8
NUM_EGRESS_QUEUES = 8

# Initialize socket
sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_receive.bind(('127.0.0.1', 8889))

# Initialize the socket
sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Destination host information
dest_addr = ("127.0.0.1", 8895)

# global pkt_loss
# global num_of_packets_sent

# pkt_loss = 0
# num_of_packets_sent = 0

# class Packet:
#     def __init__(self, src_id, dest_id, type, buffer):
#         self.src_id = src_id
#         self.dest_id = dest_id
#         self.type = type
#         self.length = len(buffer)
#         self.buffer = buffer

class Packet:
    def __init__(self):
        self.src_id = ""
        self.dest_id = ""
        self.type = ""
        self.length = 0
        self.buffer = bytearray(4096)


def create_queue(capacity):
    return {
        'data': [None] * capacity,
        'front': 0,
        'rear': capacity - 1,
        'size': 0,
        'capacity': capacity,
    }

def enqueue(q, pkt):
    if q['size'] == q['capacity']:
        # pkt_loss = pkt_loss + 1
        print("Queue is full")
        return 1

    q['rear'] = (q['rear'] + 1) % q['capacity']
    q['data'][q['rear']] = pkt
    q['size'] += 1
    return 0

def dequeue(q):
    if q['size'] == 0:
        print("Queue is empty")
        # Return an empty packet
        return Packet()

    pkt = q['data'][q['front']]
    q['front'] = (q['front'] + 1) % q['capacity']
    q['size'] -= 1
    return pkt

# Ingress queues
ingress_queues = [create_queue(10000) for _ in range(NUM_INGRESS_QUEUES)]
egress_queues = [create_queue(10000) for _ in range(NUM_EGRESS_QUEUES)]

def handle_incoming_packets():
    # global final_sock
    # current_hour = datetime.datetime.now().hour
    # test_count = 0
    q1_pkt_loss = 0
    q2_pkt_loss = 0
    q3_pkt_loss = 0
    q4_pkt_loss = 0
    q5_pkt_loss = 0
    q6_pkt_loss = 0
    q7_pkt_loss = 0
    q8_pkt_loss = 0
    pkt_received = 0
    t1_pkt_received = 0
    t2_pkt_received = 0
    t3_pkt_received = 0
    t4_pkt_received = 0
    t5_pkt_received = 0
    t6_pkt_received = 0
    t7_pkt_received = 0
    t8_pkt_received = 0
    time_counter = 0
    flag = False
    while True:
        pkt = Packet()

        # Receive packet
        pkt_bytes, src_addr = sock_receive.recvfrom(struct.calcsize("32s 32s 16s I 4096s"))
        pkt_received = pkt_received+1
        pkt_data = struct.unpack("32s 32s 16s I 4096s", pkt_bytes)
        pkt.src_id = pkt_data[0].decode().rstrip('\0')
        pkt.dest_id = pkt_data[1].decode().rstrip('\0')
        pkt.type = pkt_data[2].decode().rstrip('\0')
        pkt.length = pkt_data[3]
        pkt.buffer[:pkt.length] = pkt_data[4][:pkt.length]
        print(f"Packet received from {src_addr[0]}, src host: {pkt.src_id}, type: {pkt.type}, length: {pkt.length}, buffer: {pkt.buffer[:pkt.length]}")


        if pkt.type == "T1":
            t1_pkt_received = t1_pkt_received + 1
            q1_pkt_loss = q1_pkt_loss + enqueue(ingress_queues[0], pkt)
            # print("\nIngress queue 0 size : " + str(ingress_queues[0]['size']) + "\n")
        elif pkt.type == "T2":
            t2_pkt_received = t2_pkt_received + 1
            q2_pkt_loss = q2_pkt_loss + enqueue(ingress_queues[1], pkt)
            # print("\nIngress queue 1 size : " + str(ingress_queues[1]['size']) + "\n")
        elif pkt.type == "T3":
            t3_pkt_received = t3_pkt_received + 1
            q3_pkt_loss = q3_pkt_loss + enqueue(ingress_queues[2], pkt)
            # print("\nIngress queue 2 size : " + str(ingress_queues[2]['size']) + "\n")
        elif pkt.type == "T4":
            t4_pkt_received = t4_pkt_received + 1
            q4_pkt_loss = q4_pkt_loss + enqueue(ingress_queues[3], pkt)
            # print("\nIngress queue 3 size : " + str(ingress_queues[3]['size']) + "\n")
        elif pkt.type == "T5":
            t5_pkt_received = t5_pkt_received + 1
            q5_pkt_loss = q5_pkt_loss + enqueue(ingress_queues[4], pkt)
            # print("\nIngress queue 4 size : " + str(ingress_queues[4]['size']) + "\n")
        elif pkt.type == "T6":
            t6_pkt_received = t6_pkt_received + 1
            q6_pkt_loss = q6_pkt_loss + enqueue(ingress_queues[5], pkt)
            # print("\nIngress queue 5 size : " + str(ingress_queues[5]['size']) + "\n")
        elif pkt.type == "T7":
            t7_pkt_received = t7_pkt_received + 1
            q7_pkt_loss = q7_pkt_loss + enqueue(ingress_queues[6], pkt)
            # print("\nIngress queue 6 size : " + str(ingress_queues[6]['size']) + "\n")
        elif pkt.type == "T8":
            t8_pkt_received = t8_pkt_received + 1
            q8_pkt_loss = q8_pkt_loss + enqueue(ingress_queues[7], pkt)
            # print("\nIngress queue 7 size : " + str(ingress_queues[7]['size']) + "\n")
        else:
            print(f"Unknown packet type: {pkt.type}")
        
        if datetime.datetime.now().minute%2 == 0:
            if not flag:
                time_counter = time_counter+1
                workbook = openpyxl.load_workbook('example.xlsx')
                sheet = workbook['Sheet1']
                # timestamp = datetime.timestamp(datetime.datetime.now())
                new_row = [time_counter, datetime.datetime.now().minute, datetime.datetime.timestamp(datetime.datetime.now()), ingress_queues[0]['size'], ingress_queues[1]['size'], ingress_queues[2]['size'], ingress_queues[3]['size'], ingress_queues[4]['size'], ingress_queues[5]['size'], ingress_queues[6]['size'], ingress_queues[7]['size'], pkt_received, q1_pkt_loss, q2_pkt_loss, q3_pkt_loss, q4_pkt_loss, q5_pkt_loss, q6_pkt_loss, q7_pkt_loss, q8_pkt_loss, t1_pkt_received, t2_pkt_received, t3_pkt_received, t4_pkt_received, t5_pkt_received, t6_pkt_received, t7_pkt_received, t8_pkt_received]
                sheet.append(new_row)
                workbook.save('example.xlsx')
                flag = True
                q1_pkt_loss = 0
                q2_pkt_loss = 0
                q3_pkt_loss = 0
                q4_pkt_loss = 0
                q5_pkt_loss = 0
                q6_pkt_loss = 0
                q7_pkt_loss = 0
                q8_pkt_loss = 0
        else:
            flag = False
            # time.sleep(59)
            


def handle_egress_packets():
    while True:
        for i in range(0,8):
            if(ingress_queues[i]['size'] > 0):
                pkt = Packet()
                pkt = dequeue(ingress_queues[i])
                enqueue(egress_queues[i], pkt)
                # print("\nEgress queue size " + str(i+1) + str(":\t") + str(egress_queues[i]['size']) + "\n")
                # print(pkt.src_id)
        time.sleep(0.05)
        # time.sleep(0.09)
        # time.sleep(0.12)
        # time.sleep(0.20)
        # time.sleep(0.20)

def egress_destination_packets():
    num_of_packets_sent = 0
    # flag = False
    while True:
        for i in range(0, 8):
            if(egress_queues[i]['size'] > 0):
                pkt = Packet()
                pkt = dequeue(egress_queues[i])

                # print(pkt.src_id)
                
                src = pkt.src_id.encode()
                dest = pkt.dest_id.encode()
                pkttype = pkt.type.encode()
                length = pkt.length
                buffer = pkt.buffer

                # Convert the packet to a bytes object
                pkt_bytes = struct.pack("32s32s16si4096s", src, dest, pkttype, length, buffer)

                # Send the packet
                bytes_sent = sock_send.sendto(pkt_bytes, dest_addr)
                if(bytes_sent == 0):
                    print("Error sending packet")
                else:
                    num_of_packets_sent = num_of_packets_sent+1
                    print("Number of packets sent: ", num_of_packets_sent)
                    # print("Packet Loss: ", pkt_loss)
                    print("Packet sent successfully, bytes sent: ", bytes_sent)
        # if datetime.datetime.now().minute%2 == 0:
        #     if not flag:
        #         workbook = openpyxl.load_workbook('example.xlsx')
        #         sheet = workbook['Sheet']
        #         new_row = [num_of_packets_sent]
        #         sheet.append(new_row)
        #         workbook.save('example.xlsx')
        #         flag = True
        # else:
        #     flag = False

        # time.sleep(0.25)



def main():
    # Initialize Winsock
    # WSAStartup(MAKEWORD(2, 2), byref(WSADATA()))

    #test
    # pkt = Packet()
    # pkt.src_id = "S1"
    # pkt.dest_id = "D1"
    # pkt.type = "T1"
    # pkt.length = 10
    # pkt.buffer = "Data".encode()

    # for i in range(0, 10000):
    #     enqueue(ingress_queues[0], pkt)

    handle_thread1 = threading.Thread(target=handle_incoming_packets)
    handle_thread2 = threading.Thread(target=handle_egress_packets)
    handle_thread3 = threading.Thread(target=egress_destination_packets)
    handle_thread1.start()
    handle_thread2.start()
    # time.sleep(0.02)
    handle_thread3.start()


if __name__ == '__main__':
    main()