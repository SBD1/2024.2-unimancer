# Data Manipulation Language - DML

## Introdução

DML é um conjunto de instruções SQL que permitem consultar, adicionar, editar e excluir dados de tabelas ou visualizações de banco de dados

## DML

```py
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


# Delete a item instance from a character inventory.
def delete_item_instance(conn, id: int) -> None:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            DELETE FROM item_instancia
            WHERE id = {id};
            """
        )
        conn.commit()

# Activate an instance of item (potion).
def update_item_instance(conn, id: int, used: bool) -> None:
    with conn.cursor() as cur:
        cur.execute(
            f"""
            UPDATE item_instancia
            SET usado = {used}
            WHERE id = {id};
            """
        )
        conn.commit()

# Update `energia_arcana` after using spell.
def get_update_character_mp(conn, character_id: int, spell_value: int) -> int:
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
                    {int(enemy.vida)}
                );
                """
            )
        conn.commit()

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
                INSERT INTO item_instancia (item_id, mochila_id, usado)
                VALUES ({item_id}, {backpack_id}, FALSE)
                RETURNING item_id;
                """
            )
        conn.commit()


# function to sell an item to merchant
def sell_item(conn, character_id, item_id, preco_venda, merchant_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM item_instancia
            WHERE id = (
                SELECT ii.id
                FROM item_instancia ii
                JOIN mochila m ON ii.mochila_id = m.id
                JOIN inventario inv ON m.id = inv.id
                WHERE inv.personagem_id = %s AND ii.item_id = %s
                LIMIT 1
            )
        """, (character_id, item_id))
        
        cursor.execute("""
            INSERT INTO transacao (mercador_id, personagem_id, item_id)
            VALUES (%s, %s, %s)
        """, (merchant_id, character_id, item_id))
        
        cursor.execute("""
            UPDATE personagem
            SET moedas = moedas + %s
            WHERE id = %s
        """, (preco_venda, character_id))
        
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Erro ao vender item: {e}")
        return False


def buy_item(conn, character_id, item_id, preco):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT moedas FROM personagem WHERE id = %s", (character_id,))
            moedas = cur.fetchone()[0]
            if moedas < preco:
                raise Exception("Moedas insuficientes")

            cur.execute("""
                UPDATE armazenamento
                SET quantidade = quantidade - 1
                WHERE item_id = %s AND quantidade > 0
                RETURNING id
            """, (item_id,))
            armazenamento_id = cur.fetchone()
            if armazenamento_id is None:
                raise Exception("Item não disponível no armazenamento")

            cur.execute("""
                INSERT INTO item_instancia (item_id, mochila_id)
                VALUES (%s, (SELECT m.id FROM mochila m JOIN inventario i ON m.id = i.id WHERE i.personagem_id = %s))
            """, (item_id, character_id))

            cur.execute("""
                UPDATE personagem
                SET moedas = moedas - %s
                WHERE id = %s
            """, (preco, character_id))

            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

# function to transfer itens to your inventory
def transfer_item_to_inventory(conn, character_id, item_id, quantidade):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE armazenamento
            SET quantidade = quantidade - %s
            WHERE item_id = %s AND id IN (
                SELECT armazenamento_id 
                FROM sub_regiao 
                WHERE id = (
                    SELECT sub_regiao_id 
                    FROM personagem 
                    WHERE id = %s
                )
            );
            """,
            (quantidade, item_id, character_id)
        )
        
        cur.execute(
            """
            INSERT INTO item_instancia (item_id, mochila_id)
            SELECT %s, m.id
            FROM mochila m
            JOIN inventario inv ON m.id = inv.id
            WHERE inv.personagem_id = %s;
            """,
            (item_id, character_id)
        )
        conn.commit()
```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |
| `1.1`  | 13/01/2024 | Atualização | Grupo |
| `1.2`  | 03/02/2025 | Atualização entrega 3 | Grupo |
| `2.0`  | 10/02/2025 | Atualização   | Grupo |