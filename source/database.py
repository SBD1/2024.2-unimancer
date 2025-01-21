from utils import debug
import psycopg2

class Database:
    
    def __init__(self, host, db, user, password):
        
        self.conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=password
        )
        
        if not self.conn.status:
            debug("Database: Connection failed with server.")
            exit(1)

        self.cur = self.conn.cursor()
        
        self.types = (
            "tipo_inventario",
            "tipo_elemento",
            "tipo_dificuldade",
            "tipo_item",
            "tipo_feitico",
            "tipo_npc",
            "tipo_civil",
            "tipo_direcao",
            "tipo_situacao",
            "tipo_acessorio"
        )
        
        self.tables = (
            "tipo_item",
            "tipo_npc",
            "item",
            "armazenamento",
            "regiao",
            "sub_regiao",
            "sub_regiao_conexao",
            "sub_regiao_item_conexao",
            "personagem",
            "inventario",
            "npc",
            "quester",
            "quest",
            "quest_instancia",
            "item_instancia",
            "mercador",
            "armazenamento_mercador",
            "transacao",
            "civil",
            "mochila",
            "feitico",
            "grimorio",
            "feitico_dano",
            "feitico_dano_area",
            "feitico_cura",
            "feitico_escrito",
            "feitico_aprendido",
            "feitico_inimigo",
            "feitico_requerimento",
            "pergaminho",
            "efeito",
            "regiao_efeito",
            "acessorio",
            "acessorio_efeito",
            "pocao",
            "pocao_efeito",
            "inimigo",
            "armazenamento_inimigo",
            "inimigo_instancia",
            "combate"
        )
        
    def delete_type(self, type_name: str) -> None:
        self.cur.execute(f"DROP TYPE IF EXISTS {type_name} CASCADE")
        
    def delete_table(self, table_name: str) -> None:
        self.cur.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")

    # For debugging purposes, force delete every single table of the database and it's dependencies.
    # So that we can create the default lines of the database again.
    def delete_tables(self) -> None:
        try:
            for table in self.tables:
                self.delete_table(table)
            for type in self.types:
                self.delete_type(type)

            

            self.conn.commit()

        except Exception as e:
            debug(f"Database: Error deleting tables: {e}")

        debug("Database: Deleted all tables.")

    # Execute a SQL file in the database.
    def execute_file(self, path: str) -> None:
        debug("Database: Reading file...")
        with open(path, "r") as file:
            sql = file.read()
            self.cur.execute(sql)
            self.conn.commit()
        debug("Database: File commited successfully.")
