from numpy import character
from logic.enemy import Enemy
from logic.character import Character
from typing import List, Tuple

# Create a character.
def add_character(conn, nome: str, elemento: str) -> None:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT criar_personagem(
                '{nome}',
                '{elemento}'
            )"""
        )
        result = cur.fetchone()
        conn.commit()
        return result[0]

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
def get_subregions_character(conn, sub_regiao_id: int) -> List[Tuple]:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
                sr2.id,
                sr2.nome,
                src.direcao,
                src.situacao
            FROM sub_regiao_conexao src
            JOIN sub_regiao sr1 ON src.sub_regiao_1 = sr1.id
            JOIN sub_regiao sr2 ON src.sub_regiao_2 = sr2.id
            WHERE sr1.id = {sub_regiao_id};
            """
        )
        result = cur.fetchall()
        return result

# List enemys from a subregion
def get_alive_enemies_subregion(conn, sub_region_id: int) -> List[Tuple]:
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
                i.dialogo,
                i.emoji
            FROM inimigo i
            JOIN inimigo_instancia ii ON i.id = ii.inimigo_id
            JOIN sub_regiao sr ON ii.sub_regiao_id = sr.id
            WHERE ii.sub_regiao_id = {sub_region_id} AND ii.vida > 0;
            """
        )
        result = cur.fetchall()
    
    return result

# get enemy info 
#def get_enemy_info(conn, enemy_id):
#    with conn.cursor() as cur:
#        cur.execute(
#            f"""
#            SELECT
#                i.nome,
#                ii.id,
#                i.descricao,
#                i.elemento,
#                ii.vida,
#                i.vida_maxima,
#                i.xp_obtido,
#                i.inteligencia,
#                i.moedas_obtidas,
#                i.conhecimento_arcano,
#                i.energia_arcana_maxima,
#                i.emoji
#            FROM inimigo i
#            JOIN inimigo_instancia ii ON ii.inimigo_id = i.id
#            WHERE n.id = {enemy_id};
#            """
#        )
#        result = cur.fetchone()
#        return result

# Function to get subregion description
def get_subregion_info(conn, sub_region_id: int):
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
                descricao,
                nome
            FROM sub_regiao WHERE id = {sub_region_id}
            """
        )
        result = cur.fetchone()
        return result

# List all citizens from a subregion.
def get_citizens_subregion(conn, sub_regiao_id: int) -> List[Tuple]:
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
        cur.execute("SELECT id, nome, elemento FROM personagem WHERE vida > 0")
        result = cur.fetchall()
        return result
    
# Get all information of a character.
def get_character_info(conn, character_id):
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
                -- Seleciona os itens que estão na mochila do personagem
                SELECT 
                    i.tipo,
                    CASE 
                        WHEN i.tipo = 'Poção' THEN p.nome
                        WHEN i.tipo = 'Pergaminho' THEN pe.nome
                        WHEN i.tipo = 'Acessório' THEN a.nome
                        ELSE 'Desconhecido'
                    END AS nome,
                    CASE 
                        WHEN i.tipo = 'Poção' THEN p.descricao
                        WHEN i.tipo = 'Pergaminho' THEN pe.descricao
                        WHEN i.tipo = 'Acessório' THEN a.descricao
                        ELSE 'Sem descrição'
                    END AS descricao,
                    COUNT(ii.id) AS quantidade
                FROM item_instancia ii
                JOIN item i ON ii.item_id = i.id
                LEFT JOIN pocao p ON i.id = p.id
                LEFT JOIN pergaminho pe ON i.id = pe.id
                LEFT JOIN acessorio a ON i.id = a.id
                WHERE ii.mochila_id = %s
                GROUP BY 
                    i.tipo, 
                    p.nome, 
                    pe.nome, 
                    a.nome, 
                    p.descricao, 
                    pe.descricao, 
                    a.descricao
            """, (inventario_id,))

            items.extend(cur.fetchall())

    return items

def get_civilian_info(conn, npc_name):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT c.nome, c.descricao, c.id
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



## function to get all LERNED spells from player
#def get_learned_spells(conn, character_id):
#    with conn.cursor() as cursor:
#        cursor.execute(
#            f"""
#                SELECT
#                    *
#                FROM feitico_aprendido fa
#                WHERE fa.inventario_id = {character_id}
#            """
#    )
#        return cursor.fetchall()

# function to get all Character damage spells
def get_damage_spells(conn, character_id: int) -> List[Tuple]:
    with conn.cursor() as cur:
        cur.execute(
            f"""
                SELECT
                    fd.nome,
                    f.tipo,
                    fd.descricao, 
                    fd.energia_arcana,
                    fd.dano_total
                FROM inventario i 
                JOIN grimorio g ON i.id = g.id
                JOIN feitico_aprendido fa ON g.id = fa.grimorio_id
                JOIN feitico f ON f.id = fa.feitico_id
                JOIN feitico_dano fd ON f.id = fd.id
                WHERE i.personagem_id = {character_id};
            """
        )
        return cur.fetchall()

# function to get all Character area damage spells
def get_damage_area_spells(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(
            f"""
                SELECT
                    fda.nome,
                    f.tipo,
                    fda.descricao, 
                    fda.energia_arcana,
                    fda.dano,
                    fda.qtd_inimigos_afetados
                FROM inventario i 
                JOIN grimorio g ON i.id = g.id
                JOIN feitico_aprendido fa ON g.id = fa.grimorio_id
                JOIN feitico f ON f.id = fa.feitico_id
                JOIN feitico_dano_area fda ON f.id = fda.id
                WHERE i.personagem_id = {character_id};
            """
        )
        return cur.fetchall()

# function to get all Character healing spells
def get_healing_spells(conn, character_id: int) -> List[Tuple]:
    with conn.cursor() as cur:
        cur.execute(
            f"""
                SELECT
                    fc.nome,
                    f.tipo,
                    fc.descricao,
                    fc.energia_arcana,
                    fc.qtd_cura
                FROM inventario i 
                JOIN grimorio g ON i.id = g.id
                JOIN feitico_aprendido fa ON g.id = fa.grimorio_id
                JOIN feitico f ON f.id = fa.feitico_id
                JOIN feitico_cura fc ON f.id = fc.id
                WHERE i.personagem_id = {character_id};
            """
        )
        return cur.fetchall()

# function to get all Character potions
def get_potions(conn, character_id: int) -> List[Tuple]:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT p.id, p.nome, p.descricao, p.turnos, p.usado
            FROM pocao p
            JOIN item_instancia ii ON p.id = ii.item_id
            JOIN inventario inv ON ii.mochila_id = inv.id
            WHERE inv.personagem_id = %s;
        """, (character_id,))
        return cur.fetchall()

# function to set potion as used
def apply_potion_effect(conn, potion_id: int) -> int:
    with conn.cursor() as cur:
        cur.execute(f"""
            UPDATE pocao
            SET usado = TRUE
            WHERE id = {potion_id};
        """)
        conn.commit()

# Update `energia_arcana` after using spell.
def get_character_mp(conn, character_id: int, spell_value: int) -> int:
    with conn.cursor() as cur:
        cur.execute(f"""
            UPDATE personagem
            SET energia_arcana = energia_arcana - {spell_value}
            WHERE id = {character_id}
            RETURNING energia_arcana;
        """)
        result = cur.fetchone()
        conn.commit()
        return result[0]
    
    return None

# function to reset enemies
def reset_enemies(conn, subregiao_id: int) -> None:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            UPDATE
                inimigo_instancia ii
            SET
                vida = i.vida_maxima
            FROM inimigo i
            WHERE ii.inimigo_id = i.id AND ii.sub_regiao_id = {subregiao_id}
            """
        )
        conn.commit()

# function to change subregion
def update_character_subregion(conn, character_id: int, sub_region_id: int) -> int:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            UPDATE personagem
                SET sub_regiao_id = {sub_region_id}
            WHERE personagem.id = {character_id}
            RETURNING sub_regiao_id;
            """
        )
        result = cur.fetchone()[0]
        conn.commit()
        return result

# Update a combat between a caracter and enemies.
def update_combat(conn , enemies: List[Enemy], character: Character) -> None:
    with conn.cursor() as cursor:
        for enemy in enemies:
            cursor.execute(
                f"""
                SELECT atualizar_combate(
                    {character.id},
                    {enemy.id},
                    {int(character.vida)},
                    {enemy.vida}
                );
                """
            )
        conn.commit()

# Get character's info.
def get_character_info(conn, id: int) -> Tuple:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT *
            FROM personagem
            WHERE id = {id};
            """)
        result = cur.fetchone()

        return result

# Get the inventory id of a character.
def get_inventory(conn, type: str, character_id: int) -> int:

    if type != 'mochila' and type != 'grimorio':
        raise ValueError("Invalid type. Must be 'mochila' or 'grimorio'.")
    
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT
                inventario.id
            FROM {type}
            JOIN inventario ON personagem_id = {character_id} AND {type}.id = inventario.id;
            """
        )
        result = cur.fetchone()[0]
        return result

# Add a spell to a character spellbook.
def add_learned_spells(conn, spellbook_id: int, spells_ids: List[int]) -> None:
    with conn.cursor() as cur:
        for spell_id in spells_ids:
            cur.execute(
                f"""
                INSERT INTO feitico_aprendido (grimorio_id, feitico_id)
                VALUES ({spellbook_id}, {spell_id});
                """
            )
        conn.commit()
    
# Add an instance of item in a backpack.
def add_items_instance(conn, backpack_id: int, item_ids: List[int]) -> None:
    with conn.cursor() as cur:
        for item_id in item_ids:
            cur.execute(
                f"""
                INSERT INTO item_instancia (item_id, mochila_id)
                VALUES ({item_id}, {backpack_id})
                RETURNING item_id;
                """
            )
        conn.commit()
    