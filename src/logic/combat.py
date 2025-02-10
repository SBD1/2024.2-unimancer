from typing import List, Tuple
import random
from colorama import Fore, Style
import time

from numpy import character
import interface.inventory as inventory
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
    # Return the multiplier of enemy attack by life
    def damage_modifier_by_health(self, enemy: Enemy) -> float:
        if enemy.vida_maxima < 50:
            return 1.1
        elif 50 <= enemy.vida_maxima < 100:
            return 1.2
        elif 100 <= enemy.vida_maxima < 150:
            return 1.4
        elif enemy.vida_maxima >= 150:
            return 1.6
        return 1.1

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
        damage_caused *= self.damage_modifier_by_health(enemy)
        damage_caused = int(damage_caused)
        
        return damage_caused

    # Logic:
    # List all spells and select one to cast
    def get_spell(self, spells: List[Tuple]) -> tuple:
        
        selected_spell = None
        
        while True:
            # Select a spell from the ones that the character can cast.
            option_i = main.ask(spells, lambda: [
                display.clear_screen(),
                inventory.list_spells(spells)
            ], False)
            
            selected_spell = spells[option_i - 1]
            _, _, _, energia_arcana, *_ = selected_spell

            self.character.energia_arcana = query.get_update_character_mp(self.conn, self.character.id, energia_arcana)
            break

        return selected_spell

    # Logic:
    #   Apply effect spell selected and remove energy from character.
    #   Returns True if the enemy was killed.
    def apply_spell_effect(self, spell) -> None:
        if spell == None:
            return
        _, tipo, *_ = spell
    
        if tipo == 'Dano':
            enemy = self.select_enemy()
            self.apply_damage_spell(spell, enemy)
        elif tipo == 'Dano de área':
            self.apply_area_damage_spell(spell)
        elif tipo == 'Cura':
            self.apply_heal_spell(spell)

    # Functionality:
    #   Returns true if enemy was killed.
    def apply_damage_spell(self, spell, enemy) -> bool:
        damage = spell[4]
        
        damage *= self.advantage_element(self.character.elemento, enemy.elemento)
        damage *= self.damage_modifier_by_health(enemy)

        enemy.vida = min(enemy.vida - damage, 0)

        print(
            Fore.BLUE +
            f"Foi conjurado {spell[0]} causando {damage} de dano!" +
            Style.RESET_ALL
        )
        return enemy.vida <= 0

    # Functionality:
    #   Apply area damage spell
    def apply_area_damage_spell(self, spell):
        nome, _, _, _, dano, qtd_inimigos_afetados = spell
        
        print(
            Fore.MAGENTA +
            f"{nome} foi conjurado!" +
            Style.RESET_ALL
        )

        alive_enemies = [enemy for enemy in self.enemies if enemy.vida > 0]
        affected_enemies = random.sample(alive_enemies, min(qtd_inimigos_afetados, len(alive_enemies)))

        for enemy in affected_enemies:
            final_damage = dano * self.advantage_element(self.character.elemento, enemy.elemento)
            enemy.vida = max(enemy.vida - final_damage, 0)
            print(
                Fore.BLUE +
                f"{enemy.nome} recebeu {final_damage} de dano!" +
                Style.RESET_ALL
            )

    # Functionality:
    #   Apply recover from healing spell 
    def apply_heal_spell(self, spell):
        self.character.vida = min(self.character.vida + spell[4], self.character.vida_maxima)
        print(f"{Fore.GREEN} Você curou {spell[4]} pontos de vida! {Style.RESET_ALL}")

    # Functionality:
    #   Returns the potion selected by the player.
    def get_potion(self, potions: List[Tuple]) -> tuple:

        option_i = main.ask(potions, lambda: [
            display.clear_screen(),
            inventory.list_potions(potions)
        ])
        
        if option_i == 0:
            return None

        return potions[option_i - 1]

    # Functionality:
    #   Enemy delay.
    def enemies_delay(self):
        print(Style.BRIGHT + Fore.YELLOW + "O inimigo está pensando..." + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)
        display.press_enter()

    # Functionality:
    #   Enemy turn.
    def enemies_turn(self):        
        
        alive_enemies = len([enemy for enemy in self.enemies if enemy.vida > 0])
        
        if alive_enemies:
            for enemy in self.enemies:
                if enemy.vida > 0:

                    # To-do: implement "enemy_attack()"
                    damage = random.randint(3, 10)

                    damage *= self.advantage_element(enemy.elemento, self.character.elemento)

                    self.character.vida = self.character.vida - damage

                    print(
                        Fore.RED +
                        f"{enemy.nome} te atacou e causou {damage} de dano!" +
                        Style.RESET_ALL
                    )
                
            display.press_enter()


    # Functionality:
    #   Select and returns an enemy.
    def select_enemy(self) -> Enemy:
        
        alive_enemies = [enemy for enemy in self.enemies if enemy.vida > 0 and enemy.vida != 0]
        if not alive_enemies:
            return None
        if len(alive_enemies) == 1:
            return alive_enemies[0]
        enemy_i = main.ask(alive_enemies, lambda: [
            display.clear_screen(),
            display.interface_show_enemies(alive_enemies)
        ], False)
        return alive_enemies[enemy_i - 1]

    # Functionality
    #   Check if combat has terminated.
    def check_combat_end(self) -> bool:
        if self.character.vida <= 0:
            print(
                Fore.RED +
                "Você foi derrotado..." +
                Style.RESET_ALL
            )
            print(
                Fore.RED +
                "Seus esforços foram em vão, assim como sua estadia nesse mundo, seja apagado da realidade..." +
                Style.RESET_ALL
            )
            display.press_enter()
            return None
        
        # Check if all enemies are dead.
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
                "Fugir"
            ]
            
            spells = query.get_damage_spells(self.conn, self.character.id) + query.get_damage_area_spells(self.conn, self.character.id) + query.get_healing_spells(self.conn, self.character.id)
            usable_spells = [
                spell for spell in spells if spell[3] <= self.character.energia_arcana
            ]
            
            potions = query.get_potions(self.conn, self.character.id)
            
            if len(potions) > 0:
                options.append("Usar Poção")
                
            if len(usable_spells) > 0:
                options.append("Usar Feitiço")

            option_i = main.ask(options, lambda: [
                display.clear_screen(),
                display.header(self.character),
                display.interface_show_enemies(self.enemies),
                display.list_options(options)
            ], False)
            
            option = options[option_i - 1]

            
            if option == "Atacar":
                enemy = self.select_enemy()
                damage_caused = self.attack(enemy)
                enemy.vida -= damage_caused
                print(
                    Fore.BLUE +
                    f"{enemy.nome} recebeu {damage_caused} de dano!" +
                    Style.RESET_ALL
                )
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
                
                spell = self.get_spell(usable_spells)
                
                self.apply_spell_effect(spell)
                
                # debug(self.character.energia_arcana)
                # display.press_enter()

            elif option == "Usar Poção":
                potion = self.get_potion(potions)
                if potion == None:
                    continue
                #print(potion)
                #display.press_enter()
                query.update_item_instance(self.conn, potion[0], True)
                self.character.update(self.character.id)

            self.enemies_turn()
            query.update_combat(self.conn, self.enemies, self.character)
            
            result_combat = self.check_combat_end()
            
            # Character killed all enemies.
            if result_combat:
                query.end_combat(self.conn, self.character.id)
                return True
            
            # Character has died.
            elif result_combat == None:
                return result_combat