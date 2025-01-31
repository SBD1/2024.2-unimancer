import os
import platform
from colorama import Fore, Style
import time
import queries.query as query

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
        

def display_npc_info(npc_nome, npc_tipo, conn):
    descricao = query.get_civilian_info(conn, npc_nome)
    print(Fore.CYAN + "\n--- Ficha do Personagem ---" + Style.RESET_ALL)
    print(Fore.GREEN + f"Nome: {descricao['nome']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Descrição: {descricao['descricao']}" + Style.RESET_ALL)
    print(Fore.MAGENTA + "\n.." + Style.RESET_ALL)
    time.sleep(1)

    if npc_tipo == "Quester":
        get_quest(npc_nome) 
        input("Pressione Enter para continuar...") 
    else:
        print(Fore.RED + f"{npc_nome} não tem nada a dizer." + Style.RESET_ALL)
        print(Fore.MAGENTA + "Pressione 0 para voltar ao menu." + Style.RESET_ALL)
        input()

def get_quest(npc_nome):
    print(f"Você recebeu uma missão de {npc_nome}.")
    # Adicione mais lógica conforme necessário
