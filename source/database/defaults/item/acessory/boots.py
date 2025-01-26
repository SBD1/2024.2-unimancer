from database import Database
from utils import debug

def boots(db: Database):
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Feita de couro gasto", 2, "Botas de couro", 1, 15),
            ("Feita de couro de dragão", 4, "Botas de dragão", 2, 30),
            ("Criadas com peles encantadas de criaturas aquáticas", 5, "Botas de água", 2, 30),
            ("Forjadas com o poder das trevas", 6, "Botas do crepúsculo", 5, 50),
            ("Feitas de cristais mágicos", 6, "Botas de cristal", 4, 80),
            ("Revestidas por gelo eterno", 11, "Botas de gelo", 3, 70),
            ("Feitas de madeira viva", 3, "Botas de madeira", 2, 12),
            ("Forjadas com o poder do trovão", 15, "Botas do trovão", 3, 110),
            ("Feitas de ossos de dragão", 20, "Botas de ossos", 6, 100),
            ("Botas da Realeza, forjado para magos experientes", 23, "Botas da Realeza", 5, 120),
        ]

        
        db.cur.executemany(
            """
            CALL create_acessorio('Botas', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: botas added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *ACESSORIOS.BOOTS* values: {e}")