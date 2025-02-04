import random
from database import Database
from utils import debug, error
from colorama import Style

# 132 itens
# 32 subregioes

def default_subregion_itens(db: Database):
    table_name = Style.BRIGHT + "ITENS SUBREGIAO" + Style.NORMAL
    
    sub_regions_quantity = 33
    quantity = sub_regions_quantity // 3
    
    try:
        for i in range(1, quantity):
            random_item = random.randint(1,132)
            db.cur.execute(
                f"""
                UPDATE sub_regiao
                SET armazenamento_id = {random_item}
                WHERE id = {i}
                """, 
            )

            db.conn.commit()
            debug(f"default: {quantity} {table_name} added successfully!")

    # Olá
    # Cade vc em tema ein ein
    

    # eu fui dormir às 10:30
    # justo
    # eu n sei pq inventei de dormir às 4h45, sendo que eu tinha que acordar às 5h30
    # ai nem acordei
    
    # pq diabos tu foi dormir esse horario
    # tu nn tinha terminado antes no discord
    # eu tinha outra parada com o deadline pra ontem, aquele curso de embarcados
    
    # kkkk, foda
    # tem atividade de redes?
    # nao, professor tava aprendendo com a gente hj
    
    # tendi
    # gostou da interface com emojis/
    # nao, prefiro cru
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")
