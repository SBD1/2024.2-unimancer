from create_character import Character
from queries.query import get_subregions_character
from utils import debug 

# Show initial menu of the game and return option chosen.
def show_menu() -> str:
    def ask():
        option = input("Escolha uma opção: ")
        return option.lower()
    
    print("\n--- Bem-vindo ao Unimancer! ---")
    print("criar: criar um novo personagem;")
    print("sair: sair do jogo.")

    option = ask()
    while option not in ["criar", "sair"]:
        print("Opção inválida!")
        option = ask()
    return option

# Display player header information
def header(character):
    print(f"=== {character.nome} === vida: {character.vida}/{character.vida_maxima} "
          f"energia arcana: {character.energia_arcana}/{character.energia_arcana_maxima} "
          f"moedas: {character.moedas} xp: {character.xp}/{character.xp_total} ===")

# Show available subregions and handle navigation
def navigate(conn, character):
    while True:
        print("\n--- Locais Disponíveis ---")
        subregions = get_subregions_character(conn, character.sub_regiao_id)

        # show connected subregions
        for idx, (destino, direcao, situacao) in enumerate(subregions, start=1):
            print(f"{idx}. {destino} ({direcao}) - Situação: {situacao}")

        print("0. Voltar ao menu principal.")

        # player choice a destiny
        try:
            choice = int(input("\nEscolha uma direção ou '0' para voltar: "))
            if choice == 0:
                break  
            elif 1 <= choice <= len(subregions):
                destino, direcao, situacao = subregions[choice - 1]
                if situacao.lower() == "livre":  
                    print(f"\nVocê se moveu para: {destino} ({direcao}).")
                    character.sub_regiao_id = fetch_subregion_id_by_name(destino, conn)
                else:
                    print("\nEssa passagem está bloqueada!")
            else:
                print("\nOpção inválida!")
        except ValueError:
            print("\nEntrada inválida! Escolha um número correspondente ou '0'.")

# Function to change actual subregion
def fetch_subregion_id_by_name(name, conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM sub_regiao WHERE nome = %s", (name,))
        result = cur.fetchone()
        return result[0] if result else None

# Main game loop
def game_loop(conn):
    option = show_menu()
    if option == "sair":
        print("Saindo do jogo...")
        return

    if option == "criar":
        character = Character(conn) 
        character.add_database()  
        debug(f"Personagem {character.nome} criado com sucesso!")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Navegar")
        print("2. Ver status do personagem")
        print("3. Sair")
        
        option = input("Escolha uma opção: ").lower()
        if option == "1":
            navigate(conn, character)  
        elif option == "2":
            header(character)  
        elif option == "3":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")
