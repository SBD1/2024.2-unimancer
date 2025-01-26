import random

class Combate:
    def __init__(self, personagem, inimigo, conn):
        self.personagem = personagem
        self.inimigo = inimigo
        self.combate_ativo = True

    def atacar(self):
        dano_causado = random.randint(10, 20) ## pode variar de acordo com nivel
        self.inimigo.vida -= dano_causado
        print(f"Você atacou e causou {dano_causado} de dano ao inimigo!")

    def usar_pocao(self):
        ## veificar se foi pocao de dano, cura

    def usar_feitico(self):
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
            dano_recebido = random.randint(5, 15)
            self.personagem.vida -= dano_recebido
            print(f"O inimigo te atacou e causou {dano_recebido} de dano!")
        else:
            print("O inimigo foi derrotado!")

    def verificar_fim(self):
        if self.personagem.vida <= 0:
            self.combate_ativo = False
            print("Você foi derrotado!")
        elif self.inimigo["vida"] <= 0:
            self.combate_ativo = False
            print("Você venceu o combate!")

    def iniciar(self):
        while self.combate_ativo:
            print("\n--- Seu turno ---")
            print("1. Atacar")
            print("2. Usar Poção")
            print("3. Usar Feitiço")
            print("4. Fugir")
            escolha = input("Escolha sua ação: ")

            if escolha == "1":
                self.atacar()
            elif escolha == "2":
                self.usar_pocao()
            elif escolha == "3":
                self.usar_feitico()
            elif escolha == "4":
                self.fugir()
            else:
                print("Escolha inválida!")

            self.verificar_fim()
            if not self.combate_ativo:
                break

            print("\n--- Turno do inimigo ---")
            self.turno_inimigo()
            self.verificar_fim()

        if self.inimigo["vida"] <= 0:
            xp_ganho = self.inimigo.xp
            self.conn.execute("""SELECT criar_combate (%s, %s, %s, %s)""",(self.personagem.id, xp_ganho, 0,0))

