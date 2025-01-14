import sys
from database import Database
from create_character import Character
from default import populate_database
import interface

init_sql = "./source/init.sql"
db = Database("localhost", "postgres", "postgres", "123456")

DEBUG = True

# Get all table names from the database.
def get_table_names() -> list:
    db.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = db.cur.fetchall()
    return [table[0] for table in tables]

# Process command line arguments.
if len(sys.argv) > 1:
   arg = sys.argv[1]
   if arg == "delete" or arg == "reset":
       db.delete_tables()
       if arg == "reset":
           db.execute_file(init_sql)
   exit(0)

print(get_table_names())

if len(get_table_names()) == 0:
   print("Nenhuma tabela encontrada. Criando banco de dados...")
   db.execute_file(init_sql)
   print("Banco de dados e tabelas criados com sucesso!")
   populate_database(db)

interface.game_loop(db.conn)