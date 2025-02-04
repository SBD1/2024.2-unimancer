from database import Database
from utils import error, debug
from colorama import Style

def storage(item_name: str, quantity: int, db: Database) -> int:
    try:
        db.cur.execute(
            "SELECT id FROM item WHERE nome = %s;", (item_name,)
        )
        item_id = db.cur.fetchone()

        if item_id is None:
            error(f"Item '{item_name}' não encontrado no banco de dados.")
            return None

        db.cur.execute(
            """
            INSERT INTO armazenamento(item_id, quantidade) 
            VALUES (%s, %s)
            RETURNING id;
            """, (item_id[0], quantity)
        )
        storage_id = db.cur.fetchone()[0]
        db.conn.commit()
        
        return storage_id
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding storage values: {e}")

def populate_storage(db: Database):
    
    default_quantity = 1
    
    table_name = Style.BRIGHT + "ARMAZENAMENTO" + Style.NORMAL
   
    try:
        db.cur.execute(f"""
            SELECT id FROM item
        """)
        items = db.cur.fetchall()  

        if not items:
            debug("Nenhum item encontrado no banco de dados.")
            return

        for (id,) in items:
            db.cur.execute(f"""
                INSERT INTO armazenamento(item_id, quantidade)
                VALUES ({id}, {default_quantity});
            """)

        db.conn.commit()
        debug(f"default: {len(table_name)} {table_name} added successfully!")
        
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")