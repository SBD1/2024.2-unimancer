from database import Database
from database.data.storage.storage import storage
from utils import debug, error
from colorama import Style

def storage(item_name: str, quantity: int, db: Database) -> int:
    try:
        db.cur.execute(
            f"""
            SELECT item.id 
            FROM item 
            INNER JOIN acessorio on acessorio.id = item.id
            WHERE nome = '{item_name}';
            """
        )
        item_id = db.cur.fetchone()

        if item_id is None:
            error(f"Item '{item_name}' não encontrado no banco de dados.")
            return None

        db.cur.execute(
            f"""
            INSERT INTO armazenamento(item_id, quantidade) 
            VALUES ({item_id[0]}, {quantity})
            RETURNING id;
            """
        )
        storage_id = db.cur.fetchone()[0]
        db.conn.commit()
        
        return storage_id
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding storage values: {e}")
        return None

def quester(quester_name: str, db: Database) -> int:
    db.cur.execute(
        f"""
        SELECT quester.id
        FROM quester
        INNER JOIN civil ON quester.id = civil.id
        WHERE civil.nome = '{quester_name}';
        """
    )
    return db.cur.fetchone()[0]

def quests(db: Database):
    
    table_name = Style.BRIGHT + "QUEST" + Style.NORMAL

    try:
        ancient_id = quester("Ancião", db)
        

        storage_id_1 = storage("Chapéu do Vento Frio", 1, db)
        storage_id_2 = storage("Manto de Neve Encantado", 2, db)

        if storage_id_1 is None or storage_id_2 is None:
            error("Failed to create storage entries, aborting quest creation.")
            return 0

        values = [
            (
                ancient_id,
                storage_id_1,
                7,
                "Peste de Ratos",
                "Elimine os ratos que estão infestando a região!",
                50,
                "Iniciante"
            ),
            (
                ancient_id,
                storage_id_2,
                25,
                "Ruínas do Abismo Aterrorizada",
                "Expulse o chefe que está aterrorizando os mercadores!",
                250,
                "Fácil"
            ),
        ]
        db.cur.executemany(
            """
            INSERT INTO quest(quester_id, armazenamento_id, sub_regiao_id, titulo, descricao, recompensa, dificuldade)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, values
        )

        db.conn.commit()
        debug(f"default: {len(values)} {table_name} added successfully!")
        
        return len(values)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating {table_name}: {e}")