from database import Database
from utils import debug, error
from colorama import Style

# add gloves in the magical fantasy game where only exists magical creatures.
def gloves(db: Database):
    
    table_name = Style.BRIGHT + "ACESSORIO (Luva)" + Style.NORMAL
    
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Protege as mãos de qualquer magia .", 1, "Luva d'água", 1, 2014),
            ("Concentra chamas internas, ideal para confrontos com salamandras do vulcão.", 8, "Luvas Ígneas", 2, 320),
            ("Transfere força aérea para golpes sutis, caçadas a harpias ficam fáceis.", 10, "Luvas do Vento Cortante", 1, 280),
            ("Proporciona resistência à escuridão, eficiente contra magos sombrios.", 12, "Luvas das Sombras Profundas", 3, 400),
            ("Canaliza luz radiante, purificando venenos de slimes venenosos.", 9, "Luvas da Aurora Purificadora", 2, 350),
            ("Cria um vínculo aquático, auxiliando na absorção de magias de água.", 6, "Luvas da Maré Serena", 2, 290),
            ("Impõe terror contra inimigos fracos, inspirada em runas de necromancia.", 14, "Luvas do Terror Profano", 4, 450),
            ("Concede agilidade e precisão, ideal para caçadas a feras rápidas.", 7, "Luvas do Predador Ágil", 1, 310),
            ("Forjadas em gelo eterno, protegem contra gélidas criaturas do norte.", 11, "Luvas do Gelo Eterno", 3, 380),
            ("Concede resistência elétrica, eficaz contra magos elétricos.", 13, "Luvas da Tempestade Elétrica", 2, 420)
        ]
        
        db.cur.executemany(
            """
            SELECT criar_acessorio('Luvas', %s, %s, %s, %s, %s);
            """, default_values
        )

        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")