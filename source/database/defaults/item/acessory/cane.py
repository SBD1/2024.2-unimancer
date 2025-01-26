from database import Database
from utils import debug

def cane(db: Database):
    try:
        # [("descricao...", "inimigos para matar para dropar", "nome", "peso", "preco")]
        default_values = [
        ("Uma bengala simples feita de madeira bruta.", 2, "Bengala de Madeira Rústica", 2, 15),
        ("Feita de galhos secos e reforçada com cordas", 3, "Bengala de Galho Seco", 1.5, 10),
        ("Uma bengala de bambu leve", 4, "Bengala de Bambu", 1, 20), 
        ("Uma bengala de madeira polida", 5, "Bengala de Carvalho Encantado", 3, 40),
        ("Feita de madeira petrificada", 5, "Bengala de Madeira Petrificada", 4, 60),
        ("Feita de prata pura", 8, "Bengala de Prata Mística", 3, 90),
        ("Esculpida em cristal mágico", 10, "Bengala de Cristal Arcano", 2, 95),
        ("Composta por ossos de dragão", 12, "Bengala de Ossos Dracônicos", 5, 100)
        ]
        
        db.cur.executemany(
            """
            CALL create_acessorio('Bengala', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: bengalas added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding ACESSORIOS.CANE values: {e}")