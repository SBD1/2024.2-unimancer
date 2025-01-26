from database import Database
from utils import debug

def socks(db: Database):
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
            CALL create_acessorio('Meias', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: meias added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *ACESSORIOS.SOCKS* values: {e}")