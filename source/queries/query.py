# get regions and respective elements
def regions(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT r.nome, r.elemento, r.descricao
            FROM regiao r; 
            """
        )
        result = cur.fetchall()
        return result

# get subregions from a region
def subregions(conn, region_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT sr.nome, sr.descricao
            FROM sub_regiao sr
            WHERE sr.regiao_id = %s;
            """, (region_id,)
        )
        result = cur.fetchall()
        return result

# get subregions where character can go
def get_subregions_character(conn, sub_regiao_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT 
                CASE 
                    WHEN src.sub_regiao_1 = %s THEN sr2.nome
                    ELSE sr1.nome
                END AS sub_regiao_destino,
                src.direcao, 
                src.situacao
            FROM sub_regiao_conexao src
            JOIN sub_regiao sr1 ON src.sub_regiao_1 = sr1.id
            JOIN sub_regiao sr2 ON src.sub_regiao_2 = sr2.id
            WHERE sr1.id = %s OR sr2.id = %s;
            """, (sub_regiao_id,)
        )
        result = cur.fetchall()
        return result

# List all NPC's from a subregion
def list_npcs_subregion(conn, sub_regiao_id):
    with conn.cursor() as cur:
        cur.execute(
            """            
            SELECT n.nome, n.tipo
            FROM npc n
            JOIN civil c ON n.id = c.id
            WHERE c.sub_regiao_id = %s;
            """, (sub_regiao_id,)
        )
        result = cur.fetchall()
        return result