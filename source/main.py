# Connect to PostgreSQL database in Docker container.
# Use psycopg2 library to connect to PostgreSQL database.

import psycopg2;

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

# If there are not tables in the database, run the following code to list all tables.
# List all tables in the database.
with conn.cursor() as cur:

    # Send the SQL command to the database.
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

    # Fetch all the results.
    tables = cur.fetchall()

    # If there are no tables, create the tables.
    if len(tables) == 0:
        # Initialise database with the file `init.sql`:
        # Open and read the file `init.sql`
        with open("./source/init.sql", "r") as file:
            sql = file.read()
        
            # Send the SQL commands to the database.
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()

                
                # Create default regions with elements Water, Fire, Earth and Air.
                try:
                    regioes = [
                        (
                            'Bosques dos Serafins',
                            'Bosque com o alto índice de serafins, cheio de árvores antigas e um brilho místico.',
                            'Fogo'
                        ),
                        (
                            'Deserto de Obsidiana',
                            'Um deserto escaldante, onde as areias negras refletem o calor do sol.',
                            'Fogo'
                        ),
                        (
                            'Lago dos Espelhos',
                            'Um lago tranquilo com águas cristalinas que refletem o céu perfeitamente.',
                            'Água'
                        ),
                        (
                            'Oásis Perdido',
                            'Um oásis escondido no meio de um deserto interminável.',
                            'Água'
                        ),
                        (
                            'Floresta Esmeralda',
                            'Uma floresta vibrante, repleta de árvores verdes e vida selvagem.',
                            'Terra'
                        ),
                        (
                            'Caverna de Cristais',
                            'Uma caverna subterrânea cheia de cristais luminosos.',
                            'Terra'
                        ),
                        (
                            'Planície dos Ventos',
                            'Uma vasta planície onde os ventos nunca param de soprar.',
                            'Ar'
                        ),
                        (
                            'Céu dos Dragões',
                            'Uma região acima das nuvens, lar de dragões e outros seres alados.',
                            'Ar'
                        )
                    ]

                    cur.executemany("INSERT INTO regiao (nome, descricao, elemento) VALUES (%s, %s, %s)", regioes)
                    conn.commit()
                    print("Created default regions!")

                    # List all regions
                    cur.execute("SELECT * FROM regiao")
                    resultados = cur.fetchall()
                    for linha in resultados:
                        print(linha)
                
                except Exception as e:
                    print(f"Error creating default regions: {e}")

                # Create default subregions.

