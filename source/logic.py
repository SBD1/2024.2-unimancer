import interface.display as display
import interface.inventory as inventory
import interface.world_info as world_info
import queries.query as query
import combat as combat
from colorama import Fore, Style
from character import Character
import utils

# Interface/Logic:
#   Ask from the input options and validate it, while running auxiliary function before asking every time.
def ask(options: list, before_func=None) -> int:
    option = int(0)
    while not (option >= 1 and option <= len(options)):
        
        if before_func:
            before_func()
            
        option = input("Escolha uma opção: ")

        try:
            
            assert option != "", "Digite um número válido!"
            
            option = int(option)
                
            assert (option >= 1 and option <= len(options)), "Opção inválida entre as disponíveis!"

        except ValueError:
            print("Digite um número válido!")
            display.press_enter()
        except AssertionError as e:
            print(e)
            display.press_enter()
        
    return option

def handle_player_choice(conn, character, subregions, npcs, enemies):
    options = [
        "Caminhar",
        "Interagir",
        "Lutar",
        "Voltar"
    ]

    option = ask(options, lambda: [
        lambda: print("\nO que você deseja fazer agora?\n"),
        display.list_options(options)
    ])

    if option == 1:  # change current location
        if subregions:
            choice = int(input("\nEscolha uma direção: "))
            if 1 <= choice <= len(subregions):
                destino, direcao, situacao = subregions[choice - 1]
                if situacao == "Passável":
                    print(f"\nVocê se moveu para: {destino} ({direcao}).")
                    character.sub_regiao_id = query.fetch_subregion_id_by_name(destino, conn)
                else:
                    print("\nEssa passagem está bloqueada!")
            else:
                print("\nOpção inválida!")
        else:
            print("Nenhuma sub-região para navegar.")
            
    elif option == 2:  # Interact with npcs
        if npcs:
            npc_choice = int(input("Escolha um personagem (número): "))
            if 1 <= npc_choice <= len(npcs):
                print(f"Você interagiu com {npcs[npc_choice - 1][0]}")
                # NPCS TO INTERACT
            else:
                print("\nOpção inválida!")
        else:
            print("Nenhum NPC disponível para interação.")
    
    # Fight with an enemy:
    elif option == 3: 
        if enemies:
            result = int(input("Escolha um inimigo: "))
            if result != 0 and 1 <= result <= len(enemies):
                enemy_id = enemies[result - 1][0]
                #enemy_info = get_enemy_info(conn, enemy_id)
                #combate = Combat(character, enemy_info, conn)
                #combate.iniciar()
            else:
                print("\nOpção inválida!")
        else:
            print("Nenhum inimigo disponível para combate.")
    else:
        return False
        
    return True

def navigate(conn, character):
    while True:
        display.clear_screen()
        subregions = world_info.display_subregion_info(conn, character)
        enemies = world_info.show_enemies(conn, character)
        npcs = world_info.display_npcs(conn, character)
        
        # To-do: select first enemy and try perception:
        character_perception = combat.perception(character.inteligencia)
        enemy = combat.Enemy(*(enemies[0]))
        enemy_perception = combat.perception(enemy.inteligencia)
        
        utils.debug(f"Values perception: {character_perception}, {enemy_perception}")


        if (character_perception < enemy_perception):
            print(Style.BRIGHT + Fore.RED + "Você foi Percebido" + Style.RESET_ALL)
            enemies_instances = [combat.Enemy(*enemy) for enemy in enemies]
            enemy_combat = combat.Combat(character, enemies_instances, conn)
            enemy_combat.init()
        else:
            print(Style.BRIGHT + Fore.GREEN + "Você Passou Sorrateiramente" + Style.RESET_ALL)

        if not handle_player_choice(conn, character, subregions, npcs, enemies):
            break 

# Interface/Logic:
#   Show in-game options.
def game(conn, character: Character) -> bool:
    options = [
        "Navegar",
        "Ver status do personagem",
        "Ver inventário",
        "Ver feitiços",
        "Sair"
    ]
    option = ask(options, lambda: [
        display.clear_screen(),
        display.ingame_menu(),
        display.list_options(options)
    ])
    if option == 1:
        navigate(conn, character)  
    elif option == 2:
        display.clear_screen()
        inventory.header(character)
        display.press_enter()
    elif option == 3:    
        display.clear_screen()
        inventory.display(character, conn)
        display.press_enter()
    elif option == 4:
        display.clear_screen()
        spells = query.get_spells(conn, character.id)
        inventory.list_spells(conn, spells)

    elif option == 5:
        print("Saindo do jogo/ir para menu principal.")
        display.press_enter()
        return False
    
    return True


# Interface/Logic:
#   Show main menu (before game starts).
def main_menu(conn) -> None:
    
    options = [
        "Listar personagens",
        "Criar personagem",
        "Sair do jogo"
    ]
    
    # Get an option.
    option = ask(options, lambda: [
        display.clear_screen(),
        display.show_title(),
        display.list_options(options)
    ])
    
    character = None
    
    # Listar.
    if option == 1:

        characters = query.list_all_characters(conn)
        
        if not characters:
            display.clear_screen()
            print(Fore.RED + "Nenhum personagem encontrado" + Style.RESET_ALL)
            display.press_enter()
        else:
            character_id = ask(characters, lambda: [
                display.clear_screen(),
                display.list_characters(characters)
            ])
            character = Character(conn, character_id)
            utils.debug(f"Personagem {character.nome} selecionado com sucesso!")
            display.press_enter()


    # Criar.
    if option == 2: 
        character = Character(conn)
        character.add_database()
        character.define_initial_spells(conn)
        character.add_initial_items(conn)
        utils.debug(f"Personagem {character.nome} criado com sucesso!")

    # Sair.
    if option == 3:
        print("Saindo do jogo...")

    return character