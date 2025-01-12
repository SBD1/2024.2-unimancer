# just an idea to create character and show in menu of the game

# show main menu
def show_menu():
    print("\n=== Bem-vindo ao Unimancer! ===")
    print("1. Criar um novo personagem")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

# create a new character
def create_character(conn):
    print("\n === Criação de Personagem === ")
    nome = input("Digite o nome do personagem: ")
    elemento = input("Escolha o elemento (Fogo, Água, Terra, Ar, Trevas, Luz): ")
    sub_regiao_id = 1 # define start up region
    conhecimento_arcano = 10
    vida = 100
    vida_maxima = 100
    xp = 0
    xp_total = 0
    energia_arcana = 50
    energia_arcana_maxima = 50
    inteligencia = 1
    moedas = 15
    nivel = 1

# add to db a new character
def add_character(conn, sub_regiao_id, nome, elemento, conhecimento_arcano, vida, vida_maxima, xp, xp_total, energia_arcana, energia_arcana_maxima, inteligencia, moedas, nivel):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO personagem (
                    sub_regiao_id, nome, elemento, conhecimento_arcano, vida, vida_maxima, xp, xp_total,
                    energia_arcana, energia_arcana_maxima, inteligencia, moedas, nivel
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                sub_regiao_id, nome, elemento, conhecimento_arcano, vida, vida_maxima, xp, xp_total,
                energia_arcana, energia_arcana_maxima, inteligencia, moedas, nivel
            ))
            conn.commit()
            print(f"Personagem '{nome}' adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar personagem: {e}")