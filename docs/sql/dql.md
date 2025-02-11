# Data Query Language - DQL

## Introdução

DQL é um conjunto de comandos que permitem consultar e recuperar dados de um banco de dados relacional.


## DQL

```py
# Function to get all items in a subregion
def get_subregion_items(conn, subregion_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT i.id, i.tipo, arm.quantidade, 
                   COALESCE(p.nome, ac.nome, po.nome) AS nome, 
                   COALESCE(p.descricao, ac.descricao, po.descricao) AS descricao
            FROM armazenamento arm
            JOIN item i ON arm.item_id = i.id
            LEFT JOIN pergaminho p ON i.id = p.id
            LEFT JOIN acessorio ac ON i.id = ac.id
            LEFT JOIN pocao po ON i.id = po.id
            WHERE arm.id IN (
                SELECT armazenamento_id 
                FROM sub_regiao 
                WHERE id = %s
            );
            """,
            (subregion_id,)
        )
        return cur.fetchall()

# Check if can pickup itens
def can_pick_up_item(conn, character_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT COUNT(*) 
            FROM item_instancia ii
            JOIN mochila m ON ii.mochila_id = m.id
            JOIN inventario inv ON m.id = inv.id
            WHERE inv.personagem_id = %s;
            """,
            (character_id,)
        )
        count = cur.fetchone()[0]
        # verify is has enough space
        cur.execute(
            """
            SELECT peso_total 
            FROM mochila m
            JOIN inventario inv ON m.id = inv.id
            WHERE inv.personagem_id = %s;
            """,
            (character_id,)
        )
        peso_total = cur.fetchone()[0]
        return count < peso_total 


def get_item_sell_price(conn, item_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT preco FROM (
            SELECT id, preco FROM pergaminho
            UNION ALL
            SELECT id, preco FROM acessorio
            UNION ALL
            SELECT id, preco FROM pocao
        ) AS items
        WHERE id = %s
    """, (item_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else 0

# function to get all merchant items
def get_merchant_items(conn, mercador_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                i.id AS item_id,
                COALESCE(p.nome, ac.nome, po.nome) AS nome,  -- Nome do item
                COALESCE(p.preco, ac.preco, po.preco) AS preco,  -- Preço do item
                ar.quantidade  -- Quantidade disponível
            FROM armazenamento_mercador am
            JOIN armazenamento ar ON am.armazenamento_id = ar.id
            JOIN item i ON ar.item_id = i.id
            LEFT JOIN pergaminho p ON i.id = p.id
            LEFT JOIN acessorio ac ON i.id = ac.id
            LEFT JOIN pocao po ON i.id = po.id
            WHERE am.mercador_id = %s;
        """, (mercador_id,))
        return cur.fetchall()

# function to get all merchant in a subregion
def get_merchants_subregion(conn, sub_regiao_id):
    with conn.cursor() as cur:
        cur.execute(
            f"""
                SELECT m.id, c.nome
                FROM mercador m
                JOIN civil c ON m.id = c.id
                WHERE c.sub_regiao_id = {sub_regiao_id} 
            """
        )
        return cur.fetchall()


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


def end_combat(conn, character_id: int, enemies_ids: List[int] = []) -> None:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT end_combat({character_id}, ARRAY{enemies_ids}::integer[]);
            """
        )
        result = cur.fetchall()
        return result

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
                SELECT 
                    i.id AS item_id,  -- Adicione esta linha
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
                    i.id,  -- Agrupe por item_id para garantir a unicidade
                    i.tipo, 
                    p.nome, 
                    pe.nome, 
                    a.nome, 
                    p.descricao, 
                    pe.descricao, 
                    a.descricao
            """, (inventario_id,))

            items.extend(cur.fetchall())

    return items  # return: (item_id, tipo, nome, descricao, quantidade)

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
            SELECT
                ii.id,
                p.id,
                p.nome,
                p.descricao,
                ii.usado
            FROM pocao p
            JOIN item_instancia ii ON p.id = ii.item_id
            JOIN inventario inv ON ii.mochila_id = inv.id
            WHERE inv.personagem_id = %s;
        """, (character_id,))
        return cur.fetchall()

```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |
| `1.1`  | 13/01/2024 | Correções e Adições | Grupo |
| `2.0`  | 10/02/2025 | Atualização   | Grupo |