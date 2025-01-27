from database import Database
from utils import debug, error
from colorama import Style

def citizens(db: Database):
    
    table_name = Style.BRIGHT + "TABLE_NAME" + Style.NORMAL

    try:
        values = [
            ("a_colum_value", "b_column_value", "c_column_value", "d_column_value"),
        ]
        db.cur.executemany(
            """
            INSER INTO table_name (a_column, b_column, c_column, d_column)
            """, values
        )

        db.conn.commit()
        debug(f"default: {table_name}s added successfully!")
        

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")