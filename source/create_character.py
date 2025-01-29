from utils import debug

elements = ["Fogo", "Água", "Terra", "Ar", "Trevas", "Luz"]

initial_spells = {
     "Fogo": [
        (46, "Bola de Fogo: Lança uma bola de fogo explosiva que causa danos intensos a todos os inimigos em uma área."),
        (33, "Flama Curativa: Utiliza o calor das chamas para aquecer e curar ferimentos de aliados próximos."),
        (6, "Labareda Inicial: Lança chamas suaves que atingem uma área moderada, causando danos contínuos aos inimigos presentes.")
    ],
    "Água": [
        (43, "Jato de Água: Lança um jato de água pressurizada que causa danos moderados a um único inimigo."),
        (31, "Cura Áquatica: Canaliza a energia das águas para restaurar a vida de aliados dentro da área de efeito."),
        (1, "Sopro Congelante: Exala um vento gelado que congela os inimigos em uma ampla área, causando dano e reduzindo sua velocidade.")
    ],
    "Terra": [
        (49, "Saco de Pedra: Arremessa grandes pedras contra os inimigos, causando danos pesados a um único alvo."),
        (35, "Regeneração Terrena: Conecta-se com a energia da terra para regenerar a vida dos aliados na área afetada."),
        (11, "Tremor Raso: Provoca um leve tremor que atinge todos os inimigos próximos, causando danos moderados e desequilibrando suas defesas.")
    ],
    "Ar" :[
        (52, "Rajada Voadora: Lança uma forte rajada de vento que causa danos e empurra os inimigos para trás."),
        (37, "Brisa Curativa: Convoca uma brisa suave que revitaliza e cura os aliados dentro de sua trajetória."),
        (16, "Vento Cortante: Lança rajadas de vento afiadas que cortam e causam danos a todos os inimigos na área alvo.")
    ],
    "Luz" :[
        (55, "Raio Luminoso: Dispara um raio de luz intensa que causa danos a um único inimigo."),
        (39, "Luz Restauradora: Emite uma luz pura que cura ferimentos e restaura a energia arcana dos aliados na área iluminada."),
        (21, "Clarão Ofuscante: Emite um brilho intenso que cega e causa danos leves a todos os inimigos na área alvo.")
    ],
    "Trevas":[
        (58, "Sombras Cortantes: Lança sombras afiadas que causam danos contínuos a múltiplos inimigos."),
        (41, "Sombra Curativa: Manipula as sombras para curar os aliados, ocultando-os enquanto restaura sua vitalidade."),
        (26, "Sussurro das Sombras: Murmura palavras sombrias que envolvem a área, causando danos leves e enfraquecendo a moral dos inimigos.")
    ]
}

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
    
    def definy_initial_spells(self, conn):
        try:
            spells = initial_spells[self.elemento]

            with conn.cursor() as cur:
                for spell in spells:
                    spell_id = spell[0]
                    cur.execute(
                        """
                        SELECT aprender_feitico (%s, %s);
                        """, (self.id, spell_id)
                    )

            debug(f"Initial Spells learned for '{self.nome}' with success")
        except Exception as e:
            debug(f"Error: {e}")
            raise

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
        # self.definy_initial_spells(self.conn)

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
    


