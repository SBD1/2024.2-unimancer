from doctest import debug_script
from database import Database
from utils import debug, error
from colorama import Style

def potions(db: Database):
    
    table_name = Style.BRIGHT + "POCAO" + Style.NORMAL
    try:
        values = [
            ("Elixir da Vida", 4, "Cura Pequena", 1, 50), 
            ("Mana Líquida", 5, "Recuperação Arcana", 1, 75),
            ("Poção da Força Titânica", 4, "Aumento de Força", 2, 100),
            ("Poção do Vento Celeste", 3, "Velocidade Extra", 1, 90),
            ("Poção da Pele de Pedra", 5, "Defesa Temporária", 2, 120),
            ("Lágrima do Dragão", 6, "Regeneração Poderosa", 2, 200),
            ("Sangue do Fênix", 9, "Ressurreição", 3, 500),
            ("Poção do Tempo Congelado", 10, "Paralisação Temporal", 3, 350),
            ("Elixir da Perdição", 10, "Dano Sombrio", 5, 180),
            ("Néctar do Destino", 14, "Sorte Abençoada", 4, 150)
        ]
        for (name, p_drop_inimigos_media, description, weight, price) in values:
            db.cur.execute(
                f"""
                SELECT criar_pocao (
                    '{description}',
                    {p_drop_inimigos_media},
                    '{name}',
                    {weight},
                    {price}
                );
                """
            )

        db.conn.commit()
        debug(f"default: {len(values)} {table_name} added successfully!")
        
        return len(table_name)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")