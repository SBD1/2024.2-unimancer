import random
from colorama import Fore, Style, init

class Inimigo:
    def __init__(self, nome, id, armazenamento_id, descricao, elemento, vida_maxima, xp_obtido, inteligencia, moedas_obtidas, conhecimento_arcano, energia_arcana_maxima):
        self.id = id
        self.nome = nome
        self.armazenamento_id = armazenamento_id
        self.descricao = descricao
        self.elemento = elemento
        self.vida = vida_maxima
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
        

    def atacar(self):
        dano_causado = random.randint(10, 20) ## pode variar de acordo com nivel
        self.inimigo.vida -= dano_causado
        print(f"Você atacou e causou {dano_causado} de dano ao inimigo!")

    def usar_pocao(self):
        pass
        ## veificar se foi pocao de dano, cura

    def usar_feitico(self):
        pass
        ## usa um feitico

    def fugir(self):
        chance_fuga = random.random()
        if chance_fuga > 0.5:
            self.combate_ativo = False
            print("Você conseguiu fugir!")
        else:
            print("O inimigo nao deixou voce fugir!")

    def turno_inimigo(self):
        if self.inimigo.vida > 0:
            print(Style.BRIGHT + Fore.YELLOW + "\n--- Turno Inimigo ---" + Style.RESET_ALL)
            dano_recebido = random.randint(5, 15)
            self.personagem.vida -= dano_recebido
            print(f"O inimigo te atacou e causou {dano_recebido} de dano!")
        else:
            print("O inimigo foi derrotado!")

    def verificar_fim(self):
        if self.personagem.vida <= 0:
            self.combate_ativo = False
            print("Você foi derrotado!")
        elif self.inimigo.vida <= 0:
            self.combate_ativo = False

    def iniciar(self):
        while self.combate_ativo:
            print("---------------------------------------------------------------")
            print(f"{self.personagem.nome}: {self.personagem.vida} HP")
            print(f"{self.inimigo.nome}: {self.inimigo.vida} HP\n")
            print("---------------------------------------------------------------\n")
            print(Style.BRIGHT + Fore.YELLOW + "\n--- Seu Turno ---" + Style.RESET_ALL)
            print("1. Atacar")
            print("2. Usar Poção")
            print("3. Usar Feitiço")
            print("4. Fugir")
            escolha = input("Escolha sua ação: ")
            # clear_screen()

            if escolha == "1":
                self.atacar()
                self.verificar_fim()
                self.turno_inimigo()
                self.verificar_fim()
            elif escolha == "2":
                self.usar_pocao()
                self.verificar_fim()
                self.turno_inimigo()
                self.verificar_fim()
            elif escolha == "3":
                self.usar_feitico()
                self.verificar_fim()
                self.turno_inimigo()
                self.verificar_fim()
            elif escolha == "4":
                self.fugir()
                self.verificar_fim()
                self.turno_inimigo()
                self.verificar_fim()
            else:
                print("Escolha inválida!")

        if self.inimigo.vida <= 0:
            print("Você venceu o combate!")
            input("Pressione Enter para continuar...")
            xp_ganho = self.inimigo.xp_obtido
            with self.conn.cursor() as cursor:
                cursor.execute("""SELECT finalizar_combate (%s, %s, %s, %s, %s)""", 
                           (self.personagem.id, xp_ganho, 0, 0, 1))
                self.conn.commit()

