from database import Database
from utils import debug, error
from colorama import Style

def socks(db: Database):
    
    table_name = Style.BRIGHT + "ACESSORIO (Meias)" + Style.NORMAL
    
    try:

        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Feitas de pano comum", 2, "Meia de algodão rústico", 1, 5),
            ("Feitas de lã de ovelha", 4, "Meia de lã", 1, 10),
            ("Feitas de seda mágica", 10, "Meia da brisa celestial", 2, 45),
            ("Feitas de algodão encantado", 11, "Meia de algodão encantado", 2, 45),
            ("Com fios de ouro", 12, "Meia de ouro", 2, 47),
            ("Fabricada com raízes de árvores mágicas", 13, "Meia de raízes", 2, 50),
            ("Imbuídas com magia sombria", 15, "Meias do Vórtice Sombrio", 3, 50),
        ]
        
        db.cur.executemany(
            """
            SELECT criar_acessorio('Meias', %s, %s, %s, %s, %s);
            """, default_values
        )

        db.conn.commit()
        debug(f"default: {table_name} added successfully!")

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")