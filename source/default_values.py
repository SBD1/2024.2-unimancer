import psycopg2

# Creating default values to store in the database

def populate_database(conn):
    with conn.cursor() as cur:
        try:
            # Adding regions
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

            print("Regions added successfully!")

            # insert subregions
            default_subregions = [
                # Sub-regiões de "Bosques dos Serafins"
                (1, None, None, None, None, None, 'Clareira Central', 'Uma clareira iluminada no coração do bosque.'),
                (1, None, 2, None, None, None, 'Trilha Norte', 'Uma trilha que leva ao norte do bosque.'),
                (1, None, None, 3, None, None, 'Trilha Leste', 'Uma trilha que leva ao leste do bosque.'),
                (1, None, None, None, 4, None, 'Trilha Oeste', 'Uma trilha que leva ao oeste do bosque.'),

                # Sub-regiões de "Deserto de Obsidiana"
                (2, None, None, None, None, None, 'Oásis Escondido', 'Um pequeno oásis no meio do deserto.'),
                (2, None, 6, None, None, None, 'Dunas do Norte', 'Dunas escaldantes ao norte do deserto.'),
                (2, None, None, 7, None, None, 'Dunas do Leste', 'Dunas escaldantes ao leste do deserto.'),
                (2, None, None, None, 8, None, 'Dunas do Oeste', 'Dunas escaldantes ao oeste do deserto.'),

                # Sub-regiões de "Lago dos Espelhos"
                (3, None, None, None, None, None, 'Ilha Central', 'Uma ilha no centro do lago.'),
                (3, None, 10, None, None, None, 'Margem Norte', 'A margem norte do lago.'),
                (3, None, None, 11, None, None, 'Margem Leste', 'A margem leste do lago.'),
                (3, None, None, None, 12, None, 'Margem Oeste', 'A margem oeste do lago.'),

                # Sub-regiões de "Planície dos Ventos"
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

            print("subregions added successfully!")
            conn.commit()

        except Exception as e:
            print(f"error to populate database: {e}")
            conn.rollback()

# connect to database
if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123456"
    )

    print("connected to database!")
    populate_database(conn)
    print("database populated successfully!")
    conn.close()
            