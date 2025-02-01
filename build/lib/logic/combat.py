import random
from colorama import Fore, Style
import time
from utils import debug, error
import interface.display as display
from character import Character
import logic.main as main
from logic.enemy import Enemy
import database.dql.query as query

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

    # Logic:
    # List all spells and select one to cast
    def cast_spell(self):
        spells = query.get_learned_spells(self.conn, self.character.id)

        print(Fore.CYAN + "Feitiços disponíveis: " + Style.RESET_ALL)
        for idx, spell in enumerate(spells):
            cost = spell['energia_arcana'] if spell['energia_arcana'] else 0
            print(f"{idx+1}. {spell['nome']} (Custo: {cost} EA) - {spell['descricao']}")
        
        choice = int(input("Escolha um feitiço: "))
        selected_spell = spells[choice-1]

        # Verify if has `energia_arcana` enough
        if self.character.energia_arcana < selected_spell['energia_arcana']:
            print(Fore.RED + "Energia Arcana insuficiente!" + Style.RESET_ALL)
            return

        # apply spell efect
        self.apply_spell_effect(selected_spell)

        self.character.energia_arcana -= selected_spell['energia_arcana']
        self.character.energia_arcana = max(0, self.character.energia_arcana)

    
    # Logic
    # Apply effect spell selected
    def apply_spell_effect(self, spell):
        if spell['tipo'] == 'dano':
            ## to-do
            return # remove
        elif spell['tipo'] == 'area':
            ## to-do
            return # remove
        elif spell['tipo'] == 'cura':
            ## to do
            return # remove


    # Funcionality 
    # Combat funcionality
    # apply damage spell 
    # def apply_damage_spell(self, spell):

    # Functionality:
    #   Combat funcionality.
    # Enemy delay
    def enemy_delay(self):
        print(Style.BRIGHT + Fore.YELLOW + "O inimigo está pensando..." + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)

    # Logic:
    #   True: if the player ran away or won the combat
    #   False: if the player died.
    def init(self):
        
        while True:

            options = [
               "Atacar",
               "Fugir",
               "Usar Feitiço",
               "Usar Poção"
            ]

            option = main.ask(options, lambda: [
                self.interface_show_enemies(),
                #display.list_options(options)
            ], False)

            debug(option)
            display.press_enter()
            
            # Attack.
            #if option == 1:
            #    damage_caused = 10
            #    # To-do: put this into `interface/display.py` file.
            #    print(Style.BRIGHT + Fore.RED + f"Você atacou com força e causou {damage_caused} de dano ao inimigo!" + Style.RESET_ALL)
#
            ## Try to run
#
            ## Cast a spell
            #if option == 3:
            #    self.cast_spell()

            # Use a potion
                
            break;
                
        return True