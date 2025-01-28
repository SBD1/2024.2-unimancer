import os
import platform
import psycopg2
from colorama import Fore, Style, init
from create_character import Character
from queries.query import get_subregions_character, list_all_characters, list_npcs_subregion, list_item_inventory, list_enemys_subregion, get_enemy_info
from utils import debug 
from combat import Combate, verificar_percepcao, Inimigo

# Initialize colorama
init()

# Clean the terminal screen
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def show_title():
    print("")
    print(" ██╗   ██╗███╗   ██╗██╗███╗   ███╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ ")
    print(" ██║   ██║████╗  ██║██║████╗ ████║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗")
    print(" ██║   ██║██╔██╗ ██║██║██╔████╔██║███████║██╔██╗ ██║██║     █████╗  ██████╔╝")
    print(" ██║   ██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗")
    print(" ╚██████╔╝██║ ╚████║██║██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╗███████╗██║  ██║")
    print("  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝")
    print("")

# Show initial menu of the game and return option chosen.
def show_menu() -> str:
    def ask():
        return input("Escolha uma opção: ").lower()
    
    print(Style.BRIGHT + Fore.YELLOW + "\n--- Bem-vindo ao Unimancer! ---" + Style.RESET_ALL)
    print("criar: criar um novo personagem;")
    print("listar: Liste os personagens existentes")
    print("sair: sair do jogo.")

    option = ask()
    while option not in ["criar", "sair", "listar"]:
        print("Opção inválida!")
        option = ask()
    return option

# Display player header information
def header(character):
    clear_screen()
    print(f"=== {character.nome} === vida: {character.vida}/{character.vida_maxima} "
          f"energia arcana: {character.energia_arcana}/{character.energia_arcana_maxima} "
          f"moedas: {character.moedas} xp: {character.xp}/{character.xp_total} ===")

# Display player inventory
def inventory(character, conn):
    clear_screen()
    print(f"Inventário de === {character.nome} ===")
    print("-" * 40)

    items = list_item_inventory(conn, character.id)

    if not items:
       print("O inventário está vazio.")
    else:
       for item in items:
           nome, descricao, qtd = item
           print(f"- {nome} ({descricao}): {qtd}")
    
    print("-" * 40)

# Show available subregions and handle navigation 
def display_subregion_info(conn, character):
    print(Fore.CYAN + "\n ----- Descrição -------" + Style.RESET_ALL)
    print(get_subregion_description(conn, character))

    print(Fore.YELLOW + "\n--- Locais Disponíveis ---" + Style.RESET_ALL)
    subregions = get_subregions_character(conn, character.sub_regiao_id)
    if subregions:
        for idx, (destino, direcao, situacao) in enumerate(subregions, start=1):
            print(f"{idx}. {destino} ({direcao}) - Situação: {situacao}")
    else:
        print("Nenhum local disponível.")

    return subregions

def display_enemies(conn, character):
    enemys = list_enemys_subregion(conn, character.sub_regiao_id)
    if enemys:
        print(Fore.YELLOW + "\n--- Verificando Percepção dos Inimigos ---" + Style.RESET_ALL)
        
        for enemy in enemys:
            enemy_id, enemy_name, *_ = enemy
            enemy_info = get_enemy_info(conn, enemy_id)
            inimigo_instanciado = Inimigo(*enemy_info)
            inimigo_percebeu = verificar_percepcao(character, [inimigo_instanciado])
            
            if inimigo_percebeu:
                inimigo_percebeu = (
                inimigo_percebeu.nome,
                inimigo_percebeu.id,
                inimigo_percebeu.armazenamento_id,
                inimigo_percebeu.descricao,
                inimigo_percebeu.elemento,
                inimigo_percebeu.vida,
                inimigo_percebeu.vida_maxima,
                inimigo_percebeu.xp_obtido,
                inimigo_percebeu.inteligencia,
                inimigo_percebeu.moedas_obtidas,
                inimigo_percebeu.conhecimento_arcano,
                inimigo_percebeu.energia_arcana_maxima
            )
                print(Style.BRIGHT + Fore.RED + "Um inimigo o percebeu! O combate será iniciado." + Style.RESET_ALL)
                combate = Combate(character, inimigo_percebeu, conn)
                combate.iniciar()
                if character.vida <= 0:
                    print(Fore.RED + "Você foi derrotado no combate! Voltando ao menu principal..." + Style.RESET_ALL)
                    return
    else:
        print(Fore.GREEN + "Nenhum inimigo nesta sub-região." + Style.RESET_ALL)
    
    return enemys

def display_npcs(conn, character):
    print(Fore.YELLOW + "\n--- Personagens ---" + Style.RESET_ALL)
    npcs = list_npcs_subregion(conn, character.sub_regiao_id)
    if npcs:
        for npc in npcs:
            nome, tipo = npc
            print(f"{nome} - ({tipo})")
    else:
        print("Nenhum personagem encontrado.")
    
    return npcs

def handle_player_choice(conn, character, subregions, npcs, enemys):
    try:
        choice_interaction = input("\nO que você deseja fazer agora?\n0-Voltar\n1-Continuar caminhando\n2-Interagir com um personagem\n3-Lutar: \n")
        
        if choice_interaction == "0":
            return False 

        elif choice_interaction == "1":  # change current location
            if subregions:
                choice = int(input("\nEscolha uma direção: "))
                if 1 <= choice <= len(subregions):
                    destino, direcao, situacao = subregions[choice - 1]
                    if situacao == "Passável":
                        print(f"\nVocê se moveu para: {destino} ({direcao}).")
                        character.sub_regiao_id = fetch_subregion_id_by_name(destino, conn)
                    else:
                        print("\nEssa passagem está bloqueada!")
                else:
                    print("\nOpção inválida!")
            else:
                print("Nenhuma sub-região para navegar.")
        
        elif choice_interaction == "2":  # Iteract with npcs
            if npcs:
                npc_choice = int(input("Escolha um personagem (número): "))
                if 1 <= npc_choice <= len(npcs):
                    print(f"Você interagiu com {npcs[npc_choice - 1][0]}")
                    # NPCS TO INTERACT
                else:
                    print("\nOpção inválida!")
            else:
                print("Nenhum NPC disponível para interação.")
        
        elif choice_interaction == "3": # Fight with an enemy
            if enemys:
                result = int(input("Escolha um inimigo: "))
                if result != 0 and 1 <= result <= len(enemys):
                    enemy_id = enemys[result - 1][0]
                    enemy_info = get_enemy_info(conn, enemy_id)
                    combate = Combate(character, enemy_info, conn)
                    combate.iniciar()
                else:
                    print("\nOpção inválida!")
            else:
                print("Nenhum inimigo disponível para combate.")
        
        else:
            print("\nOpção inválida!")
        return True 
        
    except ValueError:
        print("\nEntrada inválida! Escolha um número correspondente ou '0'.")
        return True  

def navigate(conn, character):
    while True:
        clear_screen()
        
        subregions = display_subregion_info(conn, character)
        enemys = display_enemies(conn, character)
        npcs = display_npcs(conn, character)
        
        if not handle_player_choice(conn, character, subregions, npcs, enemys):
            break 


# Function to change actual subregion
def fetch_subregion_id_by_name(name, conn):
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT id FROM sub_regiao WHERE nome = %s", (name,))
        result = cur.fetchone()
        return result[0] if result else None

# Function to get subregion description
def get_subregion_description(conn, character):
    try:
        with conn.cursor() as cur:
            cur.execute(f"SELECT descricao FROM sub_regiao WHERE id = {character.sub_regiao_id}")
            result = cur.fetchone()
            return result[0]
    except psycopg2.Error as e:
        print(f"Erro ao obter descrição da sub-região: {e}")
        conn.rollback()  # Reverte a transação em caso de erro
        return "Erro ao acessar a descrição."

# Main game loop
def game_loop(conn):
    ok = False
    while(ok == False):
        clear_screen()
        show_title()
        option = show_menu()
        characters = list_all_characters(conn)

        if option == "sair":
            print("Saindo do jogo...")
            return

        elif option == "listar":
            if not characters:
                clear_screen()
                print(Fore.RED + "Nenhum personagem encontrado" + Style.RESET_ALL)
                input("\nPressione Enter para continuar...")
                ok = False
            else:
                for idx, character in enumerate(characters, start=1):
                    print(f"\n Personagem: {idx}, ID: {character[0]}, nome: {character[1]}, elemento: {character[2]}") 
                    
                personagem_id = input("Escolha um personagem (id): ")
                character = Character(conn, personagem_id)
                debug(f"Personagem {character.nome} selecionado com sucesso!")
                ok = True

        elif option == "criar":
            character = Character(conn) 
            character.add_database() 
            debug(f"Personagem {character.nome} criado com sucesso!")
            ok = True

    while True:
        show_title()
        clear_screen()
        print(Fore.CYAN + "\n--- Menu Principal ---" + Style.RESET_ALL)
        print("1. Navegar")
        print("2. Ver status do personagem")
        print("3. Ver Inventário")
        print("4. Sair")
        
        option = input("Escolha uma opção: ").lower()
        if option == "1":
            navigate(conn, character)  
        elif option == "2":
            header(character)
            input("\nPressione Enter para continuar...")
        elif option == "3":
            inventory(character, conn)
            input("\nPressione Enter para continuar...")
        elif option == "4":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")
