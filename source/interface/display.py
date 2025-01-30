import os
import platform
from colorama import Fore, Style

# Clean the terminal screen
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Show the title of the game
def show_title():
    print("")
    print(" ██╗   ██╗███╗   ██╗██╗███╗   ███╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ ")
    print(" ██║   ██║████╗  ██║██║████╗ ████║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗")
    print(" ██║   ██║██╔██╗ ██║██║██╔████╔██║███████║██╔██╗ ██║██║     █████╗  ██████╔╝")
    print(" ██║   ██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗")
    print(" ╚██████╔╝██║ ╚████║██║██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╗███████╗██║  ██║")
    print("  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝")
    print("")
    print(Style.BRIGHT + Fore.YELLOW + "\n--- Bem-vindo ao Unimancer! ---" + Style.RESET_ALL)

# Show in-game menu.
def ingame_menu() -> None:
    print(Fore.CYAN + "\n--- Menu Principal ---" + Style.RESET_ALL)

# Press Enter to continue.
def press_enter() -> None:
    input("\nPressione Enter para continuar...")

# List simple options.
def list_options(options: list) -> None:
    for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

# List characters' info.
def list_characters(characters: list) -> None:
    print("\nPersonagens disponíveis:")
    for idx, character in enumerate(characters, start=1):
        print(f"\n {idx}.  {character[1]} - {character[2]}") 