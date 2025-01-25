from database import Database
from utils import debug

def npc(db: Database):
    try:

        npcs = [
            ("Paulo", "Civil"),
            ("Natan", "Civil"),
            ("João", "Civil"),
            ("Renan", "Civil"),
            ("Millena", "Civil"),
            ("Arius", "Civil"),
            ("Elysia", "Civil"),
            ("Isolde", "Civil"),
            ("Kael", "Civil"),
            ("Jason", "Civil"),
            ("Nico", "Civil"),
        ]

        db.cur.executemany(
            """
            INSERT INTO npc (nome, tipo)
            VALUES (%s, %s)
            """, npcs
        )
        debug("default: NPCs added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding NPCs: {e}")
