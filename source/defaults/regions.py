from database import Database
from utils import debug

# Add the regions and in the game.
def regions(db: Database):
    try:
        # Adding regions
        regions = [
        ("Vilarejo do Amanhecer", "Uma vila tranquila, onde os primeiros raios de sol tocam a terra.", "Água"),
        ("Floresta Eterna", "Uma floresta densa e mística, habitada por espíritos antigos.", "Terra"),
        ("Ruínas do Abismo", "Ruínas ancestrais com segredos esquecidos.", "Trevas"),
        ("Deserto de Areias Infinitas", "Um deserto vasto e sem fim, onde segredos estão enterrados sob a areia.", "Fogo"),
        ("Montanha do Crepúsculo", "Uma montanha alta e gélida, coberta de mistérios e perigos.", "Ar"),
        ("Terras Devastadas", "Um lugar sombrio e inóspito, marcado pela destruição e caos.", "Trevas"),
        ("Caverna Cristalizada", "Uma caverna mágica repleta de cristais brilhantes e perigos ocultos.", "Luz"),
        ("Caverna Soterrada", "Uma caverna misteriosa enterrada sob as montanhas, cheia de segredos antigos.", "Terra")
        ]
        db.cur.executemany(
            """
            INSERT INTO regiao (nome, descricao, elemento)
            VALUES (%s, %s, %s)
            """, regions
        )

        debug("default: Regions added successfully!")

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding regions and subregions: {e}")
