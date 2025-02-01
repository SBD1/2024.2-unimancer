import random
from colorama import Fore, Style
import time
import src.logic as logic
from utils import debug, error
import interface.display as display
from character import Character

# 1.4x vantagem
# 0.6x desvantagem

# Fogo > Ar 
# Agua > Fogo
# Terra > Agua 
# Ar > Terra 
# Trevas > Luz 
# Luz > Trevas 

# Character/Enemy funcion:
#   Returns a perception test of a D20.
def perception(intelligence: int) -> bool:    
    return random.randint(1, 20) + intelligence

class Enemy:
    def __init__ (self, id, nome, descricao, elemento, vida, vida_maxima, xp_obtido, inteligencia, moedas_obtidas, conhecimento_arcano, energia_arcana_maxima, dialogo):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.elemento = elemento
        self.vida = vida
        self.vida_maxima = vida_maxima
        self.xp_obtido = xp_obtido
        self.inteligencia = inteligencia
        self.moedas_obtidas = moedas_obtidas
        self.conhecimento_arcano = conhecimento_arcano
        self.energia_arcana_maxima = energia_arcana_maxima
        self.dialogo = None

class Combat:
    def __init__(self, character: Character, enemies : list, conn):
        self.character = character
        self.enemies = enemies
        self.conn = conn

    # Logic:
    #   Returns the multiplier of the attack.
    def advantage_element(self, a: str, b: str) -> float:
         advantages = {
             "Fogo": ["Ar", "Água"],
             "Água": ["Fogo", "Terra"],
             "Terra": ["Água", "Ar"],
             "Ar": ["Terra", "Fogo"],
             "Trevas": ["Luz", "Trevas"],
             "Luz": ["Trevas", "Trevas"]
         }
         if advantages[a][0] == b:
             return 1.4
         elif advantages[a][1] == b:
             return 0.6
         else:
             return 1

    # Logic:
    #   Returns how possible is to run from the enemy.
    def try_to_run(self, enemy: Enemy) -> float:
         base_chance = 0.5
         modifier = (self.character.inteligencia - enemy.inteligencia) * 0.05
         chance_run = base_chance + modifier
         return max(0.8, min(0.9, chance_run))
    
    # Logic:
    #   Run away from enemy, updates all enemies info
    def escape_combat(self):
        debug(f"chance de fuga inimigo: {self.enemies[0]}")
        chance_fuga = self.try_to_run(self, self.enemies[0])
        if random.random() < chance_fuga:
            self.combate_ativo = False
            print(Style.BRIGHT + Fore.GREEN + "Você conseguiu escapar do combate!" + Style.RESET_ALL)  
            with self.conn.cursor() as cursor:
                
                # To-do: put this query into the `queries/query.py` file.
                cursor.execute("""SELECT atualizar_combate (%s, %s, %s, %s)""", 
                            (self.personagem.id, self.inimigo.id, self.personagem.vida, self.inimigo.vida))
                self.conn.commit()

            input("Pressione Enter para continuar...")
        else:
            print(Style.BRIGHT + Fore.RED + "O inimigo bloqueou sua tentativa de fuga!" + Style.RESET_ALL)

    # To-do: put this function into the `interface/display.py` file.
    # Interface:
    #   Print all enemies and their description and life.
    def interface_show_enemies(self):
        for idx, enemy in enumerate(self.enemies):
            print(f"| {idx+1} - {enemy.nome} - {enemy.descricao} - {enemy.vida}/{enemy.vida_maxima} |")

    # Logic:
    #   Returns the enemy that the player wants to attack.
    def attack(self, enemy: Enemy) -> int:
        damage_caused = random.randint(50, 60) * self.personagem.nivel
        damage_caused *= self.vantagem_elemento(self.personagem.elemento, self.inimigo.elemento)
        damage_caused = int(damage_caused)
        return damage_caused

    # Functionality:
    #   Combat funcionality.
    # Enemy delay
    def enemy_delay(self):
        print(Style.BRIGHT + Fore.YELLOW + "O inimigo está pensando..." + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)

    def init(self):
        
        while True:

            options = [
               "Atacar",
               "Fugir",
               "Usar Feitiço",
               "Usar Poção"
            ]

            option = logic.ask(options, lambda: [
                self.interface_show_enemies(),
                display.list_options(options)
            ])

            print(option)
            
            # Attack.
            if option == 1:
                # To-do: put this into `interface/display.py` file.
                print(Style.BRIGHT + Fore.RED + f"Você atacou com força e causou {damage_caused} de dano ao inimigo!" + Style.RESET_ALL)