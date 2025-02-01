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
def list_alive_enemys_subregion(conn, sub_regiao_id):
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
                ii.id,
                i.nome,
                i.descricao,
                i.elemento,
                ii.vida,
                i.vida_maxima,
                i.xp_obtido,
                i.inteligencia,
                i.moedas_obtidas,
                i.conhecimento_arcano,
                i.energia_arcana_maxima,
                i.dialogo
            FROM inimigo i
            JOIN inimigo_instancia ii ON i.id = ii.inimigo_id
            JOIN sub_regiao sr ON ii.sub_regiao_id = sr.id
            WHERE ii.sub_regiao_id = {sub_regiao_id} AND ii.vida > 0;
            """
        )
        result = cur.fetchall()
        return result

# get enemy info 
def get_enemy_info(conn, enemy_id):
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
                i.nome,
                ii.id,
                i.descricao,
                i.elemento,
                ii.vida,
                i.vida_maxima,
                i.xp_obtido,
                i.inteligencia,
                i.moedas_obtidas,
                i.conhecimento_arcano,
                i.energia_arcana_maxima
            FROM inimigo i
            JOIN inimigo_instancia ii ON ii.inimigo_id = i.id
            WHERE n.id = {enemy_id};
            """
        )
        result = cur.fetchone()
        return result

# List all citizens from a subregion.
def list_citizens_subregion(conn, sub_regiao_id):
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT 
                c.nome,
                c.descricao,
                COALESCE(
                    CASE 
                        WHEN q.id IS NOT NULL THEN 'Quester'
                        WHEN m.id IS NOT NULL THEN 'Mercador'
                        ELSE 'Civil'
                    END, 
                    c.tipo::TEXT
                ) AS tipo
            FROM civil c
            LEFT JOIN quester q ON c.id = q.id
            LEFT JOIN mercador m ON c.id = m.id
            WHERE c.sub_regiao_id = {sub_regiao_id};
            """
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
            SELECT c.nome, c.descricao
            FROM civil c
            WHERE c.nome = %s;
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



# function to get all LERNED spells from player
def get_learned_spells(conn, character_id):
    with conn.cursor() as cursor:
        cursor.execute(
            """
                SELECT f.*, fd.*, fda.*, fc.*
                FROM feitico_aprendido fa
                JOIN feitico f ON fa.feitico_id = f.id
                LEFT JOIN feitico_dano fd ON f.id = fd.id
                LEFT JOIN feitico_dano_area fda ON f.id = fda.id
                LEFT JOIN feitico_cura fc ON f.id = fc.id
                WHERE fa.inventario_id = %s
            """, (character_id))
        return cursor.fetchall()

# function to get all Character damage spells
def get_damage_spells(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(
            """
                SELECT feitico_dano.nome, feitico_dano.descricao, fetico_dano.energia_arcana
                FROM inventario
                JOIN feitico_aprendido ON inventario.id = feitico_aprendido.inventario_id
                JOIN feitico_dano ON feitico_aprendido.inventario_id = feitico_dano.id
                WHERE inventario.personagem_id = %s;
            """, (character_id)
        )

# function to get all Character area damage spells
def get_damage_area_spells(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(
            """
                SELECT feitico_dano_area.nome, feitico_dano_area.descricao, fetico_dano.energia_arcana
                FROM inventario
                JOIN feitico_aprendido ON inventario.id = feitico_aprendido.inventario_id
                JOIN feitico_dano_area ON feitico_aprendido.inventario_id = feitico_dano_area.id
                WHERE inventario.personagem_id = %s;
            """, (character_id)
        )

# function to get all Character healing spells
def get_healing_spells(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(
            """
                SELECT feitico_cura.nome, feitico_cura.descricao, fetico_dano.energia_arcana
                FROM inventario
                JOIN feitico_aprendido ON inventario.id = feitico_aprendido.inventario_id
                JOIN feitico_cura ON feitico_aprendido.inventario_id = feitico_cura.id
                WHERE inventario.personagem_id = %s;
            """, (character_id)
        )
    

# function to change subregion
def fetch_subregion_id_by_name(name, conn):
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT id FROM sub_regiao WHERE nome = %s", (name,))
        result = cur.fetchone()
        return result[0] if result else None
