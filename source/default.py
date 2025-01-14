from database import Database
from utils import debug

def populate_database(db: Database):
    try:
        # Adding regions
        default_regions = [
            ("Vilarejo do Amanhecer", "Região inicial do jogar, um vilarejo tranquilo, esbelto...", "Água")
        ]
        db.cur.executemany(
            """
            INSERT INTO regiao (nome, descricao, elemento)
            VALUES (%s, %s, %s)
            """, default_regions
        )

        debug("default: Regions added successfully!")

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
        debug(f"default: Error occurred while adding regions and subregions: {e}")
