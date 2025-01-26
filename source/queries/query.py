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
            SELECT sr2.nome AS sub_regiao_destino, src.direcao, src.situacao
            FROM sub_regiao_conexao src
            JOIN sub_regiao sr1 ON src.sub_regiao_1 = sr1.id
            JOIN sub_regiao sr2 ON src.sub_regiao_2 = sr2.id
            WHERE sr1.id = %s;
            """, (sub_regiao_id,)
        )
        result = cur.fetchall()
        return result

# List enemys from a subregion
def list_enemys_subregion(conn, sub_regiao_id):
    with conn.cursor() as cur:
        cur.execute(
            """            
            SELECT i.descricao, i.elemento, i.vida_maxima, i.xp_obtido, i.moedas_obtidas
            FROM inimigo i
            JOIN inimigo_instancia ii ON i.id = ii.inimigo_id
            WHERE ii.sub_regiao_id = %s;
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
    
# List all characters 
def list_all_characters(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, nome, elemento FROM personagem")
        result = cur.fetchall()
        return result
    
# List character with id
def list_character_id(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM personagem WHERE id = {character_id}")
        result = cur.fetchone()
        return result
    
def list_item_inventory(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(f"SELECT i.nome, i.descricao, ii.quantidade FROM inventario inv JOIN item_instancia ii ON inv.id = ii.inventario_id JOIN item i ON ii.item_id = i.id WHERE inv.personagem_id = {character_id};")
        result = cur.fetchall()
        return result