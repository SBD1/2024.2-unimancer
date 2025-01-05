# Connect to PostgreSQL database in Docker container.
# Use psycopg2 library to connect to PostgreSQL database.

import psycopg2
import sys

# For debugging purposes, force delete every single table of the database and it's dependencies.
# So that we can create the default lines of the database again.
def delete_tables(cur):
    try:
        cur.execute("DROP TABLE IF EXISTS tipo_item CASCADE")
        cur.execute("DROP TABLE IF EXISTS armazenamento CASCADE")
        cur.execute("DROP TABLE IF EXISTS regiao CASCADE")
        cur.execute("DROP TABLE IF EXISTS sub_regiao CASCADE")
        cur.execute("DROP TABLE IF EXISTS personagem CASCADE")
        cur.execute("DROP TABLE IF EXISTS inventario CASCADE")
        cur.execute("DROP TABLE IF EXISTS tipo_npc CASCADE")
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
        print(f"Error deleting tables: {e}")

    print("Deleted all tables.")
    
    exit(0)

# Initialise database with the file `init.sql`:
# Open and read the file `init.sql`
def initialize_database(conn, cur):
    with open("./source/init.sql", "r") as file:
        sql = file.read()
        cur.execute(sql)
        conn.commit()

        # Insert default regions.
        default_regions = [
            ('Bosques dos Serafins', 'Bosque com o alto índice de serafins.', 'Fogo'),
            ('Deserto de Obsidiana', 'Deserto com areias negras e calor extremo.', 'Fogo'),
            ('Lago dos Espelhos', 'Lago tranquilo com águas cristalinas.', 'Água'),
            ('Planície dos Ventos', 'Vasta planície com ventos constantes.', 'Ar'),
        ]

        cur.executemany("""
            INSERT INTO regiao (nome, descricao, elemento)
            VALUES (%s, %s, %s)
        """, default_regions)
        conn.commit()

        print("Default regions inserted successfully!")

        # Insert default subregions.
        default_subregions = [
            # To-do: add storages, then specify the storage id in the subregion.

            # Subregions for "Bosques dos Serafins".
            (1, None, None, None, None, None, 'Clareira Central', 'Uma clareira iluminada no coração do bosque.'),
            (1, None, 2, None, None, None, 'Trilha Norte', 'Uma trilha que leva ao norte do bosque.'),
            (1, None, None, 3, None, None, 'Trilha Leste', 'Uma trilha que leva ao leste do bosque.'),
            (1, None, None, None, 4, None, 'Trilha Oeste', 'Uma trilha que leva ao oeste do bosque.'),

            # Subregions for "Deserto de Obsidiana".
            (2, None, None, None, None, None, 'Oásis Escondido', 'Um pequeno oásis no meio do deserto.'),
            (2, None, 6, None, None, None, 'Dunas do Norte', 'Dunas escaldantes ao norte do deserto.'),
            (2, None, None, 7, None, None, 'Dunas do Leste', 'Dunas escaldantes ao leste do deserto.'),
            (2, None, None, None, 8, None, 'Dunas do Oeste', 'Dunas escaldantes ao oeste do deserto.'),

            # Subregions for "Lago dos Espelhos".
            (3, None, None, None, None, None, 'Ilha Central', 'Uma ilha no centro do lago.'),
            (3, None, 10, None, None, None, 'Margem Norte', 'A margem norte do lago.'),
            (3, None, None, 11, None, None, 'Margem Leste', 'A margem leste do lago.'),
            (3, None, None, None, 12, None, 'Margem Oeste', 'A margem oeste do lago.'),

            # Subregions for "Planície dos Ventos".
            (4, None, None, None, None, None, 'Campo Aberto', 'Um vasto campo aberto.'),
            (4, None, 14, None, None, None, 'Vale do Norte', 'Um vale ao norte da planície.'),
            (4, None, None, 15, None, None, 'Vale do Leste', 'Um vale ao leste da planície.'),
            (4, None, None, None, 16, None, 'Vale do Oeste', 'Um vale ao oeste da planície.'),
        ]

        cur.executemany("""
            INSERT INTO sub_regiao (
                id_regiao, id_armazenamento, id_norte, id_leste, id_oeste, id_sul, nome, descricao
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, default_subregions)
        conn.commit()

        print("Default subregions inserted successfully!")

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123456"
)

# Test connection: print connection status
if not conn.status:
    print("Connection failed with server.")
    exit(1)

print("Connection status: ", conn.status)

with conn.cursor() as cur:

    if len(sys.argv) > 1 and sys.argv[1] == "delete":
        delete_tables(cur)

    # Send the SQL command to the database.
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

    # Fetch all the results.
    tables = cur.fetchall()

    if len(tables) == 0:
        initialize_database(conn, cur)