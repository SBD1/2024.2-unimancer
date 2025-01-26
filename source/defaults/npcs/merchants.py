from database import Database
from utils import debug

def merchants(db: Database):

    try:
        db.cur.execute("SELECT id, nome FROM npc WHERE tipo = 'Civil'")
        npcs = {npc[1]: npc[0] for npc in db.cur.fetchall()}
        debug(f"Fetched NPCs for mercador: {npcs}")

        mercadores = [
            (
                "Jason",
                1,
                "Vendo acessorios",
                None,
                "...Dialogo..."
            ),
            (
                "Nico",
                1,
                "Vendo espadas",
                None,
                "...Dialogo..."
            ),
        ]
        
        db.cur.executemany(
            """
            SELECT criar_mercador(%s, %s::INT, %s, %s::INT, %s)
            """, mercadores
        )

        debug("default: mercador added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding mercador: {e}")