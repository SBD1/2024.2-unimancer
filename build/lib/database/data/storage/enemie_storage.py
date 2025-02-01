from database import Database
from utils import debug, error
from colorama import Style
import random

def enemie_storage(db: Database):

    table_name = Style.BRIGHT + "ARMAZENAMENTO INIMIGO" + Style.NORMAL

    try:
        db.cur.execute("SELECT id, vida_maxima FROM inimigo")  
        inimigos = db.cur.fetchall()

        db.cur.execute("SELECT id, tipo, nome, drop_inimigos_media FROM item")  
        itens = db.cur.fetchall()

        valores_insercao = []

        for inimigo in inimigos:
            inimigo_id, vida_maxima = inimigo

            if vida_maxima < 50:
                categoria = 1 
            elif vida_maxima < 100:
                categoria = 2 
            else:
                categoria = 3  

            for item in itens:
                item_id, tipo, nome, drop_inimigos_media = item

                if categoria == 1:
                    chance = random.randint(1, 3) 
                elif categoria == 2:
                    chance = random.randint(1, 6)  
                else:
                    chance = random.randint(1, 10) 

                if chance == 1:
                    valores_insercao.append((inimigo_id, item_id))

        db.cur.executemany(
            """
            INSERT INTO armazenamento_inimigo (inimigo_id, armazenamento_id)
            VALUES (%s, %s)
            """, valores_insercao
        )

        db.conn.commit()
        debug(f"default: {len(valores_insercao)} {table_name} updated successfully!")

        return len(valores_insercao)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")
        return 0
