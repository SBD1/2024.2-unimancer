from database import Database
from utils import debug

def questers(db: Database):

    try:
        db.cur.execute("SELECT id, nome FROM npc WHERE tipo = 'Civil'")
        npcs = {npc[1]: npc[0] for npc in db.cur.fetchall()}
        debug(f"Fetched NPCs for questers: {npcs}")

        questers = [
            (
                "Arius",
                3,
                "Bem-vindo, jovem. Você deseja embarcar em uma jornada?",
                "...Dialogo..."
            ),
            (
                "Elysia",
                2,
                "Eu vi algo estranho nas montanhas... Está preparado?",
                "...Dialogo..."
            ),
            (
                "Isolde",
                1,
                "Você está pronto para enfrentar o que há de mais perigoso neste mundo?",
                "...Dialogo..."
            ),
            (
                "Kael",
                4,
                "Tenho algumas pistas para você, mas isso vai exigir coragem.",
                "...Dialogo..."
            ),
        ]
        
        db.cur.executemany(
            """
            SELECT criar_quester(%s, %s::INT, %s, %s)
            """, questers
        )

        debug("default: Questers added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding Questers: {e}")