import random
from database import Database
from utils import debug, error
from colorama import Style

# 132 itens
# 32 subregioes

def default_subregion_itens(db: Database):
    table_name = Style.BRIGHT + "ITENS SUBREGIAO" + Style.NORMAL
    
    try:
        for i in range(1,33):
            random_item = random.randint(1,132)
            db.cur.execute(
                f"""
                UPDATE sub_regiao
                SET armazenamento_id = {random_item}
                WHERE id = {i}
                """, 
            )

            db.conn.commit()
            debug(f"default: {table_name} added successfully!")

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")
