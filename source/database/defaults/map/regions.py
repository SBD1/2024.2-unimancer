from database import Database
from utils import debug, error
from colorama import Style

# Add the regions and in the game.
def regions(db: Database):
    
    table_name = Style.BRIGHT + "REGIAO" + Style.NORMAL
    
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

        db.conn.commit()
        debug(f"default: {table_name}s added Successfully!")

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")
