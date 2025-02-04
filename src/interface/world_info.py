from colorama import Fore, Style
import psycopg2
import database.dql.query as query
from logic.character import Character
from typing import List, Tuple

from interface.display import print_center

# Show available subregions and handle navigation 
def display_subregion_info(sub_region: tuple, sub_regions: List[Tuple]):
    print(
        Fore.CYAN +
        "----- Descrição -------" +
        Style.RESET_ALL
    )
    
    name, description = sub_region
    print(
        f"{name} - {description}"
    )
    
    if sub_regions:
        
        print(
            Fore.YELLOW +
            "--- Locais Disponíveis ---" +
            Style.RESET_ALL
        )
        
        for idx, (_, destino, direcao, situacao) in enumerate(sub_regions, start=1):
            print(
                f"{idx}. {destino} ({direcao}) - Situação: {situacao}"
            )

        print()
    

# Display all npcs in that subregion
def display_npcs(npcs: List[Tuple]) -> None:
    if npcs:
        print(
            Fore.YELLOW +
            "--- Pessoas ---" +
            Style.RESET_ALL
        )

        for npc in npcs:
            nome, _, tipo = npc
            print(
                f"{nome} - ({tipo})"
            )
            
        print()

# Display all enemies in that subregion
def display_enemies(enemies: List[Tuple]) -> None:
    if enemies:
        print_center(
            Fore.RED +
            "\n--- Inimigos na Região ---" +
            Style.RESET_ALL
        )
        for idx, enemy in enumerate(enemies, start=1):
            _, name, description, *_ = enemy
            emoji = enemy[12]
            print(
                Fore.RED +
                Style.BRIGHT +
                f"{idx}. " +
                Style.NORMAL +
                f"{emoji} " +
                Style.BRIGHT +
                name +
                Style.NORMAL +
                f" - {description}" +
                Style.RESET_ALL
            )
        print("")

# Display itens
def display_items(items):
    if not any([item[2] > 0 for item in items]):
        return
    
    if items:
        print(Fore.YELLOW + "Itens no chão:" + Style.RESET_ALL)
        for item in items:
            item_id, tipo, quantidade, nome, descricao = item
            print(f"- {nome} (x{quantidade}): {descricao}")
        print()
