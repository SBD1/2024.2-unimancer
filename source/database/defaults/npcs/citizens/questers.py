from database import Database
from utils import debug

def questers(db: Database):

    try:
        questers = [
            (
                "Ancião",
                3,
                "Velho homem aborrecido com a vida.",
                """Bem-vindo, jovem. Você deseja embarcar em uma jornada?
Os ratos selavagens desta área se tornaram uma praga para nosso povo!
Destroem nossas plantações e assustam nossas crianças, por favor dê um jeito neles!"""
            ),
            (
                "Elysia",
                2,
                "descr",
                """Eu vi algo estranho nas montanhas...

Está preparado?"""
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

        debug("default: Questers added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding Questers: {e}")