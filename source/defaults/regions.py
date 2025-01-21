from database import Database
from utils import debug

# Add the regions and in the game.
def regions(db: Database):
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

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding regions and subregions: {e}")
