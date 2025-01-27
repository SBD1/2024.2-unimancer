from database import Database
from utils import debug, error
from colorama import Style

# add buckles in the magical fantasy game where only exists magical creatures.
def buckle(db: Database):
    
    table_name = Style.BRIGHT + "ACESSORIO (Fivela)" + Style.NORMAL
    
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Fivela de bronze, não é de muito valor.", 6, "Fivela de bronze", 1, 10),
            ("Forjada em runas antigas, fortalece magias destrutivas.", 12, "Fivela Rúnica", 2, 45),
            ("Tingida com aura sombria, canaliza energias malditas.", 18, "Fivela Obscura", 3, 75),
            ("Resplandecente com luz astral, aprimora habilidades de cura.", 10, "Fivela Celestial", 2, 60),
            ("Envolta em correntes de ar, concede agilidade incomum.", 14, "Fivela da Ventania", 1, 40),
            ("Revestida em gelo perpétuo, protege contra temperaturas extremas.", 20, "Fivela do Gelo Inquebrável", 4, 90)
        ]
        
        db.cur.executemany(
            """
            SELECT criar_acessorio('Fivela', %s, %s, %s, %s, %s)
            """, default_values
        )

        db.conn.commit()
        debug(f"default: {table_name} added successfully!")

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")