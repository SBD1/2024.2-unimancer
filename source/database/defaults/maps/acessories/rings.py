from database import Database
from utils import debug

# Add rings in the database.
def rings(db: Database):
    try:
        # [("descricao...", "inimigos para matar para dropar", "nome", "peso", "preco")]
        default_values = [
            ("Anel de bronze, não é de muito valor.", 5, "Anel de bronze", 1, 10),
            ("Anel de prata, forjado para magos iniciantes", 20, "Anel de prata", 2, 14),
            ("Anel de ouro, forjado para magos experientes", 23, "Anel de ouro", 5, 120),
            ("Anel encantado, forjado para magos experientes", 37, "Anel encantado", 1, 230),
            ("Anel amaldiçoado, forjado para magos experientes", 37, "Anel amaldiçoado", 15, 210),
            ("Anel de diamante, forjado para magos experientes", 51, "Anel de diamante", 10, 500),
            ("Anel de ossos forjado em matéria negra", 16, "Anel de ossos", 3, 25),
            ("Anel herbáceo entrançado com grama mística", 7, "Anel de grama", 1, 18),
            ("Anel de gelo inquebrável que congela o ambiente", 40, "Anel de gelo inquebrável", 4, 110),
            ("Anel fulgor mágico que emana energia arcana", 28, "Anel fulgor mágico", 2, 80),
            ("Anel espectral que atrai espíritos perdidos", 33, "Anel espectral", 6, 150),
            ("Anel de vento cortante com lâminas invisíveis", 20, "Anel de vento", 1, 65),
        ]
        
        db.cur.executemany(
            """
            CALL create_acessorio('Anel', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: aneis added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding ACESSORIOS.ANEIS values: {e}")