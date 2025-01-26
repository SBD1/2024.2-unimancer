# Change the name *TABLE* to the table name that you're changing!

from database import Database
from utils import debug

# Add something in the database.
def template(db: Database):
    try:
        default_values = [
            (
                "a_colum_value",
                "b_column_value",
                "c_column_value"
            )
        ]
        
        db.cur.executemany(
            """
            INSERT INTO *TABLE* (a, b, c)
            VALUES (%s, %s, %s)
            """, default_values
        )

        debug("default: *TABLE* added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *TABLE* values: {e}")