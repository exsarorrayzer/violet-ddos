import random

proxies = []

def load_proxies(path="proxy.txt"):
    global proxies
    try:                                                                        with open(path, "r") as file:
            proxies = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        proxies = []

def get_random_proxy():
    global proxies
    if not proxies:                                                             return None                                                         return random.choice(proxies)

def remove_proxy(proxy):
    global proxies
    try:
        proxies.remove(proxy)
    except ValueError:
        pass
