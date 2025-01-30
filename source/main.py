import sys
from database.Database import Database
from default import populate_database
import logic
from utils import debug

sqls = {
    "./source/database/ddl/types.sql",
    "./source/database/ddl/tables.sql",
    "./source/database/ddl/procedures.sql",
    "./source/database/ddl/triggers.sql"
}

db = Database("localhost", "postgres", "postgres", "123456")

def table_length() -> list:
    db.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = db.cur.fetchall()
    return len(tables)

def init_database():
    for sql in sqls:
        db.execute_file(sql)
    debug("")
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
    debug("Nenhuma tabela encontrada. Criando banco de dados...")
    debug("Banco de dados e tabelas criados com sucesso!")
    init_database()

while True:
    character = logic.main_menu(db.conn)
    if not character:
        debug("Nenhum personagem retornado, saindo.")
        exit(0)
    
    while logic.game(db.conn, character):
        pass