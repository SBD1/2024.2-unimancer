from database import Database
from utils import debug, error
from colorama import Style

def create_enemy_instances(db: Database):
    
    table_name = Style.BRIGHT + "INIMIGO_INSTANCIA" + Style.NORMAL
    
    try:
        enemy_instances = [
            # Floresta Eterna
            (4, 1, 50),  # TESTE
            (4, 5, 50),  # Lobo Sombrio - Clareira dos Espíritos
            (5, 5, 40),  # Espírito da Clareira - Clareira dos Espíritos
            (6, 6, 70),  # Ent Ancião - Bosque Sombrio
            (7, 6, 80),  # Guardião de Pedra - Bosque Sombrio
            (8, 7, 60),  # Serpente das Sombras - Lago da Serenidade
            (9, 8, 50),  # Espectro do Abismo - Ruínas Perdidas

            # Ruínas do Abismo
            (10, 9, 90),  # Escorpião Gigante - Fenda do Abismo
            (11, 9, 60),  # Djin Traiçoeiro - Fenda do Abismo
            (12, 10, 70),  # Caravaneiro Corrompido - Praça das Estátuas
            (13, 12, 150),  # Golem de Cristal - Santuário Perdido
            (14, 12, 80),  # Minerador Fantasma - Santuário Perdido

            # Deserto de Areias Infinitas
            (15, 13, 100),  # Afortunado - Oásis dos Mercadores
            (16, 14, 120),  # Gigante Congelado - Vale das Serpentes
            (17, 14, 80),  # Águia do Crepúsculo - Vale das Serpentes
            (18, 15, 70),  # Espírito da Geada - Ruínas Submersas

            # Caverna Cristalizada
            (19, 17, 70),  # Guerreiro Esqueleto - Trono de Cristal
            (20, 17, 60),  # Feiticeiro Esqueleto - Trono de Cristal
            (21, 18, 50),  # Goblin Zumbi - Núcleo Cristalino

            # Montanha do Crepúsculo
            (22, 21, 100),  # Guerreiro Corrompido - Pico Congelado
            (23, 22, 110),  # Fera Flamejante - Vilarejo dos Gigantes

            # Caverna Soterrada
            (24, 25, 200),  # Dragão da Devastação - Vila Esquecida

            # Bosses
            (25, 9, 150), # Abgail -> Fenda do Abismo
            (26, 17, 180), # Lumina -> Trono Cristalizado
            (27, 25, 200), # Necromante -> Vila Esquecida
            (28, 29, 220) # Nosferus -> Catedral Queimada
        ]
        db.cur.executemany(
            """
                INSERT INTO inimigo_instancia (inimigo_id, sub_regiao_id, vida)
                VALUES (%s, %s, %s)
            """, enemy_instances
        )
        db.conn.commit()
        debug(f"default: {len(table_name)} {table_name} added successfully!")
        
        return len(table_name)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")