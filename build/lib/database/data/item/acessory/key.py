from database import Database
from utils import debug, error
from colorama import Style

# Add hats in the magical fantasy game where only exists magical creatures.
def keys(db: Database):
    
    table_name = Style.BRIGHT + "ACESSORIO (Chave)" + Style.NORMAL
    
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            # Abre a "Catedral Queimada".
            (
                "Cruz Papal",
                9999999,
                "Antiga cruz deixada por um portão da igreja.",
                1,
                100
            ),
            # Abre a "Fenda do Abismo"
            (
                "Chave de Bronze",
                9999999,
                "Uma chave de bronze que abre a porta para o Abismo.",
                2,
                78
            ),
            # Abre o "Monte Caído".
            (
                "Torcha do Escuro Montante",
                9999999,
                "Uma tocha que brilha no escuro especificamente no Monte Caído.",
                5,
                128
            )
        ]
        
        db.cur.executemany(
            """
            SELECT criar_acessorio('Chave', %s, %s, %s, %s, %s);
            """, default_values
        )

        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")