from database import Database
from utils import debug, error
from colorama import Style

def pants(db: Database):
    
    table_name = Style.BRIGHT + "ACESSORIO (Calça)" + Style.NORMAL
    
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Feita de couro gasto", 2, "Calças de couro", 1, 40),
            ("Feita de couro de dragão", 4, "Calças de dragão", 2, 50),
            ("Forjadas com o poder das trevas", 6, "Calças do crepúsculo", 3, 55),
            ("Feitas de cristais mágicos", 6, "Calças de cristal", 4, 80),
            ("Feitas de madeira viva", 3, "Calças de madeira", 2, 12),
            ("Forjadas com o poder do trovão", 15, "Calças do trovão", 3, 110),
            ("Feitas de ossos de dragão", 20, "Calças de ossos", 6, 100),
            ("Calças da Realeza, forjado para magos experientes", 23, "Calças da Realeza", 5, 120),
            ("Estas calças carregam a energia das tempestades", 25, "Calças do Ciclone", 4, 130),
            ("Calças feitas de peles de animais mágicos", 30, "Calças de Fera", 5, 140),
            ("Calças feitas de tecido encantado", 32, "Calças de Tecido", 3, 150),
            ("Calças feitas de seda mágica", 33, "Calças de Seda", 3, 200),
            ("Calças feitas de ossos de gigante", 34, "Calças de Gigante", 6, 210),
            ("Calças feitas de algodão encantado", 36, "Calças de Algodão", 4, 220),
            ("Calças feitas de escamas de serpente", 35, "Calças de Serpente", 5, 230)
        ]

        
        db.cur.executemany(
            """
            SELECT criar_acessorio('Calça', %s, %s, %s, %s, %s);
            """, default_values
        )

        db.conn.commit()
        debug(f"default: {table_name} added successfully!")

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")