from database import Database
from utils import debug

def civil(db: Database):
    try:
        db.cur.execute("SELECT id, nome FROM npc")
        npcs = {npc[1]: npc[0] for npc in db.cur.fetchall()}
        debug(f"Fetched NPCs: {npcs}")

        civis = [
            (npcs["Paulo"], 4, "Um homem que passa o tempo observando os magos.", None),
            (npcs["Natan"], 2, "Um indivíduo que frequentemente passa pela cidade, sem muito a dizer.", None),
            (npcs["João"], 2, "Um indivíduo que parece estar sempre ocupado com suas próprias tarefas.", None),
            (npcs["Renan"], 4, "Visto frequentemente perto do rio, pescando ou relaxando.", None),
            (npcs["Millena"], 5, "Uma pessoa tranquila que observa o movimento da cidade sem se envolver.", None),
            (npcs["Arius"], 1, "Um homem que parece estar sempre em busca de algo.", "Quester"),
            (npcs["Elysia"], 3, "Uma mulher que parece estar sempre em busca de algo.", "Quester"),
            (npcs["Isolde"], 1, "Uma mulher que parece estar sempre em busca de algo.", "Quester"),
            (npcs["Kael"], 4, "Um homem que parece estar sempre em busca de algo.", "Quester"),
            (npcs["Jason"], 4, "Um homem que parece estar sempre em busca de algo.", "Mercador"),
            (npcs["Nico"], 4, "Um homem que parece estar sempre em busca de algo.", "Mercador"),
        ]
        db.cur.executemany(""" SELECT criar_civil(%s, %s, %s, %s) """,civis)

        db.conn.commit()
        debug("default: Civils added successfully!")
        

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding Civils: {e}")
