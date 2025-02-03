from database import Database
from utils import debug, error
from colorama import Style

def merchants(db: Database):
    
    table_name = Style.BRIGHT + "MERCADOR" + Style.NORMAL

    try:
        mercadores = [
            (
                "Jason",
                2,
                "Jason é um importante mercador de acessórios e itens mágicos.",
                """Bem-vindo, aventureiro! O que você deseja comprar?
Tenho uma variedade de itens mágicos e acessórios de qualidade!"""
            ),
            (
                "Nico",
                18,
                "Nico é um antigo vendedor de poções",
                """Olá, aventureiro! O que você deseja comprar?
Tenho uma variedade de poções para suas necessidades!"""
            ),
            (
                "Luna",
                32,
                "Luna é uma mercadora de itens mágicos",
                """Olá, aventureiro! Vejo que conseguiu chegar até aqui.
Mundo perigoso, não é mesmo? Mas não se preocupe, tenho os itens mágicos perfeitos para você!"""
            )
        ]
        
        db.cur.executemany(
            """
            SELECT criar_mercador(%s, %s::INT, %s, %s)
            """, mercadores
        )

        db.conn.commit()
        debug(f"default: {len(mercadores)} {table_name} added successfully!")
        
        return len(mercadores)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")