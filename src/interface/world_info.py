from colorama import Fore, Style
import psycopg2
from database.dql.query import get_subregions_character, list_npcs_subregion, list_enemys_subregion
from character import Character

# Function to get subregion description
def get_subregion_description(conn, character: Character):
    try:
        with conn.cursor() as cur:
            cur.execute(f"SELECT descricao, nome FROM sub_regiao WHERE id = {character.sub_regiao_id}")
            result = cur.fetchall()
            return result
    except psycopg2.Error as e:
        print(f"Erro ao obter descrição da sub-região: {e}")
        conn.rollback() 
        return "Erro ao acessar a descrição."

# Show available subregions and handle navigation 
def display_subregion_info(conn, character: Character):
    print(Fore.CYAN + "\n ----- Descrição -------" + Style.RESET_ALL)
    rg = get_subregion_description(conn, character)
    print(f"{rg[0][1]} - {rg[0][0]}")

    print(Fore.YELLOW + "\n--- Locais Disponíveis ---" + Style.RESET_ALL)
    subregions = get_subregions_character(conn, character.sub_regiao_id)
    if subregions:
        for idx, (destino, direcao, situacao) in enumerate(subregions, start=1):
            print(f"{idx}. {destino} ({direcao}) - Situação: {situacao}")
    else:
        print("Nenhum local disponível.")

    return subregions

# Display all npcs in that subregion
def display_npcs(conn, character: Character):
    print(Fore.YELLOW + "\n--- Personagens ---" + Style.RESET_ALL)
    npcs = list_npcs_subregion(conn, character.sub_regiao_id)
    if npcs:
        for npc in npcs:
            nome, tipo = npc
            print(f"{nome} - ({tipo})")
    else:
        print("Nenhum personagem encontrado.")
    
    return npcs

# Display all enemies in that subregion
def show_enemies(conn, character: Character):
   enemies = list_enemys_subregion(conn, character.sub_regiao_id)
   if enemies:
       print(Fore.YELLOW + "\n--- Inimigos na Região ---" + Style.RESET_ALL)
       for idx, enemy in enumerate(enemies, start=1):
           enemy_id, enemy_name, enemy_description,  *_ = enemy
           print(f"{idx}. {enemy_name} - {enemy_description}")
   else:
       print(Fore.GREEN + "Nenhum inimigo nesta sub-região." + Style.RESET_ALL)
   return enemies
