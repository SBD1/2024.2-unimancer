DEBUG = False

from colorama import Fore, Style

def error(*args):
    if DEBUG:
        print(Fore.RED + "ERROR: ", *args, Style.RESET_ALL)

def debug(*args):
    
    if DEBUG:
        print(Fore.CYAN + "DEBUG: ", *args, Style.RESET_ALL)