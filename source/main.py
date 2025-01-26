import sys
from database.Database import Database
from create_character import Character
from default import populate_database
from interface import game_loop
from utils import debug

types_sql = "./source/database/ddl/types.sql"
init_sql = "./source/database/ddl/init.sql"
procedures_sql = "./source/database/ddl/procedure.sql"
triggers_sql = "./source/database/ddl/triggers.sql"
db = Database("localhost", "postgres", "postgres", "123456")

# Get all table names from the database.
def get_table_names() -> list:
    db.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = db.cur.fetchall()
    return [table[0] for table in tables]

def init_database():
    db.execute_file(types_sql)
    db.execute_file(init_sql)
    db.execute_file(procedures_sql)
    db.execute_file(triggers_sql)
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

if len(get_table_names()) == 0:
    debug("Nenhuma tabela encontrada. Criando banco de dados...")
    debug("Banco de dados e tabelas criados com sucesso!")
    init_database()

game_loop(db.conn)