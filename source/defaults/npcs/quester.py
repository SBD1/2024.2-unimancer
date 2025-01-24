from database import Database
from utils import debug

def quester(db: Database):

    try:
        db.cur.execute("SELECT id, nome FROM npc WHERE tipo = 'Civil'")
        npcs = {npc[1]: npc[0] for npc in db.cur.fetchall()}
        debug(f"Fetched NPCs for questers: {npcs}")

        questers = [
            (npcs["Arius"], "Bem-vindo, jovem. Você deseja embarcar em uma jornada?", 3),
            (npcs["ELysia"], "Eu vi algo estranho nas montanhas... Está preparado?", 2),
            (npcs["Isolde"], "Você está pronto para enfrentar o que há de mais perigoso neste mundo?", 1),
            (npcs["Kael"], "Tenho algumas pistas para você, mas isso vai exigir coragem.", 4),
        ]
        
        db.cur.executemany(
            """
            INSERT INTO quester (id, dialogo, num_quests)
            VALUES (%s, %s, %s)
            """, questers
        )

        debug("default: Questers added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding Questers: {e}")