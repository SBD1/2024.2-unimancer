from database import Database
from utils import debug

def citizens(db: Database):
    try:
        db.cur.execute("SELECT id, nome FROM npc")
        npcs = {npc[1]: npc[0] for npc in db.cur.fetchall()}
        debug(f"Fetched NPCs: {npcs}")

        civis = [
            ("Paulo", 4, "Um homem que passa o tempo observando os magos."),
            ("Natan", 2, "Um indivíduo que frequentemente passa pela cidade, sem muito a dizer."),
            ("João", 2, "Um indivíduo que parece estar sempre ocupado com suas próprias tarefas."),
            ("Renan", 4, "Visto frequentemente perto do rio, pescando ou relaxando."),
            ("Millena", 5, "Uma pessoa tranquila que observa o movimento da cidade sem se envolver."),
        ]
        db.cur.executemany(
            """
            SELECT criar_civil(%s, %s::INT, %s, 'Civil')
            """, civis
        )

        db.conn.commit()
        debug("default: Civils added successfully!")
        

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding Civils: {e}")
