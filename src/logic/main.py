from typing import List, Tuple
import interface.display as display
import interface.inventory as inventory
import interface.world_info as world_info
import interface.merchant_interface as merchant
import database.dql.query as query
import logic.combat as combat
from colorama import Fore, Style
from logic.character import Character
import utils

global perceived_subregion
perceived_subregion = False

# Interface/Logic:
#   Ask from the input options and validate it, while running auxiliary function before asking every time.
def ask(options: list, before_func=None, exit_option = True) -> int:
    
    inf_limit = int(not exit_option)
    
    option = -1
    while not (option >= inf_limit and option <= len(options)):
        
        if before_func:
            before_func()

        if exit_option:
            print(
                Style.DIM +
                "--- Para voltar, digite 0 ---" +
                Style.RESET_ALL
            )
            
        option = display.ask_text("Escolha uma opção")
        print(Style.RESET_ALL, end = "")

        try:
            assert option != "", "Digite um número válido!"
            option = int(option)
            assert (option >= inf_limit and option <= len(options)), "Opção inválida entre as disponíveis!"

        except ValueError:
            print("Digite um número válido!")
            option = -1
            display.press_enter()
        except AssertionError as e:
            print(e)
            option = -1
            display.press_enter()
        
    return option

# Logic:
#   Check if the character was perceived by the enemies.
#       True: if the player ran away or won the combat
#       False: if the player died.
def enemies_perception(conn, character : Character, enemies) -> bool:
    
    # Pick the first enemy.
    enemy = combat.Enemy(*(enemies[0]))
    
    # Calculate the perception of the character and the enemy.
    character_perception = combat.perception(character.inteligencia)
    enemy_perception = combat.perception(enemy.inteligencia)

    if (character_perception < enemy_perception):
        global perceived_subregion
        perceived_subregion= True
        print(
            Style.BRIGHT +
            Fore.RED +
            "Você foi Percebido" +
            Style.RESET_ALL
        )
        
        enemies_instances = [combat.Enemy(*enemy) for enemy in enemies]
        enemy_combat = combat.Combat(character, enemies_instances, conn)
        display.press_enter()
        
        result = enemy_combat.init()
        
        if result == None:
            return False
        
        return True
    
    print(
        Style.BRIGHT +
        Fore.GREEN +
        "    Você Passou Sorrateiramente" +
        Style.RESET_ALL
    )
    #display.press_enter()
        
    return True

# Logic:
#
#
# Get all itens from a subregion
def pick_up_items(conn, character: Character, total_items: List[Tuple]) -> None:
    
    items = [item for item in total_items if item[2] > 0]
    
    while True:
        display.clear_screen()
        print(Fore.GREEN + "Itens disponíveis no chão:" + Style.RESET_ALL)
        for idx, (item_id, tipo, quantidade, nome, descricao) in enumerate(items, start=1):
            if quantidade > 0:
                print(f"{idx}. {nome} - x{quantidade}")
        print("0. Voltar")
        
        choice = display.ask_text("Escolha um item para pegar")
        if choice == "0":
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(items):
                item_id, tipo, quantidade, nome, descricao = items[choice - 1]
                if query.can_pick_up_item(conn, character.id):
                    query.transfer_item_to_inventory(conn, character.id, item_id, 1)  # Transfere 1 unidade
                    print(Fore.GREEN + f"Você pegou {nome}." + Style.RESET_ALL)
                    items = query.get_subregion_items(conn, character.sub_regiao_id)
                    return
                else:
                    print(Fore.RED + "Seu inventário está cheio!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Escolha inválida." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Digite um número válido!" + Style.RESET_ALL)
        display.press_enter()

# Logic:
#   Navigate through the subregion the character is.
#   Returns:
#       True: if the player wants to continue navigating.
#       False: if the player died.
def navigate(conn, character: Character) -> bool:
    global perceived_subregion
    
    while True:
        subregion = query.get_subregion_info(conn, character.sub_regiao_id)
        subregions = query.get_subregions_character(conn, character.sub_regiao_id)
        npcs = query.get_citizens_subregion(conn, character.sub_regiao_id)
        enemies = query.get_alive_enemies_subregion(conn, character.sub_regiao_id)
        items = query.get_subregion_items(conn, character.sub_regiao_id)
        
        there_is_at_least_one_item = any(item[2] > 0 for item in items)
        
        if not perceived_subregion and len(enemies) > 0:
            alive = enemies_perception(conn, character, enemies);
            if not alive:
                return False
            continue

        options = []
        if subregions:
            options.append("Caminhar")
        if npcs:
            options.append("Interagir")
        if enemies:
            options.append("Lutar")
        if items and there_is_at_least_one_item:
            options.append("Pegar itens do chão")

        option_i = ask(options, lambda: [
            display.clear_screen(),
            display.header(character),
            world_info.display_subregion_info(subregion, subregions),
            world_info.display_npcs(npcs),
            world_info.display_enemies(enemies),
            world_info.display_items(items),
            display.print_center("O que você deseja fazer agora?"), 
            display.list_options(options)
        ])

        # Go back a menu.
        if option_i == 0:
            return -1

        option = options[option_i - 1]

        if option == "Caminhar":
            direction = ask(subregions, lambda: [
                display.clear_screen(),
                display.list_subregions(subregions)
            ])
            sub_region_id, _, _, status = subregions[direction - 1]
            
            if status == "Passável":
                query.reset_enemies(conn, character.sub_regiao_id)
                character.sub_regiao_id = query.update_character_subregion(conn, character.id, sub_region_id)
                perceived_subregion = False
            else:
                print("\nEssa passagem está bloqueada!")

        elif option == "Interagir":
            npcs = query.get_citizens_subregion(conn, character.sub_regiao_id)

            npc_i = ask(npcs, lambda: [
                display.clear_screen(),
                display.list_npcs(npcs)
            ], False)

            if npc_i == 0:
                return True  

            npc = npcs[npc_i - 1]
            npc_id, npc_nome, npc_tipo, *_ = npc  

            if npc_tipo == "Mercador":
                options = ["Negociar", "Conversar"]
                option_trade = ask(options, lambda: [
                    display.clear_screen(),
                    print(
                        Fore.YELLOW +
                        f"Você encontrou {npc_nome}." +
                        Style.RESET_ALL
                    ),
                    print("O que deseja fazer?"),
                    display.list_options(options)
                ])
                if option_trade == 1:
                    merchant.trade_with_merchant(conn, character)
                else:
                    display.display_npc_info(conn, npc, character.id)
            else:
                display.display_npc_info(conn, npc, character.id)

        elif option == "Lutar": 
            enemies_instances = [combat.Enemy(*enemy) for enemy in enemies]
            combat_instance = combat.Combat(character, enemies_instances, conn)
            alive = combat_instance.init()
            if not alive:
                return False

        elif option == "Pegar itens do chão":
            pick_up_items(conn, character, items)  # pick up ites (update!!!)
    return True

# Interface/Logic:
#   Show in-game options.
def game(conn, character: Character) -> bool:
    options = [
        "Navegar",
        "Ver status do personagem",
        "Ver inventário",
        "Ver feitiços"
    ]
    option_i = ask(options, lambda: [
        display.clear_screen(),
        display.header(character),
        display.ingame_menu(),
        display.list_options(options)
    ])

    # Go back one menu.
    if option_i == 0:
        return 0
    
    option = options[option_i - 1]
        
    if option == "Navegar":
        result = navigate(conn, character)
        if not result:
            return False
    elif option == "Ver status do personagem":
        display.clear_screen()
        display.header(character, complete=True)
        display.press_enter()
    elif option == "Ver inventário":
        display.clear_screen()
        inventory.list_items(character, conn)
        display.press_enter()
    elif option == "Ver feitiços":
        display.clear_screen()
        spells = query.get_damage_spells(conn, character.id) + query.get_damage_area_spells(conn, character.id) + query.get_healing_spells(conn, character.id)
        inventory.list_spells(spells)
        display.press_enter()

    elif option == "Sair":
        print("Saindo do jogo/ir para menu principal.")
        display.press_enter()
        return False
    
    return True


# Interface/Logic:
#   Show main menu (before game starts).
def main_menu(conn) -> int:
    
    options = [
        "Listar personagens",
        "Criar personagem"
    ]
    
    # Get an option.
    option_i = ask(options, lambda: [
        display.clear_screen(),
        display.show_title(),
        display.list_options(options)
    ])
    
    # Go back one menu.
    if option_i == 0:
        return -1
    
    option = options[option_i - 1]

    
    character = None
    

    if option == "Listar personagens":

        characters = query.list_all_characters(conn)
        
        if not characters:
            display.clear_screen()
            print(Fore.RED + "Nenhum personagem encontrado" + Style.RESET_ALL)
            display.press_enter()
            return 0
        else:
            character_i = ask(characters, lambda: [
                display.clear_screen(),
                display.list_characters(characters)
            ])
            
            # If a character was not selected.
            if character_i == 0:
                return 0
            
            character_id = characters[character_i - 1][0]
            
            character = Character(conn, character_id)
            utils.debug(f"Personagem {character.nome} selecionado com sucesso!")
            display.press_enter()


    if option == "Criar personagem": 
        character = Character(conn)
        
        # If character was not created.
        if character.nome == "":
            return 0

        character.define_initial_spells(conn)
        character.add_initial_items(conn)
        utils.debug(f"Personagem {character.nome} criado com sucesso!")
        display.press_enter()


    return character