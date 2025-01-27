from database import Database
from utils import debug, error
from colorama import Style

def insert_spell_requirements(db: Database):
    table_name = Style.BRIGHT + "FEITICO_REQUERIMENTO" + Style.NORMAL
    try:
        # Lista de feitiços ordenados por elemento e nível
        # Assumindo que os IDs dos feitiços começam em 1 e são inseridos na ordem acima
        # Cada feitiço após o primeiro de cada elemento terá o anterior como pré-requisito

        requisitos_area = [
            # Água
            (1, 2),  # Sopro Congelante → Muralha Gélida
            (2, 3),  # Muralha Gélida → Nevasca Intensa
            (3, 4),  # Nevasca Intensa → Tempestade Glacial
            (4, 5),  # Tempestade Glacial → Dilúvio Ártico

            # Fogo
            (6, 7),  # Labareda Inicial → Explosão Ígnea
            (7, 8),  # Explosão Ígnea → Chamas Medonhas
            (8, 9),  # Chamas Medonhas → Inferno Crescente
            (9, 10), # Inferno Crescente → Apocalipse de Fogo

            # Terra
            (11, 12), # Tremor Raso → Ondas Sísmicas
            (12, 13), # Ondas Sísmicas → Espiral Rochosa
            (13, 14), # Espiral Rochosa → Avalanche Subterrânea
            (14, 15), # Avalanche Subterrânea → Cataclismo Terrestre

            # Ar
            (16, 17), # Vento Cortante → Tornado Enfurecido
            (17, 18), # Tornado Enfurecido → Furacão Impiedoso
            (18, 19), # Furacão Impiedoso → Ciclone Ascendente
            (19, 20), # Ciclone Ascendente → Tempestade Celeste

            # Luz
            (21, 22), # Clarão Ofuscante → Arco Luminoso
            (22, 23), # Arco Luminoso → Chuva Reluzente
            (23, 24), # Chuva Reluzente → Brilho Divino
            (24, 25), # Brilho Divino → Êxtase Solar

            # Trevas
            (26, 27), # Sussurro das Sombras → Poço Profano
            (27, 28), # Poço Profano → Aura Maldita
            (28, 29), # Aura Maldita → Tormenta Sombria
            (29, 30), # Tormenta Sombria → Abismo Final
        ]

        requisitos_cura = [
            # Água
            (31, 32),  # Cura Áquatica → Manto Revitalizante

            # Fogo
            (33, 34),  # Flama Curativa → Fogo Vigoroso

            # Terra
            (35, 36),  # Regeneração Terrena → Escudo Vital

            # Ar
            (37, 38),  # Brisa Curativa → Vórtice Revigorante

            # Luz
            (39, 40),  # Luz Restauradora → Aura Divina

            # Trevas
            (41, 42),  # Sombra Curativa → Véu das Trevas
        ]

        requisitos_dano = [
            # Água
            (43, 44),  # Jato de Água → Maremoto
            (44, 45),  # Maremoto → Tsunami

            # Fogo
            (46, 47),  # Bola de Fogo → Chuva de Fogo
            (47, 48),  # Chuva de Fogo → Inferno Abrasador

            # Terra
            (49, 50),  # Saco de Pedra → Terremoto
            (50, 51),  # Terremoto → Coluna de Terra

            # Ar
            (52, 53),  # Rajada Voadora → Tempestade de Vento
            (53, 54),  # Tempestade de Vento → Furacão Violento

            # Luz
            (55, 56),  # Raio Luminoso → Explosão Solar
            (56, 57),  # Explosão Solar → Eclipse Radiante

            # Trevas
            (58, 59),  # Sombras Cortantes → Torretas Obscuras
            (59, 60),  # Torretas Obscuras → Tempestade Sombria
        ]

        default_values = requisitos_area + requisitos_cura + requisitos_dano # juntando a construção de todos so pre-requisitos

        db.cur.executemany(
            """
            INSERT INTO feitico_requerimento (de_id, para_id)
            VALUES (%s, %s)
            """,
            default_values
        )
        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)
        
        
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")