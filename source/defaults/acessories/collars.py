from database import Database
from utils import debug
        
# add collars in the magical fantasy game where only exists magical creatures.
def collars(db: Database):
    try:
        # [("descricao...", inimigos para matar para dropar, "nome", "peso", "preco")]
        default_values = [
            ("Colar de bronze, não é de muito valor.", 5, "Colar de bronze", 1, 10),
            ("Colar de prata, forjado para magos iniciantes", 20, "Colar de prata", 2, 14),
            ("Banhado em brasas vivas, abastece feitiços de fogo.", 15, "Colar da Combustão Arcana", 2, 50),
            ("Carrega correntes aéreas, amplificando magias de vento.", 10, "Colar da Brisa Mística", 1, 35),
            ("Feito de gelo eterno, concede resistência ao calor intenso.", 18, "Colar do Gelo Supremo", 3, 65),
            ("Pulsante com energia vital, auxilia na regeneração.", 8, "Colar do Vigor Florestal", 2, 40),
            ("Criado a partir de cristais puros, potencializa feitiços de luz.", 12, "Colar do Prisma Radiante", 5, 90),
            ("Une ecos ancestrais, conferindo proteção espiritual.", 20, "Colar do Eco Ancestral", 4, 70),
            ("Guardado por faíscas trovejantes, intensifica habilidades elétricas.", 25, "Colar do Raio Furioso", 3, 100),
            ("Tecido com sombras crepitantes, canaliza força sombria.", 18, "Colar do Eclipse Noturno", 4, 110),
            ("Imerso em magia aquática, fornece agilidade e ataques aquosos.", 14, "Colar da Maré Mística", 2, 80),
            ("Forjado em runas de sangue, sacrifica vida para poder extremo.", 30, "Colar Carmesim Profano", 6, 150),
            ("Colar de vento cortante com lâminas invisíveis", 20, "Anel de vento", 1, 65),
            ("Colar da Realeza, forjado para magos experientes", 23, "Anel da Realeza", 5, 120),
        ]
        
        db.cur.executemany(
            """
            CALL create_acessorio('Colar', %s, %s, %s, %s, %s);
            """, default_values
        )

        debug("default: *collars* added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding *ACESSORIOS.COLLARS* values: {e}")