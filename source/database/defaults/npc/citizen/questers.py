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
                "Bem-vindo, jovem. Você deseja embarcar em uma jornada?"
            ),
            (
                "Elysia",
                2,
                "descr",
                "Eu vi algo estranho nas montanhas... Está disposto a investigar?"
            ),
            (
                "Isolde",
                1,
                "Você está pronto para enfrentar o que há de mais perigoso neste mundo?",
                "...Dialogo..."
            ),
            (
                "Kael",
                4,
                "Tenho algumas pistas para você, mas isso vai exigir coragem.",
                "...Dialogo..."
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