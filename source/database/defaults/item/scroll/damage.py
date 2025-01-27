from database import Database
from utils import debug, error
from colorama import Style

def damage_spells(db: Database):
    table_name = Style.BRIGHT + "FEITICO_DANO" + Style.NORMAL
    try:
        default_values = [
            # Água
            (
                "Jato de Água: Lança um jato de água pressurizada que causa danos moderados a um único inimigo.",
                "Água",
                2,
                5,
                10,
                15  
            ),
            (
                "Maremoto: Invoca uma grande onda que atinge vários inimigos, causando danos elevados.",
                "Água",
                5,
                12,
                20,
                30
            ),
            (
                "Tsunami: Desencadeia um tsunami devastador que causa danos massivos e empurra os inimigos para longe.",
                "Água",
                8,
                20,
                30,
                50
            ),

            # Fogo
            (
                "Bola de Fogo: Lança uma bola de fogo explosiva que causa danos intensos a todos os inimigos em uma área.",
                "Fogo",
                2,
                5,
                10,
                20
            ),
            (
                "Chuva de Fogo: Desce uma chuva de chamas sobre a área alvo, causando danos contínuos aos inimigos.",
                "Fogo",
                5,
                12,
                20,
                35
            ),
            (
                "Inferno Abrasador: Cria um inferno que queima intensamente, causando danos massivos e queimaduras persistentes.",
                "Fogo",
                8,
                20,
                30,
                60
            ),

            # Terra
            (
                "Saco de Pedra: Arremessa grandes pedras contra os inimigos, causando danos pesados a um único alvo.",
                "Terra",
                2,
                5,
                10,
                18
            ),
            (
                "Terremoto: Provoca um terremoto que atinge múltiplos inimigos, causando danos significativos e desequilibrando suas posições.",
                "Terra",
                5,
                12,
                20,
                35
            ),
            (
                "Coluna de Terra: Erige uma coluna gigante de terra que danifica severamente todos os inimigos ao seu redor.",
                "Terra",
                8,
                20,
                30,
                50
            ),

            # Ar
            (
                "Rajada Voadora: Lança uma forte rajada de vento que causa danos e empurra os inimigos para trás.",
                "Ar",
                2,
                5,
                10,
                15
            ),
            (
                "Tempestade de Vento: Invoca uma tempestade de vento que atinge vários inimigos, causando danos contínuos.",
                "Ar",
                5,
                12,
                20,
                30
            ),
            (
                "Furacão Violento: Desencadeia um furacão poderoso que causa danos massivos e desorienta todos os inimigos na área afetada.",
                "Ar",
                8,
                20,
                30,
                50
            ),

            # Luz
            (
                "Raio Luminoso: Dispara um raio de luz intensa que causa danos a um único inimigo.",
                "Luz",
                2,
                5,
                10,
                15
            ),
            (
                "Explosão Solar: Cria uma explosão de luz solar que atinge vários inimigos, causando danos elevados.",
                "Luz",
                5,
                12,
                20,
                30
            ),
            (
                "Eclipse Radiante: Invoca um eclipse de luz que causa danos massivos e cega temporariamente os inimigos na área.",
                "Luz",
                8,
                20,
                30,
                50
            ),

            # Trevas
            (
                "Sombras Cortantes: Lança sombras afiadas que causam danos contínuos a múltiplos inimigos.",
                "Trevas",
                2,
                5,
                10,
                15
            ),
            (
                "Torretas Obscuras: Invoca torretas de trevas que atacam automaticamente os inimigos nas proximidades, causando danos regulares.",
                "Trevas",
                5,
                12,
                20,
                30
            ),
            (
                "Tempestade Sombria: Desencadeia uma tempestade de trevas que envolve a área, causando danos intensos e drenando a energia arcana dos inimigos.",
                "Trevas",
                8,
                20,
                30,
                50
            ),
        ]

        db.cur.executemany(
            """
            SELECT criar_feitico_dano(%s, %s, %s, %s, %s, %s)
            """,
            default_values
        )
        
        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values:\n{e}")