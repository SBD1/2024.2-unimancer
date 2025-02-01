from database import Database
from utils import debug, error
from colorama import Style

def questers(db: Database):
    
    table_name = Style.BRIGHT + "QUESTER" + Style.NORMAL

    try:
        questers = [
            (
                "Ancião",
                3,
                "Velho homem aborrecido com a vida.",
                """Tsk! Malditas pragas... esses ratos estão por toda parte!
                Entram nos celeiros, roem nossos suprimentos e nem os templos escaparam deles!
                Se ninguém fizer nada, logo estaremos dividindo nossas camas com essa praga!
                Se você puder nos ajudar a exterminá-los, seremos imensamente gratos. Mate-os e lhe darei uma recompensa justa!
                """
            ),
        ]
        
        db.cur.executemany(
            """
            SELECT criar_quester(%s, %s::INT, %s, %s)
            """, questers
        )

        db.conn.commit()
        debug(f"default: {len(questers)} {table_name} added successfully!")
        
        return len(questers)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")