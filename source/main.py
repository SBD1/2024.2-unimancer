# Connect to PostgreSQL database in Docker container.
# Use psycopg2 library to connect to PostgreSQL database.

import psycopg2
import sys

# For debugging purposes, force delete every single table of the database and it's dependencies.
# So that we can create the default lines of the database again.
def delete_tables(cur) -> None:
    try:
        # Drop types.
        cur.execute("DROP TYPE IF EXISTS tipo_inventario CASCADE")
        cur.execute("DROP TYPE IF EXISTS tipo_elemento CASCADE")
        cur.execute("DROP TYPE IF EXISTS tipo_dificuldade CASCADE")
        cur.execute("DROP TYPE IF EXISTS tipo_item CASCADE")
        cur.execute("DROP TYPE IF EXISTS tipo_feitico CASCADE")
        cur.execute("DROP TYPE IF EXISTS tipo_npc CASCADE")
        cur.execute("DROP TYPE IF EXISTS tipo_civil CASCADE")

        # Drop tables.
        cur.execute("DROP TABLE IF EXISTS item CASCADE")
        cur.execute("DROP TABLE IF EXISTS armazenamento CASCADE")
        cur.execute("DROP TABLE IF EXISTS regiao CASCADE")
        cur.execute("DROP TABLE IF EXISTS sub_regiao CASCADE")
        cur.execute("DROP TABLE IF EXISTS personagem CASCADE")
        cur.execute("DROP TABLE IF EXISTS inventario CASCADE")
        cur.execute("DROP TABLE IF EXISTS npc CASCADE")
        cur.execute("DROP TABLE IF EXISTS quester CASCADE")
        cur.execute("DROP TABLE IF EXISTS quest CASCADE")
        cur.execute("DROP TABLE IF EXISTS quest_instancia CASCADE")
        cur.execute("DROP TABLE IF EXISTS item_instancia CASCADE")
        cur.execute("DROP TABLE IF EXISTS mercador CASCADE")
        cur.execute("DROP TABLE IF EXISTS transacao CASCADE")
        cur.execute("DROP TABLE IF EXISTS civil CASCADE")
        cur.execute("DROP TABLE IF EXISTS mochila CASCADE")
        cur.execute("DROP TABLE IF EXISTS feitico CASCADE")
        cur.execute("DROP TABLE IF EXISTS grimorio CASCADE")
        cur.execute("DROP TABLE IF EXISTS feitico_dano CASCADE")
        cur.execute("DROP TABLE IF EXISTS feitico_dano_area CASCADE")
        cur.execute("DROP TABLE IF EXISTS feitico_cura CASCADE")
        cur.execute("DROP TABLE IF EXISTS pergaminho CASCADE")
        cur.execute("DROP TABLE IF EXISTS acessorio CASCADE")
        cur.execute("DROP TABLE IF EXISTS pocao CASCADE")
        cur.execute("DROP TABLE IF EXISTS inimigo CASCADE")
        cur.execute("DROP TABLE IF EXISTS inimigo_instancia CASCADE")
        cur.execute("DROP TABLE IF EXISTS combate CASCADE")
        cur.execute("DROP TABLE IF EXISTS feitico_escrito CASCADE")
        cur.execute("DROP TABLE IF EXISTS feitico_aprendido CASCADE")
        conn.commit()
    
    except Exception as e:
        print(f"delete_tables: Error deleting tables: {e}")

    print("delete_tables: Deleted all tables.")

# Execute a SQL file in the database.
def execute_file(name: str, conn, cur) -> None:
    print("execute_file: Reading file...")
    with open("./source/init.sql", "r") as file:
        sql = file.read()
        cur.execute(sql)
        conn.commit()
    print("execute_file: File commited successfully.")

# Add defaults in the database.
def add_defaults(conn, cur) -> None:

    # Insert default regions.
    default_regions = [
        # Fogo
        ('Bosques dos Serafins', 'Bosque com o alto índice de serafins.', 'Fogo'),
        ('Deserto de Obsidiana', 'Deserto com areias negras e calor extremo.', 'Fogo'),
        
        # Terra
        ('Planalto dos Gigantes', 'Planalto com montanhas e vales.', 'Terra'),
        
        # Água
        ('Lago dos Espelhos', 'Lago tranquilo com águas cristalinas.', 'Água'),
        
        # Ar
        ('Planície dos Ventos', 'Vasta planície com ventos constantes.', 'Ar'),
        
        # Trevas
        ('Caverna dos Espíritos', 'Caverna escura e assombrada.', 'Trevas'),
        
        # Luz
        ('Montanha dos Anjos', 'Montanha com picos nevados.', 'Luz'), 
    ]

    cur.executemany("""
        INSERT INTO regiao (nome, descricao, elemento)
        VALUES (%s, %s, %s)
    """, default_regions)
    conn.commit()

    print("add_defaults: Default regions inserted successfully!")

    # Insert default subregions.
    # (regiao_id, armazenamento_id, norte_id, leste_id, oeste_id, sul_id, nome, descricao)
    default_subregions = [

        # Subregions for "Bosques dos Serafins."
        (1, None, None, None, None, None, 'Clareira Central', 'Uma clareira iluminada no coração do bosque.'),
        (1, None, 1, None, None, None, 'Caminho dos Serafins', 'Caminho que leva à morada dos serafins.')
    ]

    cur.executemany("""
        INSERT INTO sub_regiao (
            regiao_id, armazenamento_id, norte_id, leste_id, oeste_id, sul_id, nome, descricao
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, default_subregions)
    conn.commit()

    print("add_defaults: Default subregions inserted successfully!")

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456"
)

# Test connection: print connection status
if not conn.status:
    print("python: Connection failed with server.")
    exit(1)

print("python: Connection status: ", conn.status)

# Get all table names from the database.
def get_table_names(cur) -> list:
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cur.fetchall()
    return [table[0] for table in tables]
    

with conn.cursor() as cur:
    
    # Process command line arguments.
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "delete" or arg == "reset":
            delete_tables(cur)
            if arg == "reset":
                execute_file("./source/init.sql", conn, cur)
        exit(0)

    if len(get_table_names(cur)) == 0:
        execute_file("./source/init.sql", conn, cur)
        add_defaults(conn, cur)
        
    print(get_table_names(cur))