class Enemy:
    def __init__ (self, id, nome, descricao, elemento, vida, vida_maxima, xp_obtido, inteligencia, moedas_obtidas, conhecimento_arcano, energia_arcana_maxima, dialogo, emoji):
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
        self.dialogo = dialogo
        self.emoji = emoji