from database import Database
from utils import debug

def merchant(db: Database):

    try:
        db.cur.execute("SELECT id, nome FROM npc WHERE tipo = 'Civil'")
        npcs = {npc[1]: npc[0] for npc in db.cur.fetchall()}
        debug(f"Fetched NPCs for mercador: {npcs}")

        mercador = [
            (npcs["Jason"], "Vendo acessorios"),
            (npcs["Nico"], "Vendo espadas"),
        ]
        
        db.cur.executemany(
            """
            INSERT INTO mercador (id, dialogo)
            VALUES (%s, %s)
            """, mercador
        )

        debug("default: mercador added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding mercador: {e}")