from database import Database
from utils import debug

def sub_regions(db: Database):
    try:
        db.cur.execute("SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer'")
        regiao_id = db.cur.fetchone()[0]

        # insert subregions
        default_subregions = [
            (regiao_id, None, "Ferraria Albnur", "Local de trabalho árduo onde ferramentas e armas são forjadas."),
            (regiao_id, None, "Praça Central", "O coração do vilarejo, cheio de vida e comércio."),
            (regiao_id, None, "Casa do Ancião", "Uma casa tranquila que guarda histórias e conselhos sábios."),
            (regiao_id, None, "Taberna da Caneca Partida", "Um refúgio caloroso para diversão e descanso.")
        ]
        db.cur.executemany(
            """
            INSERT INTO sub_regiao (regiao_id, armazenamento_id, nome, descricao)
            VALUES (%s, %s, %s, %s)
            """, default_subregions
        )
        debug("default: Subregions added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *TABLE* values: {e}")
