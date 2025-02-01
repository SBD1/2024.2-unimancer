from database import Database
from utils import debug, error
from colorama import Style

def citizens(db: Database):
    
    table_name = Style.BRIGHT + "CIVIL" + Style.NORMAL

    try:
        civis = [
            ("Paulo", 4, "Um homem que passa o tempo observando os magos."),
            ("Natan", 2, "Um indivíduo que frequentemente passa pela cidade, sem muito a dizer."),
            ("João", 2, "Um indivíduo que parece estar sempre ocupado com suas próprias tarefas."),
            ("Renan", 4, "Visto frequentemente perto do rio, pescando ou relaxando."),
            ("Millena", 5, "Uma pessoa tranquila que observa o movimento da cidade sem se envolver."),
        ]
        db.cur.executemany(
            """
            SELECT criar_civil(%s, %s::INT, %s, 'Civil')
            """, civis
        )

        db.conn.commit()
        debug(f"default: {len(civis)} {table_name} added successfully!")
        
        return len(civis)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")