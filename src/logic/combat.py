from typing import List
import random
from colorama import Fore, Style
import time
from utils import debug, error
import interface.display as display
from logic.character import Character
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
    def __init__(self, character: Character, enemies : List[Enemy], conn):
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
    #   Returns if it was possible to run away from enemy.
    def can_escape(self, enemy: Enemy) -> bool:
         base_chance = 0.5
         modifier = (self.character.inteligencia - enemy.inteligencia) * 0.05
         chance_run = base_chance + modifier
         return random.random() < max(0.8, min(0.9, chance_run))



    # Logic:
    #   Returns the enemy that the player wants to attack.
    def attack(self, enemy: Enemy) -> int:
        damage_caused = random.randint(3, 15) * self.character.nivel
        damage_caused *= self.advantage_element(self.character.elemento, enemy.elemento)
        damage_caused = int(damage_caused)
        return damage_caused

    # Logic:
    # List all spells and select one to cast
    def get_spell(self) -> tuple:
        
        selected_spell = None
        
        while True:
            spell_damage = query.get_damage_spells(self.conn, self.character.id)
            spell_area = query.get_damage_area_spells(self.conn, self.character.id)
            spell_healing = query.get_healing_spells(self.conn, self.character.id)
        
            spells = spell_damage + spell_area + spell_healing
            
            option_i = main.ask(spells, lambda: [
                display.clear_screen(),
                display.list_spells(spells)
            ], False)
            
            selected_spell = spells[option_i - 1]
            _, _, _, energia_arcana, *_ = selected_spell
            
    
            if energia_arcana > self.character.energia_arcana:
                print(Fore.RED + "Energia Arcana insuficiente!" + Style.RESET_ALL)
                display.press_enter()
                continue
            # To-do: Add to query
            self.character.energia_arcana = query.update_mp(self.conn, self.character.id, energia_arcana)
            break
        
        return selected_spell

    
    # Logic:
    #   Apply effect spell selected and remove energy from character.
    #   Returns True if the enemy was killed.
    def apply_spell_effect(self, spell) -> None:
        _, tipo, _, energia_arcana, *_ = spell
        
        # ..
        # To-do: debug test...
        # ..
        debug(tipo, energia_arcana)
        display.press_enter()
        
        if tipo == 'Dano':
            enemy = self.select_enemy()
            self.apply_damage_spell(spell, enemy)
        

        elif tipo == 'Dano de área':
            enemy = self.select_enemy()
            debug('to-do: area damage')
            display.press_enter()


        elif tipo == 'Cura':
            self.apply_heal_spell(spell)

    # Functionality:
    #   Returns true if enemy was killed.
    def apply_damage_spell(self, spell, enemy) -> bool:
        damage = spell[3]
        
        damage *= self.advantage_element(self.character.elemento, enemy.elemento)

        enemy.vida = min(enemy.vida - damage, 0)
        
        # To-do: put this into a interface file.
        print(f"{Fore.BLUE} Foi conjurado {spell[0]} causando {damage} de dano! {Style.RESET_ALL}")
        
        return enemy.vida <= 0

    # Functionality:
    #   Apply area damage spell

    # Functionality:
    #   Apply recover from healing spell 
    def apply_heal_spell(self, spell):
        self.character.vida = min(self.character.vida + spell[4], self.character.vida_maxima)
        print(f"{Fore.GREEN} Você curou {spell[4]} pontos de vida! {Style.RESET_ALL}")

    # Functionality:
    #   Enemy delay.
    def enemy_delay(self):
        print(Style.BRIGHT + Fore.YELLOW + "O inimigo está pensando..." + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)

    # Functionality:
    #   Select and returns an enemy.
    def select_enemy(self) -> Enemy:
        
        if len(self.enemies) == 1:
            return self.enemies[0]
        
        enemy_i = main.ask(self.enemies, lambda: [
            display.clear_screen(),
            display.interface_show_enemies(self.enemies)
        ], False)
        return self.enemies[enemy_i - 1]

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

            option_i = main.ask(options, lambda: [
                display.interface_show_enemies(self.enemies),
                display.list_options(options)
            ], False)
            
            option = options[option_i - 1]

            
            if option == "Atacar":
                enemy = self.select_enemy()
                damage_caused = self.attack(enemy)
                enemy.vida -= damage_caused
                debug(damage_caused)
                display.press_enter()


            elif option == "Fugir":
                
                enemy = self.enemies[0]
                
                if self.can_escape(enemy):
                    print("Você conseguiu escapar do combate!")
                    display.press_enter()
                    display.clear_screen()
                    return True
                
                print("Você não conseguiu escapar do combate!")
                display.press_enter()   

            
            elif option == "Usar Feitiço":
                spell = self.get_spell()
                
                self.apply_spell_effect(spell)
                
                debug(self.character.energia_arcana)
                display.press_enter()
                
                # to-do:
                query.update_combat(self.conn, self.enemies, self.character)


            elif option == "Usar Poção":
                debug("to-do: usar poção")
                display.press_enter()
                
            # ---
            # ....
            # To-do: enemies turn.
            
        return True