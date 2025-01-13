from utils import debug

elements = ["Fogo", "Água", "Terra", "Ar", "Trevas", "Luz"]

class Character:
    
    def __init__(self, conn):
        self.conn = conn
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
        self.get_information()
        
    def get_information(self):
        print("\n === Criação de Personagem === ")
        self.nome = input("Digite o nome do personagem: ")
        elemento = ""
        while elemento not in elements:
            print("Elemento inválido!")
            elemento = input(f"Escolha o elemento ({', '.join(elements)}): ")
        
    def add_database(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO personagem (
                        sub_regiao_id,
                        nome,
                        elemento,
                        conhecimento_arcano,
                        vida,
                        vida_maxima,
                        xp,
                        xp_total,
                        energia_arcana,
                        energia_arcana_maxima,
                        inteligencia,
                        moedas,
                        nivel
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.sub_regiao_id,
                    self.nome,
                    self.elemento,
                    self.conhecimento_arcano,
                    self.vida,
                    self.vida_maxima,
                    self.xp,
                    self.xp_total,
                    self.energia_arcana,
                    self.energia_arcana_maxima,
                    self.inteligencia,
                    self.moedas,
                    self.nivel
                ))
                self.conn.commit()
                debug(f"Character: Personagem '{self.nome}' adicionado com sucesso!")
        except Exception as e:
            debug(f"Character: Erro ao adicionar personagem: {e}")
    
    def get_character_info(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM personagem
                WHERE id = {id}
            """)
           