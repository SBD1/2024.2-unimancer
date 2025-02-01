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
            SELECT ii.id, n.nome, i.descricao, i.elemento, ii.vida, i.vida_maxima, i.xp_obtido, i.inteligencia, i.moedas_obtidas, i.conhecimento_arcano, i.energia_arcana_maxima, i.dialogo
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
            SELECT 
                n.nome,
                COALESCE(
                    CASE 
                        WHEN q.id IS NOT NULL THEN 'Quester'
                        WHEN m.id IS NOT NULL THEN 'Mercador'
                        ELSE 'Civil'
                    END, 
                    n.tipo::TEXT
                ) AS tipo
            FROM npc n
            JOIN civil c ON n.id = c.id
            LEFT JOIN quester q ON c.id = q.id
            LEFT JOIN mercador m ON c.id = m.id
            WHERE c.sub_regiao_id = %s;
            """, 
            (sub_regiao_id,)
        )
        result = cur.fetchall()
        return result

def get_npc_details(conn, type):
    with conn.cursor() as cur:

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
        cur.execute("""
            SELECT id FROM inventario WHERE personagem_id = %s AND tipo = 'Mochila'
        """, (character_id,))
        
        inventarios = cur.fetchall()
        
        items = []
        for inventario in inventarios:
            inventario_id = inventario[0]
            cur.execute("""
                SELECT item.nome, item.descricao, COUNT(item_instancia.id) as quantidade
                FROM item_instancia
                JOIN item ON item_instancia.item_id = item.id
                WHERE item_instancia.inventario_id = %s
                GROUP BY item.nome, item.descricao
            """, (inventario_id,))
            
            items.extend(cur.fetchall())
    return items

def get_civilian_info(conn, npc_name):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT n.nome, c.descricao
            FROM npc n
            JOIN civil c ON n.id = c.id
            WHERE n.nome = %s;
            """, (npc_name,)
        )
        result = cur.fetchone()
        return {
            'nome': result[0],
            'descricao': result[1],
            'npc_id': result[2]
        }

# get quest given a quester id 
def get_quest(conn, quester_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT q.titulo, q.descricao, qu.dialogo, q.id, q.recompensa
            FROM quest q 
            LEFT JOIN quester qu ON qu.id = q.quester_id
            WHERE q.quester_id = %s;
            """, (quester_id,)
        )
        result = cur.fetchall()
        return {
            'title': result[0][0],
            'description': result[0][1],
            'dialog': result[0][2],
            'quest_id': result[0][3],
            'reward': result[0][4]
        }


# Function to get all spells
def get_spells(conn, character_id):
    with conn.cursor() as cur:
       cur.execute("""
           SELECT feitico.descricao, feitico.energia_arcana
           FROM inventario
           JOIN feitico_aprendido ON inventario.id = feitico_aprendido.inventario_id
           JOIN feitico ON feitico_aprendido.feitico_id = feitico.id
           WHERE inventario.personagem_id = %s;
       """, (character_id,))
       
       return cur.fetchall()

# function to change subregion
def fetch_subregion_id_by_name(name, conn):
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT id FROM sub_regiao WHERE nome = %s", (name,))
        result = cur.fetchone()
        return result[0] if result else None
