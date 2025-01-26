from database import Database
from utils import debug, error

def merchants(db: Database):

    try:
        mercadores = [
            (
                "Jason",
                12,
                "Jason é um importante mercador de acessórios e itens mágicos.",
                None,
                """Bem-vindo, aventureiro! O que você deseja comprar?
Tenho uma variedade de itens mágicos e acessórios de qualidade!"""
            ),
            (
                "Nico",
                18,
                "Nico é um antigo vendedor de poções",
                None,
                """Olá, aventureiro! O que você deseja comprar?
Tenho uma variedade de poções para suas necessidades!"""
            ),
            (
                "Luna",
                32,
                "Luna é uma mercadora de itens mágicos",
                None,
                """Olá, aventureiro! Vejo que conseguiu chegar até aqui.
Mundo perigoso, não é mesmo? Mas não se preocupe, tenho os itens mágicos perfeitos para você!"""
            )
        ]
        
        db.cur.executemany(
            """
            SELECT criar_mercador(%s, %s::INT, %s, %s::INT, %s)
            """, mercadores
        )

        debug("default: mercador added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        error(f"default: Error occurred while adding mercador: {e}")