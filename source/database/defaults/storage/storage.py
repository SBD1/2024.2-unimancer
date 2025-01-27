from database import Database
from utils import error

def storage(item_name: str, quantity: int, db: Database) -> int:
    try:
        db.cur.execute(
            f"""
            SELECT id FROM item WHERE nome = '{item_name}';
            """
        )
        item_id = db.cur.fetchone()[0]

        db.cur.execute(
            """
            INSERT INTO armazenamento(item_id, quantidade) VALUES (%s, %s)
            RETURNING id;
            """, (item_id, quantity)
        )
        storage_id = db.cur.fetchone()[0]
        db.conn.commit()
        
        return storage_id
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding storage values: {e}")