from database import Database
from utils import debug, error
from colorama import Style

def writted_scrolls(db: Database, items_total: int):
    
    table_name = Style.BRIGHT + "PERGAMINHO_ESCRITO" + Style.NORMAL
    try:
        
        # Relações entre pergaminhos e feitiços
        default_values = [
            # Pergaminho 1: Elementos Unidos
            (1, 1),  # Elementos Unidos contém Feitico de Dano 1
            (1, 31), # Elementos Unidos contém Feitico de Cura 31
            (1, 43), # Elementos Unidos contém Feitico de Dano 43

            # Pergaminho 2: Harmonia Arcana
            (2, 2),  # Harmonia Arcana contém Feitico de Dano 2
            (2, 32), # Harmonia Arcana contém Feitico de Cura 32
            (2, 44), # Harmonia Arcana contém Feitico de Dano 44

            # Pergaminho 3: Encantos Mistosa
            (3, 3),  # Encantos Mistos contém Feitico de Dano 3
            (3, 33), # Encantos Mistos contém Feitico de Cura 33
            (3, 45), # Encantos Mistos contém Feitico de Dano 45

            # Pergaminho 4: Versatilidade Mágica
            (4, 4),  # Versatilidade Mágica contém Feitico de Dano 4
            (4, 34), # Versatilidade Mágica contém Feitico de Cura 34
            (4, 46), # Versatilidade Mágica contém Feitico de Dano 46

            # Pergaminho 5: Convergência Elemental
            (5, 5),  # Convergência Elemental contém Feitico de Dano 5
            (5, 35), # Convergência Elemental contém Feitico de Cura 35
            (5, 47), # Convergência Elemental contém Feitico de Dano 47

            # Pergaminho 6: Sinergia Arcana
            (6, 6),  # Sinergia Arcana contém Feitico de Dano 6
            (6, 36), # Sinergia Arcana contém Feitico de Cura 36
            (6, 48), # Sinergia Arcana contém Feitico de Dano 48

            # Pergaminho 7: Feitiços Múltiplos
            (7, 7),  # Feitiços Múltiplos contém Feitico de Dano 7
            (7, 37), # Feitiços Múltiplos contém Feitico de Cura 37
            (7, 49), # Feitiços Múltiplos contém Feitico de Dano 49

            # Pergaminho 8: Dualidade Mágica
            (8, 8),  # Dualidade Mágica contém Feitico de Dano 8
            (8, 38), # Dualidade Mágica contém Feitico de Cura 38
            (8, 50), # Dualidade Mágica contém Feitico de Dano 50

            # Pergaminho 9: Poder Compartilhado
            (9, 9),  # Poder Compartilhado contém Feitico de Dano 9
            (9, 39), # Poder Compartilhado contém Feitico de Cura 39
            (9, 51), # Poder Compartilhado contém Feitico de Dano 51

            # Pergaminho 10: Amplificação Mágica
            (10, 10), # Amplificação Mágica contém Feitico de Dano 10
            (10, 40), # Amplificação Mágica contém Feitico de Cura 40
            (10, 52), # Amplificação Mágica contém Feitico de Dano 52

            # Pergaminho 11: Adaptação Arcana
            (11, 11), # Adaptação Arcana contém Feitico de Dano 11
            (11, 41), # Adaptação Arcana contém Feitico de Cura 41
            (11, 53), # Adaptação Arcana contém Feitico de Dano 53

            # Pergaminho 12: Energias Combinadas
            (12, 12), # Energias Combinadas contém Feitico de Dano 12
            (12, 42), # Energias Combinadas contém Feitico de Cura 42
            (12, 54), # Energias Combinadas contém Feitico de Dano 54

            # Pergaminho 13: Resiliência Mágica
            (13, 13), # Resiliência Mágica contém Feitico de Dano 13
            (13, 55), # Resiliência Mágica contém Feitico de Dano 55
            (13, 58), # Resiliência Mágica contém Feitico de Dano 58

            # Pergaminho 14: Fluxo Mágico
            (14, 14), # Fluxo Mágico contém Feitico de Dano 14
            (14, 56), # Fluxo Mágico contém Feitico de Dano 56
            (14, 59), # Fluxo Mágico contém Feitico de Dano 59

            # Pergaminho 15: Estabilidade Arcana
            (15, 15), # Estabilidade Arcana contém Feitico de Dano 15
            (15, 57), # Estabilidade Arcana contém Feitico de Dano 57
            (15, 60), # Estabilidade Arcana contém Feitico de Dano 60

            # Pergaminho 16: Manipulação Mágica
            (16, 16), # Manipulação Mágica contém Feitico de Dano 16
            (16, 17), # Manipulação Mágica contém Feitico de Dano 17
            (16, 18), # Manipulação Mágica contém Feitico de Dano 18

            # Pergaminho 17: Expansão de Feitiços
            (17, 19), # Expansão de Feitiços contém Feitico de Dano 19
            (17, 20), # Expansão de Feitiços contém Feitico de Dano 20
            (17, 21), # Expansão de Feitiços contém Feitico de Dano 21

            # Pergaminho 18: Intensificação
            (18, 22), # Intensificação contém Feitico de Dano 22
            (18, 23), # Intensificação contém Feitico de Dano 23
            (18, 24), # Intensificação contém Feitico de Dano 24

            # Pergaminho 19: Diversificação
            (19, 25), # Diversificação contém Feitico de Dano 25
            (19, 26), # Diversificação contém Feitico de Dano 26
            (19, 27), # Diversificação contém Feitico de Dano 27

            # Pergaminho 20: Conjuração Mista
            (20, 28), # Conjuração Mista contém Feitico de Dano 28
            (20, 29), # Conjuração Mista contém Feitico de Dano 29
            (20, 30), # Conjuração Mista contém Feitico de Dano 30
        ]

        default_values = [(item_id + items_total, feitico_id) for item_id, feitico_id in default_values]

        db.cur.executemany(
            """
            INSERT INTO feitico_escrito(item_id, feitico_id)
            VALUES (%s, %s)
            """,
            default_values
        )
        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values:\n{e}")