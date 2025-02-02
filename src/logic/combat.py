from ast import For
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

            # Verify if the character has enough energy to cast the spell
            usable_spells = [spell for spell in spells if spell[3] <= (self.character.energia_arcana if self.character.energia_arcana is not None else 0)]

            if not usable_spells:
                print(Fore.RED + "Você não tem energia arcana suficiente para usar nenhum feitiço!" + Style.RESET_ALL)
                display.press_enter()
                return None
            
            option_i = main.ask(spells, lambda: [
                display.clear_screen(),
                display.list_spells(spells)
            ], False)
            
            selected_spell = spells[option_i - 1]
            _, _, _, energia_arcana, *_ = selected_spell
            
            # Energia_arcana != None
            energia_arcana = energia_arcana if energia_arcana is not None else 0
            pc_energia_acana = self.character.energia_arcana if self.character.energia_arcana is not None else 0

            if energia_arcana > pc_energia_acana:
                print(Fore.RED + "Energia Arcana insuficiente!" + Style.RESET_ALL)
                display.press_enter()
                continue
            # To-do: Add to query
            self.character.energia_arcana -= energia_arcana
            self.character.energia_arcana = query.update_mp(self.conn, self.character.id, self.character.energia_arcana)
            break
        
        return selected_spell

    
    # Logic:
    #   Apply effect spell selected and remove energy from character.
    #   Returns True if the enemy was killed.
    def apply_spell_effect(self, spell) -> None:
        if spell == None:
            return
        _, tipo, _, energia_arcana, *_ = spell
        
        # ..
        # To-do: debug test...
        # ..
        debug(f" tipo do feitiço: {tipo}, qtd_energia: {energia_arcana}")
        display.press_enter()
        
        if tipo == 'Dano':
            enemy = self.select_enemy()
            self.apply_damage_spell(spell, enemy)
        

        elif tipo == 'Dano de área':
            # enemy = self.select_enemy()
            # debug('to-do: area damage')
            # display.press_enter()
            self.apply_area_damage_spell(spell)


        elif tipo == 'Cura':
            self.apply_heal_spell(spell)

    # Functionality:
    #   Returns true if enemy was killed.
    def apply_damage_spell(self, spell, enemy) -> bool:
        damage = spell[4]
        
        damage *= self.advantage_element(self.character.elemento, enemy.elemento)

        enemy.vida = min(enemy.vida - damage, 0)
        
        # To-do: put this into a interface file.
        print(f"{Fore.BLUE} Foi conjurado {spell[0]} causando {damage} de dano! {Style.RESET_ALL}")
        return enemy.vida <= 0

    # Functionality:
    #   Apply area damage spell
    def apply_area_damage_spell(self, spell):
        nome, _, _, _, dano, qtd_inimigos_afetados = spell
        print(f"{Fore.MAGENTA} {nome} foi conjurado! {Style.RESET_ALL}")

        # filter enemies alive and random chose enemies
        alive_enemies = [enemy for enemy in self.enemies if enemy.vida > 0]
        affected_enemies = random.sample(alive_enemies, min(qtd_inimigos_afetados, len(alive_enemies)))

        for enemy in affected_enemies:
            final_damage = dano * self.advantage_element(self.character.elemento, enemy.elemento)
            enemy.vida = max(enemy.vida - final_damage, 0)
            print(f"{Fore.BLUE} {enemy.nome} recebeu {final_damage} de dano! {Style.RESET_ALL}")

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

    # Functionality
    # Enemy turn
    def enemy_turn(self):
        print(Style.BRIGHT + Fore.YELLOW + "Os inimigos estão atacando!!!" + Style.RESET_ALL)
        time.sleep(1)

        for enemy in self.enemies:
            if enemy.vida > 0:
                damage = random.randint(3, 10)
                damage *= self.advantage_element(enemy.elemento, self.character.elemento)
                self.character.vida = max(self.character.vida - damage, 0)

                print(f"{Fore.RED} {enemy.nome} te atacou e causou {damage} de dano! {Style.RESET_ALL}")

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

    # Functionality
    # check if combat has terminated
    def check_combat_end(self):
        if self.character.vida <= 0:
            print(Fore.RED + "Você foi derrotado..." + Style.RESET_ALL)
            return True
        
        if all(enemy.vida <= 0 for enemy in self.enemies):
            print(Fore.GREEN + "Todos os inimigos foram derrotados!" + Style.RESET_ALL)
            return True

        return False

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

            elif option == "Usar Poção":
                debug("to-do: usar poção")
                display.press_enter()

            query.update_combat(self.conn, self.enemies, self.character)
            if self.check_combat_end():
                return True
            
            self.enemy_turn()

            if self.check_combat_end():
                return True

        return True