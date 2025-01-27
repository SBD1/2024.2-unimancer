from database import Database
from utils import debug, error
from colorama import Style

def area_spells(db: Database):
    table_name = Style.BRIGHT + "FEITICO_DANO_AREA" + Style.NORMAL
    try:
        default_values = [
            # Água
            (
                "Sopro Congelante: Exala um vento gelado que congela os inimigos em uma ampla área, causando dano e reduzindo sua velocidade.",
                "Água",
                2,
                5,
                5,
                10,   
                3     
            ),
            (
                "Muralha Gélida: Cria uma barreira de gelo ao redor do mago, danificando e desacelerando todos os inimigos que a atravessam.",
                "Água",
                4,
                10,
                8,
                20,
                5
            ),
            (
                "Nevasca Intensa: Invoca uma tempestade de neve que causa dano contínuo aos inimigos dentro de sua área de efeito.",
                "Água",
                6,
                15,
                12,
                25,
                6
            ),
            (
                "Tempestade Glacial: Desencadeia uma poderosa tempestade de gelo que atinge múltiplos inimigos, causando elevados danos e podendo congelá-los.",
                "Água",
                8,
                20,
                16,
                35,
                7
            ),
            (
                "Dilúvio Ártico: Inunda a área com águas geladas, causando danos massivos e drenando a energia arcana dos inimigos afetados.",
                "Água",
                10,
                25,
                20,
                50,
                10
            ),

            # Fogo
            (
                "Labareda Inicial: Lança chamas suaves que atingem uma área moderada, causando danos contínuos aos inimigos presentes.",
                "Fogo",
                2,
                5,
                5,
                10,
                3
            ),
            (
                "Explosão Ígnea: Detona uma explosão de fogo que causa dano elevado a todos os inimigos em uma grande área.",
                "Fogo",
                4,
                10,
                8,
                20,
                5
            ),
            (
                "Chamas Medonhas: Invoca chamas negras que envolvem a área alvo, causando dano constante e reduzindo a resistência dos inimigos.",
                "Fogo",
                6,
                15,
                12,
                25,
                6
            ),
            (
                "Inferno Crescente: Desencadeia um inferno que se expande progressivamente, aumentando o dano conforme avança sobre os inimigos.",
                "Fogo",
                8,
                20,
                16,
                35,
                7
            ),
            (
                "Apocalipse de Fogo: Invoca uma catástrofe de chamas que devasta uma vasta área, causando danos massivos e incendiando o terreno.",
                "Fogo",
                10,
                25,
                20,
                50,
                10
            ),

            # Terra
            (
                "Tremor Raso: Provoca um leve tremor que atinge todos os inimigos próximos, causando danos moderados e desequilibrando suas defesas.",
                "Terra",
                2,
                5,
                5,
                10,
                3
            ),
            (
                "Ondas Sísmicas: Envia ondas de choque pelo solo, danificando e desestabilizando múltiplos inimigos na área.",
                "Terra",
                4,
                10,
                8,
                20,
                5
            ),
            (
                "Espiral Rochosa: Invoca espinhos de pedra que giram em torno do mago, atingindo todos os inimigos presentes na área de efeito.",
                "Terra",
                6,
                15,
                12,
                25,
                6
            ),
            (
                "Avalanche Subterrânea: Desencadeia uma avalanche de pedras e terra que esmagam e causam danos severos aos inimigos na região afetada.",
                "Terra",
                8,
                20,
                16,
                35,
                7
            ),
            (
                "Cataclismo Terrestre: Provoca uma devastadora ruptura na terra, causando danos massivos e alterando a topografia da área de combate.",
                "Terra",
                10,
                25,
                20,
                50,
                10
            ),

            # Ar
            (
                "Vento Cortante: Lança rajadas de vento afiadas que cortam e causam danos a todos os inimigos na área alvo.",
                "Ar",
                2,
                5,
                5,
                10,
                3
            ),
            (
                "Tornado Enfurecido: Invoca um tornado violento que percorre a área, causando danos constantes e desorganizando as formações inimigas.",
                "Ar",
                4,
                10,
                8,
                20,
                5
            ),
            (
                "Furacão Impiedoso: Desencadeia um furacão devastador que arrasta e fere todos os inimigos atingidos dentro de sua vasta área de impacto.",
                "Ar",
                6,
                15,
                12,
                25,
                6
            ),
            (
                "Ciclone Ascendente: Cria um ciclone poderoso que sobe rapidamente, causando danos intensos e espalhando destruição por toda a área afetada.",
                "Ar",
                8,
                20,
                16,
                35,
                7
            ),
            (
                "Tempestade Celeste: Invoca uma tempestade de ventos celestiais que atinge múltiplos inimigos com rajadas de ar cortante e relâmpagos.",
                "Ar",
                10,
                25,
                20,
                50,
                10
            ),

            # Luz
            (
                "Clarão Ofuscante: Emite um brilho intenso que cega e causa danos leves a todos os inimigos na área alvo.",
                "Luz",
                2,
                5,
                5,
                10,
                3
            ),
            (
                "Arco Luminoso: Cria um arco de luz brilhante que dispara feixes de energia luminosa, danificando múltiplos inimigos.",
                "Luz",
                4,
                10,
                8,
                20,
                5
            ),
            (
                "Chuva Reluzente: Desce uma chuva de raios de luz que atinge uma área ampla, causando danos contínuos e curando aliados próximos.",
                "Luz",
                6,
                15,
                12,
                25,
                6
            ),
            (
                "Brilho Divino: Envolve a área com uma aura divina que causa danos elevados aos inimigos e aumenta a resistência dos aliados.",
                "Luz",
                8,
                20,
                16,
                35,
                7
            ),
            (
                "Êxtase Solar: Libera um poderoso estalo de luz solar que incendeia e causa danos massivos a todos os inimigos na área de efeito.",
                "Luz",
                10,
                25,
                20,
                50,
                10
            ),

            # Trevas
            (
                "Sussurro das Sombras: Murmura palavras sombrias que envolvem a área, causando danos leves e enfraquecendo a moral dos inimigos.",
                "Trevas",
                2,
                5,
                5,
                10,
                3
            ),
            (
                "Poço Profano: Cria um vórtice de trevas que atrai e danifica todos os inimigos que se aproximam, drenando sua energia vital.",
                "Trevas",
                4,
                10,
                8,
                20,
                5
            ),
            (
                "Aura Maldita: Propaga uma aura de maldição que causa danos contínuos e reduz a eficácia das habilidades dos inimigos na área.",
                "Trevas",
                6,
                15,
                12,
                25,
                6
            ),
            (
                "Tormenta Sombria: Desencadeia uma tempestade de trevas que atinge múltiplos inimigos, causando danos intensos e drenando sua energia arcana.",
                "Trevas",
                8,
                20,
                16,
                35,
                7
            ),
            (
                "Abismo Final: Invoca um abismo de trevas que consome tudo ao seu redor, causando danos devastadores e eliminando inimigos em grande número.",
                "Trevas",
                10,
                25,
                20,
                50,
                10
            ),
        ]

        db.cur.executemany(
            """
            SELECT criar_feitico_dano_area(%s, %s, %s::INT, %s::INT, %s::INT, %s::INT, %s::INT)
            """,
            default_values
        )
        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")