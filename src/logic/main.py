import interface.display as display
import interface.inventory as inventory
import interface.world_info as world_info
import database.dql.query as query
import logic.combat as combat
from colorama import Fore, Style
from logic.character import Character
import utils

global perceived_subregion

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
            
        option = input("Escolha uma opção: ")

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

def handle_player_choice(conn, character, subregions, npcs, enemies):
    
    options = []
    if subregions:
        options.append("Caminhar")
    if npcs:
        options.append("Interagir")
    if enemies:
        options.append("Lutar")
        


    option_i = ask(options, lambda: [
        lambda: print("\nO que você deseja fazer agora?\n"),
        display.list_options(options)
    ])
    
    # Go back a menu.
    if option_i == 0:
        return False
    
    option = options[option_i - 1]
    

    if option == "Caminhar":
        direction = ask(subregions, lambda: [
            display.clear_screen(),
            display.list_subregions(subregions)
        ])
        destiny_name, _, status = subregions[direction - 1]
        if status == "Passável":
            print(f"\nVocê se moveu para: {subregions[direction - 1]} ({direction}).")
            character.sub_regiao_id = query.fetch_subregion_id_by_name(destiny_name, conn)
            perceived_subregion = False
        else:
            print("\nEssa passagem está bloqueada!")
            

    elif option == "Interagir":
        
        npcs = query.list_citizens_subregion(conn, character.sub_regiao_id)  
            
        npc_i = ask(npcs, lambda: [
            display.clear_screen(),
            display.list_npcs(npcs)
        ], False)
        
        print(npc_i)
        display.press_enter()
        #
        #display.display_npc_info(npcs[npc_choice - 1], conn)
    

    elif option == "Lutar": 
        print("to-do: complete this part lutar")
        display.press_enter()
        #result = int(input("Escolha um inimigo: "))
        #if result != 0 and 1 <= result <= len(enemies):
        #    enemy_id = enemies[result - 1][0]
        #    enemy_info = get_enemy_info(conn, enemy_id)
        #    combat = combat.Com(character, enemy_info, conn)
        #    combat.init

        
    return True

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
    
    # To-do: remove this line of overwritting character percpetion.
    character_perception = 0

    utils.debug(f"Values perception: {character_perception}, {enemy_perception}")

    if (character_perception < enemy_perception):
        print(Style.BRIGHT + Fore.RED + "Você foi Percebido" + Style.RESET_ALL)
        
        enemies_instances = [combat.Enemy(*enemy) for enemy in enemies]
        enemy_combat = combat.Combat(character, enemies_instances, conn)
        
        return enemy_combat.init()
    
    print(Style.BRIGHT + Fore.GREEN + "Você Passou Sorrateiramente" + Style.RESET_ALL)
        
    return True

# Logic:
#   Navigate through the subregion the character is.
#   Returns:
#       True: if the player wants to continue navigating.
#       False: if the player died.
def navigate(conn, character):
        
    perceived_subregion = False
    
    while True:
        display.clear_screen() 
        subregions = world_info.display_subregion_info(conn, character)
        enemies = world_info.show_enemies(conn, character)
        npcs = world_info.display_npcs(conn, character)
        
        if not perceived_subregion and len(enemies) > 0:
            perceived_subregion = True
            alive = enemies_perception(conn, character, enemies);
            if not alive:
                return False

        if not handle_player_choice(conn, character, subregions, npcs, enemies):
            break 
        
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
        display.ingame_menu(),
        display.list_options(options)
    ])

    # Go back one menu.
    if option_i == 0:
        return False
    
    option = options[option_i - 1]
        
    if option == "Navegar":
        navigate(conn, character)  
    elif option == "Ver status do personagem":
        display.clear_screen()
        inventory.header(character)
        display.press_enter()
    elif option == "Ver inventário":
        display.clear_screen()
        inventory.display(character, conn)
        display.press_enter()
    elif option == "Ver feitiços":
        display.clear_screen()
        spells = query.get_spells(conn, character.id)
        inventory.list_spells(conn, spells)

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
            return character
        else:
            character_id = ask(characters, lambda: [
                display.clear_screen(),
                display.list_characters(characters)
            ])
            character = Character(conn, character_id)
            utils.debug(f"Personagem {character.nome} selecionado com sucesso!")
            display.press_enter()


    if option == "Criar personagem": 
        character = Character(conn)
        character.add_database()
        character.define_initial_spells(conn)
        character.add_initial_items(conn)
        utils.debug(f"Personagem {character.nome} criado com sucesso!")


    return character