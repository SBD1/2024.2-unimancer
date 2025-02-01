from database import Database
from utils import debug, error
from colorama import Style

def potion_effect(db: Database):

    potion_effect = Style.BRIGHT + "POCAO EFEITO" + Style.NORMAL
    try:
        values = [
            # Elixir da Vida
            (133, 7), # "Raízes da Vida" (Aumenta a recuperação de vida)
            # Mana Líquida
            (134, 5), # "Caminhos Luminosos" (Aumenta regeneração de energia arcana)
            # Poção da Força Titânica
            (135, 9), # "Força Óssea" (Aumenta resistência física e dano crítico)
            # Poção do Vento Celeste
            (136, 3), # "Agilidade das Marés" (Aumenta a velocidade em terrenos aquáticos)
            # Poção da Pele de Pedra
            (137, 2), # "Proteção Dracônica" (Concede resistência moderada a ataques físicos)
            # Lágrima do Dragão
            (138, 8), # "Congelamento Ártico" (Reduz dano recebido de ataques de fogo)
            # Sangue do Fênix
            (139, 10), # "Presença Real" (Bônus em batalhas e ganho de XP)
            # Poção do Tempo Congelado
            (140, 4), # "Sombras Protetoras" (Diminui a chance de ser detectado por inimigos)
            # Elixir da Perdição
            (141, 6), # "Passos Trovejantes" (Causa dano em área ao pular em combate)
            # Néctar do Destino
            (142, 1), # "Passos Silenciosos" (Reduz o ruído ao caminhar)
        ]
        db.cur.executemany(
            """
            INSERT INTO pocao_efeito
            VALUES (%s, %s)
            """, values
        )

        db.conn.commit()
        debug(f"default: {len(values)} {potion_effect} added successfully!")
        
        return len(potion_effect)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {potion_effect}: {e}")
