from database import Database
from utils import debug

# Add hats in the magical fantasy game where only exists magical creatures.
def hats(db: Database):
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Envolto em símbolos arcanos, revela segredos a mentes curiosas.", 5, "Chapéu de Bruxo", 10, 100),
            ("Uma presença sussurrante acompanha seu dono, trazendo incertezas.", 15, "Chapéu amaldioçado", 1, 150),
            ("Sombras vivas pairam ao redor, nutrindo feitiços destrutivos.", 10, "Chapéu do Feiticeiro das Sombras", 5, 180),
            ("Forjado no sopro de um dragão, exala poder ancestral.", 20, "Chapéu do Dragão Ancião", 8, 250),
            ("Sussurros gélidos moldam sua forma, despertando inquietação sutil.", 12, "Chapéu do Vento Frio", 4, 120),
            ("Cerimônias sombrias consagram este item, nutrindo energias nefastas.", 25, "Chapéu do Necromante Oculto", 7, 300),
            ("Brilha com fervor etéreo, repelindo ameaças e purificando a escuridão.", 5, "Chapéu da Luz Purificadora", 3, 150),
            ("Cada centelha emana adrenalina, incendiando o campo de batalha.", 18, "Chapéu do Pirotécnico Selvagem", 6, 210),
            ("Troveja energias dançantes, agitando corações imprudentes.", 15, "Chapéu da Tempestade Elétrica", 4, 190),
            ("Um encanto dourado envolve o usuário, inspirando coragem inabalável.", 22, "Chapéu do Guardião Dourado", 6, 260),
            ("Sutileza ilusionista tece ilusões traiçoeiras aos olhos alheios.", 9, "Chapéu do Ilusionista Arcano", 3, 140),
            ("Guardado por espíritos milenares, desperta ecos de eras passadas.", 17, "Chapéu do Espírito Ancestral", 5, 220),
        ]

        
        db.cur.executemany(
            """
            CALL create_acessorio('Chapéu', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: *hats* added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *ACESSORIOS.HATS* values: {e}")