from typing import List
import os
import platform
from colorama import Fore, Style
import time

from numpy import add

from logic.enemy import Enemy
from logic.quest import Quest
from database.dql.query import get_quest, get_civilian_info

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

def display_npc_info(conn, npc):
   quest_instance = Quest()
   npc_nome = npc[0]
   npc_tipo = npc[2]
   descricao = get_civilian_info(conn, npc_nome)
   print(Fore.CYAN + "\n--- Ficha do Personagem ---" + Style.RESET_ALL)
   print(Fore.GREEN + f"Nome: {descricao['nome']}" + Style.RESET_ALL)
   print(Fore.GREEN + f"Descrição: {descricao['descricao']}" + Style.RESET_ALL)
   print(Fore.MAGENTA + "\n.." + Style.RESET_ALL)
   time.sleep(1)

   if npc_tipo == "Quester":
       print(Fore.GREEN + f"{npc_nome} tem uma missão para você." + Style.RESET_ALL)
       input("Pressione Enter para continuar...") 
       quest_instance.show_quest(conn, npc_nome, descricao['npc_id'])
   else:
       print(Fore.RED + f"{npc_nome} não tem nada a dizer." + Style.RESET_ALL)
       print(Fore.MAGENTA + "Pressione 0 para voltar ao menu." + Style.RESET_ALL)
       input()

def list_subregions(subregions) -> None:
    print(Fore.CYAN + "\n--- Sub-regiões disponíveis ---" + Style.RESET_ALL)
    for idx, subregion in enumerate(subregions, start=1):
        print(f"\n {idx}.  {subregion[1]} - {subregion[2]}")
        
# Interface:
#   A character was perceveid by an enemy and now has to fight.
def enemy_perceives(enemy):
    print(f"{Style.BRIGHT}{Fore.RED}Você foi Percebido por {enemy.nome}" + Style.RESET_ALL)
    
#def display_npc_info(npc, conn):
#    npc_nome, npc_tipo = npc
#    descricao = query.get_civilian_info(conn, npc_nome)
#    print(Fore.CYAN + "\n--- Ficha do Personagem ---" + Style.RESET_ALL)
#    print(Fore.GREEN + f"Nome: {descricao['nome']}" + Style.RESET_ALL)
#    print(Fore.GREEN + f"Descrição: {descricao['descricao']}" + Style.RESET_ALL)
#    print(Fore.MAGENTA + "\n.." + Style.RESET_ALL)
#    time.sleep(1)
#
#    if npc_tipo == "Quester":
#        show_quest(conn, npc_nome, descricao['npc_id'], character)
#        input("Pressione Enter para continuar...") 
#    else:
#        print(Fore.RED + f"{npc_nome} não tem nada a dizer." + Style.RESET_ALL)
#        print(Fore.MAGENTA + "Pressione 0 para voltar ao menu." + Style.RESET_ALL)
#        input()

# Interface:
#   Will show the information of the quest.
#def show_quest(conn, npc_name, npc_id, character):
#    quest = get_quest(conn, npc_id)
#    print(Fore.CYAN + f"\n Missão: {quest['title']}" + Style.RESET_ALL)
#    print(Fore.CYAN + f"{quest['description']}" + Style.RESET_ALL)
#    print('..')
#    time.sleep(1)
#    for line in quest['dialog'].split('\n'):
#        print(f"{npc_name} diz: {line}")
#        input("Pressione Enter para continuar...")
#    
#    accept_quest(conn, character.id, quest['quest_id'])
#    
#    print(Fore.GREEN + "\n--- COMPLETE A MISSÃO ---" + Style.RESET_ALL)
#    print(Fore.YELLOW + f"Descrição: {quest['description']}" + Style.RESET_ALL)
#    print(Fore.YELLOW + f"Recompensa: {quest['reward']}" + Style.RESET_ALL)
#    print(Fore.MAGENTA + "Pressione Enter para continuar..." + Style.RESET_ALL)
#    input()

# Interface:
#   Will list the NPCs available in the subregion.
def list_npcs(npcs) -> None:
    print("\nNPCs disponíveis:")
    for idx, npc in enumerate(npcs, start=1):
        name, description, function = npc
        print(f"\n {idx}.  {name} - {function} - {description}")
        
# Interface:
#   Will list the spells available to the character.
def list_spells(spells) -> None:
    for idx, spell in enumerate(spells):
        print(f"{idx+1}. {spell}")

# Print all enemies and their description and life.
def interface_show_enemies(enemies: List[Enemy]) -> None:
    for idx, enemy in enumerate(enemies):
        print(f"| {idx+1} - {enemy.nome} - {enemy.descricao} - {enemy.vida}/{enemy.vida_maxima} |")