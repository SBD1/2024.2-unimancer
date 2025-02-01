from database import Database
from utils import debug, error
from colorama import Style

def cloack(db: Database):
    
    table_name = Style.BRIGHT + "ACESSORIO (Manto)" + Style.NORMAL
    
    try:
        # [("descricao...", "inimigos para matar para dropar", "nome", "peso", "preco")]
        default_values = [
            ("Um manto simples de tecido grosso", 5, "Manto de Lona Simples", 2, 30),
            ("Feito de algodão comum, esse manto é leve e confortável", 8, "Manto de Algodão Básico", 2, 25),
            ("Este manto de lã não é muito resistente", 9, "Manto de Lã Rústica", 3, 35),
            ("Manto de tecido encantado que protege contra a neve.", 11, "Manto de Neve Encantado", 4, 60),
            ("Feito com peles de animais selvagens", 14, "Manto de Pele de Urso", 5, 70),
            ("Manto de seda refinada", 15, "Manto de Seda Flamejante", 6, 85),
            ("Manto forjado a partir de tecido celestial", 17, "Manto Celestial das Sombras", 6, 100),
            ("Feito com penas de fênix", 20, "Manto da Fênix Ardente", 6, 120),
            ("Este manto é imbuído com magia de tempestade", 22, "Manto do Vórtice Tempestuoso", 7, 140)
        ]
        
        db.cur.executemany(
            """
            SELECT criar_acessorio('Manto', %s, %s, %s, %s, %s);
            """, default_values
        )

        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")