from database.Database import Database
from default import populate_database
import sys
import logic
import utils

def main():

    sqls = {
        "./source/database/ddl/types.sql",
        "./source/database/ddl/tables.sql",
        "./source/database/dml/procedures.sql",
        "./source/database/dml/triggers.sql"
    }
    
    db = Database("localhost", "postgres", "postgres", "123456")
    
    def table_length() -> list:
        db.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        tables = db.cur.fetchall()
        return len(tables)
    
    def init_database():
        for sql in sqls:
            db.execute_file(sql)
        utils.debug("")
        populate_database(db)
    
    # Process command line arguments.
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "delete" or arg == "reset":
            db.delete_tables()
            if arg == "reset":
                init_database()
        exit(0)
    
    if table_length() == 0:
        utils.debug("Nenhuma tabela encontrada. Criando banco de dados...")
        utils.debug("Banco de dados e tabelas criados com sucesso!")
        init_database()
    
    while True:
        character = logic.main_menu(db.conn)
        if not character:
            utils.debug("Nenhum personagem retornado, saindo.")
            exit(0)
        
        while logic.game(db.conn, character):
            pass