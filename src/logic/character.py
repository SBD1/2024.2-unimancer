from utils import debug
import database.dql.query as query
import interface.display as display
import logic.main as logic
import utils

initial_spells = {
     "Fogo": [
        46,
        33,
        6,
    ],
    "Água": [
        43,
        31,
        1,
    ],
    "Terra": [
        49,
        35,
        11
    ],
    "Ar" :[
        52,
        37,
        16,
    ],
    "Luz" :[
        55,
        39,
        21,
    ],
    "Trevas":[
        58,
        41,
        26,
    ]
}

elements = [key for key in initial_spells]

class Character:
    
    def __init__(self, conn, id = None):
        self.conn = conn

        if not id:
            self.ask_info()
            
            # If the character shouldn't exist, return.
            if self.nome == "":
                return
            
            id = query.add_character(self.conn, self.nome, self.elemento)
            print(id)
            
        self.update(id)
        
    def update(self, id: int) -> None:
        character_info = query.get_character_info(self.conn, id)
        
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

    # Get the character's information.
    def ask_info(self) -> None:
        
        display.print_center("=== Criação de Personagem === ")
        
        self.nome = display.ask_text(
            "Digite o nome do personagem, digite nada para voltar"
        )
        
        if not self.nome:
            return

        element_i = logic.ask(elements, lambda: [
            display.clear_screen(),
            display.print_center(f"Nome: {self.nome}"),
            display.list_options(elements)
        ])
        
        # If player chooses to go back, then clear name to go back one menu.
        if not element_i:
            self.nome = ""
            return
            
        self.elemento = elements[element_i - 1]

    # Define the initial spells for the character.
    def define_initial_spells(self, conn):
        spellbook_id = query.get_inventory(conn, "grimorio", self.id)
        spells_ids = initial_spells[self.elemento]
        query.add_learned_spells(conn, spellbook_id, spells_ids)

    # Add initial items to the character's backpack.
    def add_initial_items(self, conn):
        backpack_id = query.get_inventory(conn, "mochila", self.id)

        elixir_da_vida_id = 133
        mana_liquida_id = 134
        
        query.add_items_instance(conn, backpack_id, [
            elixir_da_vida_id,
            elixir_da_vida_id,
            mana_liquida_id
        ])