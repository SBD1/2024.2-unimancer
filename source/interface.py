# Show initial menu of the game and return option chosen.
def show_menu() -> str:
    
    def ask():
        option = input("Escolha uma opção: ")
        option = option.lower()
        return option
    
    print("\n--- Bem-vindo ao Unimancer! ---")
    print("criar: criar um novo personagem;")
    print("sair: sair do jogo.")

    option = ask()
    while option not in ["criar", "sair"]:
        print("Opção inválida!")
        option = ask()
    return option

def header(character):
    player_info = get_character_info(id)
    print(f"=== {player_info['nome']} === vida: {player_info['vida']}/{player_info['vida_maxima']} energia arcana: {player_info['energia_arcana']}/{player_info['energia_acana_maxima']} moedas: {player_info['moedas']} xp: {player_info['xp']}/{player_info['xp_maximo']} ===")