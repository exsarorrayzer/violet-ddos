from colorama import init, Fore, Style
import os
import platform

init(autoreset=True)

def set_title(title: str):
    if platform.system() == "Windows":
        os.system(f"title {title}")
    else:
        print(f"\033]0;{title}\007", end="", flush=True)

def color(text: str, c: str = "blue") -> str:
    colors = {
        "red": Fore.LIGHTRED_EX,
        "green": Fore.LIGHTGREEN_EX,
        "blue": Fore.LIGHTBLUE_EX,
        "yellow": Fore.LIGHTYELLOW_EX,
        "cyan": Fore.LIGHTCYAN_EX,
        "white": Fore.WHITE
    }
    return colors.get(c, Fore.WHITE) + text + Style.RESET_ALL