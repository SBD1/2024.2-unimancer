from database import Database
from utils import debug

# Add something in the database.
def template(db: Database):
    try:
        default_values = [
            ("A", "B", "C")
        ]
        
        db.cur.executemany(
            """
            INSERT INTO *TABLE* (a, b, c)
            VALUES (%s, %s, %s)
            """, default_values
        )

        debug("default: *hats* added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *ACESSORIOS.HATS* values: {e}")