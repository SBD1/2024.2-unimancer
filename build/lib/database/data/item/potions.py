from database import Database
from utils import debug, error
from colorama import Style

def potions(db: Database):
    
    table_name = Style.BRIGHT + "POCAO" + Style.NORMAL
    try:
        values = [
            ("Elixir da Vida", 4, "Cura Pequena", 1, 50, 2), 
            ("Mana Líquida", 5, "Recuperação Arcana", 1, 75, 3),
            ("Poção da Força Titânica", 4, "Aumento de Força", 2, 100, 4),
            ("Poção do Vento Celeste", 3, "Velocidade Extra", 1, 90, 3),
            ("Poção da Pele de Pedra", 5, "Defesa Temporária", 2, 120, 5),
            ("Lágrima do Dragão", 6, "Regeneração Poderosa", 2, 200, 6),
            ("Sangue do Fênix", 9, "Ressurreição", 3, 500, 8),
            ("Poção do Tempo Congelado", 10, "Paralisação Temporal", 3, 350, 3),
            ("Elixir da Perdição", 10, "Dano Sombrio", 5, 180, 2),
            ("Néctar do Destino", 14, "Sorte Abençoada", 4, 150, 4)
        ]
        db.cur.executemany(
            """
            SELECT criar_pocao (%s, %s, %s, %s, %s, %s)
            """, values
        )

        db.conn.commit()
        debug(f"default: {len(values)} {table_name} added successfully!")
        
        return len(table_name)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")