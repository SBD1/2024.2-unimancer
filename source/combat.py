import random
from colorama import Fore, Style
import time

# 1.4x vantagem
# 0.6x desvantagem

# Fogo > Ar 
# Agua > Fogo
# Terra > Agua 
# Ar > Terra 
# Trevas > Luz 
# Luz > Trevas 

class Inimigo:
    def __init__(self, nome, id, armazenamento_id, descricao, elemento, vida, vida_maxima, xp_obtido, inteligencia, moedas_obtidas, conhecimento_arcano, energia_arcana_maxima):
        self.id = id
        self.nome = nome
        self.armazenamento_id = armazenamento_id
        self.descricao = descricao
        self.elemento = elemento
        self.vida = vida
        self.vida_maxima = vida_maxima
        self.xp_obtido = xp_obtido
        self.inteligencia = inteligencia
        self.moedas_obtidas = moedas_obtidas
        self.conhecimento_arcano = conhecimento_arcano
        self.energia_arcana_maxima = energia_arcana_maxima

class Combate:
    def __init__(self, personagem, inimigo, conn):
        self.personagem = personagem
        self.combate_ativo = True

        # Instanciando o inimigo
        self.inimigo = Inimigo(*inimigo)
        self.conn = conn

        self.dano_causado = 0
        self.dano_recebido = 0
    
    def vantagem_elemento(self, elemento1, elemento2):
        vantagens = {
            "Fogo": ["Ar", "Água"],
            "Água": ["Fogo", "Terra"],
            "Terra": ["Água", "Ar"],
            "Ar": ["Terra", "Fogo"],
            "Trevas": ["Luz", "Trevas"],
            "Luz": ["Trevas", "Trevas"]
        }

        if vantagens[elemento1][0] == elemento2:
            return 1.4
        elif vantagens[elemento1][1] == elemento2:
            return 0.6
        else:
            return 1       

    def calcular_chance_fuga(self):
        base_chance = 0.5
        modificador = (self.personagem.inteligencia - self.inimigo.inteligencia) * 0.05
        chance_fuga = base_chance + modificador
        return max(0.8, min(0.9, chance_fuga))
    
    def atacar(self):
        dano_causado = random.randint(50, 60) * self.personagem.nivel
        dano_causado *= self.vantagem_elemento(self.personagem.elemento, self.inimigo.elemento)
        dano_causado = int(dano_causado)
        self.dano_causado = dano_causado
        self.inimigo.vida -= dano_causado
        print(Style.BRIGHT + Fore.RED + f"Você atacou com força e causou {dano_causado} de dano ao inimigo!" + Style.RESET_ALL)

    def usar_pocao(self):
        print(Style.BRIGHT + Fore.CYAN + "Você tentou usar uma poção, mas essa funcionalidade ainda está em desenvolvimento!" + Style.RESET_ALL)

    def usar_feitico(self):
        print(Style.BRIGHT + Fore.CYAN + "Você tentou usar um feitiço, mas essa funcionalidade ainda está em desenvolvimento!" + Style.RESET_ALL)

    def fugir(self):
        chance_fuga = self.calcular_chance_fuga()
        if random.random() < chance_fuga:
            self.combate_ativo = False
            print(Style.BRIGHT + Fore.GREEN + "Você conseguiu escapar do combate!" + Style.RESET_ALL)  
            with self.conn.cursor() as cursor:
                cursor.execute("""SELECT atualizar_combate (%s, %s, %s, %s)""", 
                            (self.personagem.id, self.inimigo.id, self.personagem.vida, self.inimigo.vida))
                self.conn.commit()
            input("Pressione Enter para continuar...")
        else:
            print(Style.BRIGHT + Fore.RED + "O inimigo bloqueou sua tentativa de fuga!" + Style.RESET_ALL)

    def turno_inimigo(self):
        if self.inimigo.vida > 0:
            print(Style.BRIGHT + Fore.YELLOW + "\n--- Turno do Inimigo ---" + Style.RESET_ALL)
            dano_recebido = random.randint(5, 15)
            dano_recebido *= self.vantagem_elemento(self.inimigo.elemento, self.personagem.elemento)
            dano_recebido = int(dano_recebido)
            self.dano_recebido = dano_recebido
            self.personagem.vida -= dano_recebido
            print(Style.BRIGHT + Fore.RED + f"O inimigo atacou e causou {dano_recebido} de dano!" + Style.RESET_ALL )
        else:
            print(Style.BRIGHT + Fore.GREEN + "O inimigo foi derrotado!" + Style.RESET_ALL)

    def verificar_fim(self):
        if self.personagem.vida <= 0:
            self.combate_ativo = False
            print(Style.BRIGHT + Fore.RED + "Você foi derrotado!" + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.RED + "Game Over!" + Style.RESET_ALL)
            input(Fore.YELLOW + "Pressione Enter para continuar..." + Style.RESET_ALL)
                   
        elif self.inimigo.vida <= 0:
            self.combate_ativo = False

    def enemy_delay(self):
        print(Style.BRIGHT + Fore.YELLOW + "O inimigo está pensando..." + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)
        print(Style.BRIGHT + Fore.YELLOW + "..." + Style.RESET_ALL)
        time.sleep(1)

    def iniciar(self):
        while self.combate_ativo:
            print(Style.BRIGHT + Fore.MAGENTA + "---------------------------------------------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + f"{self.personagem.nome}: {self.personagem.vida} HP" + Style.RESET_ALL)
            print(Fore.RED + f"{self.inimigo.nome}: {self.inimigo.vida} HP" + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.MAGENTA + "---------------------------------------------------------------" + Style.RESET_ALL)
            
            # Turno do personagem
            print(Style.BRIGHT + Fore.YELLOW + "--- Seu Turno ---" + Style.RESET_ALL)
            print("1. Atacar")
            print("2. Usar Poção")
            print("3. Usar Feitiço")
            print("4. Fugir")

            escolha = input(Fore.YELLOW + "Escolha sua ação: " + Style.RESET_ALL)

            if escolha == "1":
                self.atacar()
                valido = True
            elif escolha == "2":
                self.usar_pocao()
                valido = True
            elif escolha == "3":
                self.usar_feitico()
                valido = True
            elif escolha == "4":
                self.fugir()
                valido = True
            else:
                print(Style.BRIGHT + Fore.RED + "Escolha inválida!" + Style.RESET_ALL)
                valido = False

            if valido:
                self.verificar_fim()
                if not self.combate_ativo:
                    break

                self.enemy_delay()
                self.turno_inimigo()
                self.verificar_fim()

        if self.inimigo.vida <= 0:
            print(Style.BRIGHT + Fore.GREEN + "Você venceu o combate!" + Style.RESET_ALL)
            input(Fore.YELLOW + "Pressione Enter para continuar..." + Style.RESET_ALL)
            xp_ganho = self.inimigo.xp_obtido
            with self.conn.cursor() as cur:
                cur.execute("""SELECT atualizar_combate (%s, %s, %s, %s)""", 
                            (self.personagem.id, self.inimigo.id, self.personagem.vida, 0))
                self.conn.commit()
                cur.execute("""SELECT finalizar_combate (%s, %s, %s, %s, %s, %s)""", 
                            (self.personagem.id, xp_ganho, 0, self.dano_causado, self.dano_recebido, self.inimigo.id))
                self.conn.commit()
                result = cur.fetchall()
                print(result)
                input(Fore.YELLOW + "Pressione Enter para continuar..." + Style.RESET_ALL)



def verificar_percepcao(personagem, inimigos):
    print(Style.BRIGHT + Fore.YELLOW + "\n--- Verificando Percepção dos Inimigos ---" + Style.RESET_ALL)

    for inimigo in inimigos:
        rolagem_personagem = random.randint(1, 20) + personagem.inteligencia
        rolagem_inimigo = random.randint(1, 20) + inimigo.inteligencia

        print(
            f"Rolagem: {personagem.nome} ({rolagem_personagem}) vs "
            f"{inimigo.nome} ({rolagem_inimigo})"
        )

        if rolagem_inimigo >= rolagem_personagem:
            print(Style.BRIGHT + Fore.RED + f"\nO inimigo {inimigo.nome} percebeu você!" + Style.RESET_ALL)
            return inimigo

    print(Style.BRIGHT + Fore.GREEN + "\nVocê conseguiu evitar os inimigos!" + Style.RESET_ALL)
    return None
