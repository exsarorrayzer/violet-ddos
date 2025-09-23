from colorama import init, Fore

init(autoreset=True)

def set_title(title):
    print(f"\033]0;{title}\007", end="", flush=True)

def color(text, c="blue"):
    colors = {
        "red": Fore.LIGHTRED_EX,
        "green": Fore.LIGHTGREEN_EX,
        "blue": Fore.LIGHTBLUE_EX,
        "yellow": Fore.LIGHTYELLOW_EX,
        "cyan": Fore.LIGHTCYAN_EX,
        "white": Fore.WHITE
    }
    return colors.get(c, Fore.WHITE) + text