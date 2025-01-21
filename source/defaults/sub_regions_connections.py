from database import Database
from utils import debug

# Add something in the database.
def sub_regions_connections(db: Database):
    try:
        db.cur.execute("SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer'")
        regiao_id = db.cur.fetchone()[0]
        
        # get subregions id to link
        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id = {regiao_id}")
        subregion_ids = {row[1]: row[0] for row in db.cur.fetchall()}
        default_connections = [
            (subregion_ids["Ferraria Albnur"], subregion_ids["Praça Central"], "Sul", "Passável"),
            (subregion_ids["Praça Central"], subregion_ids["Ferraria Albnur"], "Norte", "Passável"),
            (subregion_ids["Praça Central"], subregion_ids["Casa do Ancião"], "Oeste", "Passável"),
            (subregion_ids["Casa do Ancião"], subregion_ids["Praça Central"], "Leste", "Passável"),
            (subregion_ids["Praça Central"], subregion_ids["Taberna da Caneca Partida"], "Leste", "Passável"),
            (subregion_ids["Taberna da Caneca Partida"], subregion_ids["Praça Central"], "Oeste", "Passável")
        ]
        db.cur.executemany(
            """
            INSERT INTO sub_regiao_conexao (sub_regiao_1, sub_regiao_2, direcao, situacao)
            VALUES (%s, %s, %s, %s)
            """, default_connections
        )
        debug("default: Subregion connections added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *TABLE* values: {e}")
