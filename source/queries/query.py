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
            SELECT n.id, n.nome, i.descricao, i.elemento
            FROM npc n
            JOIN inimigo i ON n.id = i.id
            JOIN inimigo_instancia ii ON i.id = ii.inimigo_id
            WHERE ii.sub_regiao_id = %s AND ii.vida > 0;
            """, (sub_regiao_id,)
        )
        result = cur.fetchall()
        return result

# get enemy info
def get_enemy_info(conn, enemy_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT n.nome, ii.id, i.armazenamento_id, i.descricao, i.elemento, ii.vida, i.vida_maxima, i.xp_obtido, i.inteligencia, i.moedas_obtidas,  i.conhecimento_arcano, i.energia_arcana_maxima
            FROM npc n
            JOIN inimigo i ON n.id = i.id
            JOIN inimigo_instancia ii ON ii.inimigo_id = i.id
            WHERE n.id = %s;
            """, (enemy_id,)
        )
        result = cur.fetchone()
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
        cur.execute(f"SELECT i.nome, i.descricao FROM inventario inv JOIN item_instancia ii ON inv.id = ii.inventario_id JOIN item i ON ii.item_id = i.id WHERE inv.personagem_id = {character_id};")
        result = cur.fetchall()
        return result

# Query to know if a character is a merchant, quester or civil 
def get_npc_role(conn, npc_name, npc_type):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT c.tipo
            FROM npc n
            INNER JOIN civil c ON n.id = c.id
            WHERE n.id = %s;
            """, (npc_name)
        )
        result = cur.fetchone()
        return result