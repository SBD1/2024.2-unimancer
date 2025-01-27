from database import Database
from database.defaults.storage.storage import storage
from utils import debug, error
from colorama import Style

def quester(quester_name: str, db: Database) -> int:
    db.cur.execute(
        f"""
        SELECT quester.id
        FROM quester
        INNER JOIN npc ON quester.id = npc.id
        WHERE nome = '{quester_name}';
        """
    )
    return db.cur.fetchone()[0]

def quests(db: Database):
    
    table_name = Style.BRIGHT + "QUEST" + Style.NORMAL

    try:
        ancient_id = quester("Ancião", db)
    
        
        values = [
            (
                ancient_id,
                storage("Chapéu do Vento Frio", 1, db),
                "Peste de Ratos",
                "Elimine os ratos que estão infestando a região!",
                50,
                "Iniciante"
            ),
            (
                ancient_id,
                storage("Manto de Neve Encantado", 2, db),
                "Ruínas do Abismo Atterrorizada",
                "Expulse o chefe que está aterrorizando os mercadores!",
                250,
                "Fácil"
            ),
        ]
        db.cur.executemany(
            """
            INSERT INTO quest(quester_id, armazenamento_id, titulo, descricao, recompensa, dificuldade)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, values
        )

        db.conn.commit()
        debug(f"default: {len(table_name)} {table_name} added successfully!")
        
        return len(table_name)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")