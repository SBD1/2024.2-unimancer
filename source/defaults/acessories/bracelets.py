from database import Database
from utils import debug

# add bracelets in the magical fantasy game where only exists magical creatures.
def bracelets(db: Database):
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Bracelete de bronze, não é de muito valor.", 6, "Bracelete de bronze", 1, 10),
            ("Bracelete de ossos forjado em matéria negra", 16, "Bracelete de ossos", 3, 25),
            ("Bracelete herbáceo entrançado com grama mística", 7, "Bracelete de grama", 1, 18),
            ("Bracelete envolto em plasma mágico, intensifica feitiços destrutivos", 20, "Bracelete de Plasma Arcano", 4, 80),
            ("Bracelete de vidro etéreo, refletindo energias arcanas", 12, "Bracelete de Cristal Etéreo", 2, 50),
            ("Bracelete entalhado em rocha ancestral, trazendo firmeza inabalável", 25, "Bracelete da Rocha Primeva", 5, 100),
        ]
    
        
        db.cur.executemany(
            """
            CALL create_acessorio('Bracelete', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: *bracelets* added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *ACESSORIOS.BRACELETS* values: {e}")
        