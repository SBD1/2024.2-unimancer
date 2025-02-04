from typing import List
import os
import platform
from colorama import Back, Fore, Style
import time

from logic.enemy import Enemy
from logic.quest import Quest
from database.dql.query import get_quest, get_civilian_info
from logic.character import Character


# Ask for a text.
def ask_text(message: str) -> str:
    return input(
        message +
        ": " +
        Style.BRIGHT
    )

# Clean the terminal screen
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Show the title of the game
def show_title():
    print_center("")
    print(Style.BRIGHT + Fore.BLUE)
    print_center("            .:-----:.              ", reset = False)
    print_center("           :'   |   ':             ", reset = False)
    print_center("   :':     :  .d'b.  :     .:'.    ", reset = False)
    print_center("  :   :   _.,d  . b,._    :   :    ", reset = False)
    print_center("   ':.' .d''           ``b. ':.'   ", reset = False)
    print_center("      .p'      .         `q.       ", reset = False)
    print_center("   ..d'   .         .      'b..    ", reset = False)
    print_center(" .d'___________________________'b. ", reset = False)
    print_center(":::::::::::::::::::::::::::::::::::", reset = False)
    print_center("    `p.     .pq.    .pq.    .q'    ", reset = False)
    print_center("    `p.     .pq.    .pq.    .q'    ", reset = False)
    print_center("     `p.     ..      ..    .q'     ", reset = False)
    print_center("      `b.                 .d'      ", reset = False)
    print_center("        `q..            ..,'       ", reset = False)
    print_center("           '',,,,,,,,,,''          ", reset = False)
    print_center("")
    print(Style.BRIGHT + Fore.YELLOW)
    print_center(
        "--- Bem-vindo ao Unimancer! ---"
    )

# Show in-game menu.
def ingame_menu() -> None:
    print(
        Fore.CYAN +
        "--- Menu Principal ---" +
        Style.RESET_ALL
    )

# Press Enter to continue.
def press_enter() -> None:
    input("\nPressione Enter para continuar...")

# List simple options.
def list_options(options: list) -> None:
    for idx, option in enumerate(options, start=1):
        print(
            Style.BRIGHT +
            f"{idx}." +
            Style.NORMAL +
            f" {option}")

# List characters' info.
def list_characters(characters: list) -> None:
    print("\nPersonagens disponíveis:")
    for idx, character in enumerate(characters, start=1):
        print(f"\n {idx}.  {character[1]} - {character[2]}") 

def display_npc_info(conn, npc, character_id):
   quest_instance = Quest(conn)
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
       quest_instance.show_quest(npc_nome, descricao['npc_id'], character_id)
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


# Return the terminal columns.
def terminal_width() -> None:
    return os.get_terminal_size().columns

def print_center(text: str, width = terminal_width(), reset = True) -> None:
    print(
        text.center(width) +
        (Style.RESET_ALL if reset else "")
    )
    
def print_terminal_width(character: str) -> None:
    print(
        character * terminal_width() +
        Style.RESET_ALL
    )

# Displays a bar with the character's life and energy.
def header(character: Character, complete = False) -> None:
    spacing = "  "
    emoji_size = 10 # bytes of ASCII encoding of an emoji
        
    def label(field: str, value: str, column = 0, larger = False) -> str:
        field_column = f"{field:<4}" if column else field
        if larger:
            field_column = f"{field:<3}" if column else field
            

        return "".join([
            field_column,
            " : ",
            Style.BRIGHT,
            value,
            Style.NORMAL
        ])
        
    if complete:
        print(Style.BRIGHT)
        
        elements = {
            "Fogo": "🔥",
            "Água": "💧",
            "Terra": "🌿",
            "Ar": "💨",
            "Luz": "☀️",
            "Trevas": "🌑"
        }
        
        nome = '       ' + character.nome + '    '
        life = label("🫀", f"{character.vida}/{character.vida_maxima}", True)
        energy = label("🌀", f"{character.energia_arcana}/{character.energia_arcana_maxima}", True, True)
        coins = label("🪙", f"{character.moedas}", True)
        xp = label("✨", f"{character.xp}/{character.xp_total}", True, True)
        element = label(elements[character.elemento], character.elemento, True, True)
        knowledge = label("📚", f"{character.conhecimento_arcano}", True, True)
        intelligence = label("🧠", f"{character.inteligencia}", True, True)
        level = label("💪", f"{character.nivel}", True, True)
        
        print_center(f"{nome:<30}")
        print()
        print_center(f"{life:<30}")
        print_center(f"{energy:<30}")
        print_center(f"{coins:<30}")
        print_center(f"{xp:<30}")
        print_center(f"{element:<30}")
        print_center(f"{knowledge:<30}")
        print_center(f"{intelligence:<30}")
        print_center(f"{level:<30}")
        
    else:
        
        life = label("🫀", f"{character.vida}/{character.vida_maxima}")
        energy = label("🌀", f"{character.energia_arcana}/{character.energia_arcana_maxima}")
        coins = label("🪙", f"{character.moedas}")
        xp = label("✨", f"{character.xp}/{character.xp_total}")
    
        line = (
            Fore.BLUE +
            spacing +
            Style.BRIGHT +
            f"{character.nome} {spacing}" +
            Style.NORMAL +
            life +
            spacing +
            energy +
            spacing +
            coins +
            spacing +
            xp +
            spacing
        )
        
        emojis_size = emoji_size * 4
        print()
        print_center(line, width=terminal_width() + emojis_size)
        
    

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
        if enemy.vida > 0:
            print(f"| {idx+1} - {enemy.emoji} - {enemy.nome} - {enemy.descricao} - {enemy.vida}/{enemy.vida_maxima} |")
            