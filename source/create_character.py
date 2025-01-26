from utils import debug

elements = ["Fogo", "Água", "Terra", "Ar", "Trevas", "Luz"]

class Character:
    
    def __init__(self, conn, id = None):
        self.conn = conn
        self.id = None
        self.nome = None
        self.elemento = None
        self.sub_regiao_id = 1
        self.conhecimento_arcano = 10
        self.vida = 100
        self.vida_maxima = 100
        self.xp = 0
        self.xp_total = 10
        self.energia_arcana = 50
        self.energia_arcana_maxima = 50
        self.inteligencia = 1
        self.moedas = 15
        self.nivel = 1
        if not id:
            self.get_information()
        else:
            character_info = self.get_character_info(conn, id) 
            self.id = character_info[0] 
            self.sub_regiao_id = character_info[1]
            self.nome = character_info[2]
            self.elemento = character_info[3]
            self.conhecimento_arcano = character_info[4]
            self.vida = character_info[5]
            self.vida_maxima = character_info[6]
            self.xp = character_info[7]
            self.xp_total = character_info[8]
            self.energia_arcana = character_info[9]
            self.energia_arcana_maxima = character_info[10]
            self.inteligencia = character_info[11]
            self.moedas = character_info[12]
            self.nivel = character_info[13]
        
    def get_information(self):
        print("\n === Criação de Personagem === ")
        self.nome = input("Digite o nome do personagem: ")
        
        def ask():
            return input(f"Escolha o elemento ({', '.join(elements)}): ").lower()
        
        elemento = ask()
        lower_case_elements = [elemento.lower() for elemento in elements]
        while elemento not in lower_case_elements:
            print("Elemento inválido.")
            elemento = ask()
        
        self.elemento = elemento.capitalize()

        
        
    def add_database(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT criar_personagem(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.sub_regiao_id, self.nome, self.elemento, self.conhecimento_arcano, self.vida, self.vida_maxima, self.xp, self.xp_total, self.energia_arcana, self.energia_arcana_maxima, self.inteligencia, self.moedas, self.nivel))
                self.id = cur.fetchone()[0]
                self.conn.commit()

                debug(f"Character: Personagem '{self.nome}' adicionado com sucesso!")
                return self

        except Exception as e:
            debug(f"Character: Erro ao adicionar personagem: {e}")

        
    
    def get_character_info(self, conn, id): 
        with conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM personagem
                WHERE id = %s
            """, (id,))
            result = cur.fetchone() 
            return result
