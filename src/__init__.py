import os

# To work on windows
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from database.Database import Database
from default import populate_database
import sys
import logic.main as logic
import utils

def main():
    sqls = [    
        "./database/ddl/types.sql",
        "./database/ddl/tables.sql",
        "./database/dml/procedures.sql",
        "./database/dml/triggers.sql"
    ]
    
    # Create users of the database.
    db_root = Database("localhost", "postgres", "postgres", "123456")
    
    def table_length(db) -> list:
        db.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        tables = db.cur.fetchall()
        return len(tables)
    
    def init_database(db_root):
        db_root.execute_file("./database/users.sql")
        db_dba = Database("localhost", "postgres", "dba", "dba123")
        db_dba.cur.execute("SET search_path TO public")  
        for sql in sqls:
            db_dba.execute_file(sql)
        db_root.execute_file("./database/user_game.sql")
        populate_database(db_dba)
    
    # Process command line arguments.
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "delete" or arg == "reset":
            db_root.delete_tables()
            if arg == "reset":
                init_database(db_root)
        return 0
    
    # Interface of the gamer, user with less privileges.
    db_game = Database("localhost", "postgres", "game", "game123")
    
    if table_length(db_game) == 0:
        utils.debug("Nenhuma tabela encontrada. Criando banco de dados...")
        utils.debug("Banco de dados e tabelas criados com sucesso!")
        init_database()
    
    while True:
        
        character = logic.main_menu(db_game.conn)
        if not character:
            utils.debug("Nenhum personagem retornado, saindo.")
            continue
        
        elif character == -1:
            utils.debug("Saindo do jogo")
            return 0
        
        
        while logic.game(db_game.conn, character):
            pass
        
main()