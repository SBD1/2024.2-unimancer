# PROCEDURES

## Introdução

Stored Procedures são blocos de código SQL armazenados no banco de dados, permitindo a execução de várias instruções em uma única unidade. Elas melhoram o desempenho ao reduzir a comunicação entre a aplicação e o banco, além de oferecerem mais segurança ao restringir o acesso direto a tabelas. Outra vantagem é a manutenção simplificada, já que a lógica pode ser centralizada no banco de dados, facilitando atualizações sem a necessidade de alterar a aplicação. 

## Procedures

```sql
-- PostGreSQL: create `civil` linking to `npc`
CREATE OR REPLACE FUNCTION criar_civil(
    IN nome VARCHAR(100),
    IN sub_regiao_id INT,
    IN descricao TEXT,
    IN tipo TIPO_CIVIL
) RETURNS INT AS $$
DECLARE 
    npc_id INT;
BEGIN

    INSERT INTO npc (tipo)
    VALUES ('Civil')
    RETURNING id INTO npc_id;

    INSERT INTO civil (
        id,
        sub_regiao_id,
        tipo,
        nome,
        descricao
    )
    VALUES (
        npc_id,
        sub_regiao_id,
        tipo::TIPO_CIVIL,
        nome,
        descricao
    );

    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `quester` linking to `civil` using `criar_civil`.
CREATE OR REPLACE FUNCTION criar_quester(
    IN nome VARCHAR(100),
    IN sub_regiao_id INT,
    IN descricao TEXT,
    IN dialogo TEXT
) RETURNS INT AS $$
DECLARE
    npc_id INT;
BEGIN
    npc_id = criar_civil(nome, sub_regiao_id, descricao, 'Quester');

    -- create line in table `quester` linking to `npc_id`.
    INSERT INTO quester (
        id,
        num_quests,
        dialogo
    )
    VALUES (
        npc_id,
        0,
        dialogo
    );

    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `mercador` linking to `npc`
CREATE OR REPLACE FUNCTION criar_mercador(
    IN nome VARCHAR(100),
    IN sub_regiao_id INT,
    IN descricao TEXT,
    IN dialogo TEXT
) RETURNS INT AS $$
DECLARE
    npc_id INT;
BEGIN
    npc_id = criar_civil(nome, sub_regiao_id, descricao, 'Mercador');

    INSERT INTO mercador (
        id,
        dialogo
    )
    VALUES (
        npc_id,
        dialogo
    );

    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;


-- PostGreSQL: create enemy linking to npc.
CREATE OR REPLACE FUNCTION criar_inimigo(
    IN emoji TEXT,
    IN nome VARCHAR(100),
    IN descricao TEXT,
    IN elemento TEXT,
    IN vida_maxima INT,
    IN xp_obtido INT,
    IN inteligencia INT,
    IN moedas_obtidas INT,
    IN conhecimento_arcano INT,
    IN energia_arcana_maxima INT,
    IN dialogo TEXT
) RETURNS INT AS $$
DECLARE 
    npc_id INT;
BEGIN
    INSERT INTO npc (tipo)
    VALUES ('Inimigo')
    RETURNING id INTO npc_id;

    INSERT INTO inimigo (
        id,
        emoji,
        nome,
        descricao,
        elemento,
        vida_maxima,
        xp_obtido,
        inteligencia,
        moedas_obtidas,
        conhecimento_arcano,
        energia_arcana_maxima,
        dialogo
    )
    VALUES (
        npc_id,
        emoji,
        nome,
        descricao,
        elemento::TIPO_ELEMENTO,
        vida_maxima,
        xp_obtido,
        inteligencia,
        moedas_obtidas,
        conhecimento_arcano,
        energia_arcana_maxima,
        dialogo
    );
    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `personagem`
CREATE OR REPLACE FUNCTION criar_personagem(
    IN p_nome VARCHAR(20),
    IN p_elemento TEXT
) RETURNS INT AS $$
DECLARE
    v_personagem_id INT;
    v_inventario_mochila_id INT;
    v_inventario_grimorio_id INT;
BEGIN
    INSERT INTO personagem (
        sub_regiao_id,
        nome,
        elemento,
        conhecimento_arcano,
        vida,
        vida_maxima,
        xp,
        xp_total,
        energia_arcana,
        energia_arcana_maxima,
        inteligencia,
        moedas,
        nivel
    )
    VALUES (
        1,
        p_nome,
        p_elemento::TIPO_ELEMENTO,
        10,
        100,
        100,
        0,
        10,
        50,
        50,
        1,
        15,
        1
    )
    RETURNING id INTO v_personagem_id;
    -- Criar o inventário do tipo Mochila
    INSERT INTO inventario (personagem_id, tipo)
    VALUES (v_personagem_id, 'Mochila')
    RETURNING id INTO v_inventario_mochila_id;

    INSERT INTO mochila (id, peso, peso_total)
    VALUES (v_inventario_mochila_id, 0, 20);

    --  Criar o inventário do tipo Grimório
    INSERT INTO inventario (personagem_id, tipo)
    VALUES (v_personagem_id, 'Grimório')
    RETURNING id INTO v_inventario_grimorio_id;

    INSERT INTO grimorio (id, num_pag, num_pag_maximo)
    VALUES (v_inventario_grimorio_id, 0, 5);

    RETURN v_personagem_id;
END;
$$ LANGUAGE plpgsql;


-- PostGreSQL: create `acessorio`
CREATE OR REPLACE FUNCTION criar_acessorio(
  IN tipo TEXT,
  IN descricao TEXT,
  IN drop_inimigos_media INT,
  IN nome VARCHAR(200),
  IN peso INT,
  IN preco INT  
)
RETURNS INT AS $$
DECLARE
     v_item_id INT;
BEGIN
     INSERT INTO item (tipo)
     VALUES ('Acessório')
     RETURNING id INTO v_item_id;

     INSERT INTO acessorio (id, tipo, descricao, drop_inimigos_media, nome, peso, preco)
     VALUES (v_item_id, tipo::TIPO_ACESSORIO, descricao, drop_inimigos_media, nome, peso, preco);
 
     RETURN v_item_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `pergaminho`
CREATE OR REPLACE FUNCTION criar_pergaminho(
    IN p_descricao TEXT,
    IN p_drop_inimigos_media INT,
    IN p_nome VARCHAR(20),
    IN p_peso INT,
    IN p_preco INT,
    IN p_cor TEXT
) RETURNS INT AS $$
DECLARE
    v_item_id INT;
BEGIN
    -- create item.
    INSERT INTO item (tipo)
    VALUES ('Pergaminho')
    RETURNING id INTO v_item_id;

    -- create scroll.
    INSERT INTO pergaminho (id, cor, descricao, drop_inimigos_media, nome, peso, preco)
    VALUES (v_item_id, p_cor::TIPO_COR, p_descricao, p_drop_inimigos_media, p_nome, p_peso, p_preco);

    RETURN v_item_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `pocao`
CREATE OR REPLACE FUNCTION criar_pocao(
    IN p_descricao TEXT,
    IN p_drop_inimigos_media INT,
    IN p_nome VARCHAR(20),
    IN p_peso INT,
    IN p_preco INT
) RETURNS INT AS $$
DECLARE
    v_item_id INT;
BEGIN
    -- Criar o item da poção
    INSERT INTO item (tipo)
    VALUES ('Poção')
    RETURNING id INTO v_item_id;

    -- Criar a poção
    INSERT INTO pocao (id, descricao, drop_inimigos_media, nome, peso, preco)
    VALUES (v_item_id, p_descricao, p_drop_inimigos_media, p_nome, p_peso, p_preco);

    RETURN v_item_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `feitico_dano`
CREATE OR REPLACE FUNCTION criar_feitico_dano(
    IN nome TEXT,
    IN descricao TEXT ,
    IN elemento TEXT, -- ::TIPO_ELEMENTO,
    IN countdown INT,
    IN conhecimento_arcano_necessario INT,
    IN energia_arcana INT,
    IN dano_total INT
) RETURNS INT AS $$
DECLARE
    v_feitico_id INT;
BEGIN
    -- Criar o feitico
    INSERT INTO feitico (tipo)
    VALUES ('Dano')
    RETURNING id INTO v_feitico_id;

    -- Criar a feitico_dano
    INSERT INTO feitico_dano (
        id,
        dano_total,
        descricao,
        elemento,
        countdown,
        conhecimento_arcano_necessario,
        energia_arcana,
        nome
    )
    VALUES (
        v_feitico_id,
        dano_total,
        descricao,
        elemento::TIPO_ELEMENTO,
        countdown,
        conhecimento_arcano_necessario,
        energia_arcana,
        nome
    );

    RETURN v_feitico_id;
END;
$$ LANGUAGE plpgsql;


-- PostGreSQL: create `feitico_dano_area`
CREATE OR REPLACE FUNCTION criar_feitico_dano_area(
    IN nome TEXT,
    IN descricao TEXT,
    IN elemento TEXT, -- ::TIPO_ELEMENTO,
    IN countdown INT,
    IN conhecimento_arcano_necessario int,
    IN energia_arcana INT,
    IN dano INT,
    IN qtd_inimigos_afetados INT
) RETURNS INT AS $$
DECLARE
    v_feitico_id INT;
BEGIN
    -- Criar o feitico
    INSERT INTO feitico (tipo)
    VALUES ('Dano de área')
    RETURNING id INTO v_feitico_id;

    -- Criar a feitico_dano_area
    INSERT INTO feitico_dano_area(id, 
        dano, qtd_inimigos_afetados, 
        descricao, 
        elemento, 
        countdown, 
        conhecimento_arcano_necessario, 
        energia_arcana,
        nome
    )
    VALUES (v_feitico_id, 
        dano, 
        qtd_inimigos_afetados, 
        descricao, 
        elemento::TIPO_ELEMENTO, 
        countdown, 
        conhecimento_arcano_necessario, 
        energia_arcana,
        nome);

    RETURN v_feitico_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `feitico_cura`
CREATE OR REPLACE FUNCTION criar_feitico_cura(
    IN nome TEXT,
    IN descricao TEXT,
    IN elemento TIPO_ELEMENTO,
    IN countdown INT,
    IN conhecimento_arcano_necessario INT,
    IN energia_arcana INT,
    IN qtd_cura INT
) RETURNS INT AS $$
DECLARE
    v_feitico_id INT;
BEGIN
    -- Criar o feitico
    INSERT INTO feitico (tipo)
    VALUES ('Cura')
    RETURNING id INTO v_feitico_id;

    -- Criar a feitico_cura
    INSERT INTO feitico_cura (
        id,
        qtd_cura,
        descricao,
        elemento,
        countdown,
        conhecimento_arcano_necessario,
        energia_arcana,
        nome
    )
    VALUES (
        v_feitico_id,
        qtd_cura,
        descricao,
        elemento::TIPO_ELEMENTO,
        countdown,
        conhecimento_arcano_necessario,
        energia_arcana,
        nome
    );

    RETURN v_feitico_id;
END;
$$ LANGUAGE plpgsql;

-- PosGreSQL: create `atualizar_combate`
CREATE OR REPLACE FUNCTION atualizar_combate(
    IN p_personagem_id INT,
    IN p_inimigo_id INT,
    IN p_vida_personagem INT,
    IN p_vida_inimigo INT
) RETURNS INT AS $$
DECLARE
    v_personagem_id INT;
BEGIN
    -- Update character fields.
    UPDATE personagem
    SET vida = GREATEST(p_vida_personagem, 0)
    WHERE id = p_personagem_id;

    -- Update enemy fields.
    UPDATE inimigo_instancia
    SET vida = GREATEST(p_vida_inimigo, 0)
    WHERE id = p_inimigo_id;

    RETURN p_personagem_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `combate`
CREATE OR REPLACE FUNCTION finalizar_combate(
    IN p_id INT,
    IN p_xp INT,
    IN p_energia_arcana INT,
    IN p_dano_recebido INT, 
    IN p_dano_causado INT,
    IN ei_id INT
) RETURNS INT[] AS $$
DECLARE
    v_armazenamentos RECORD;
    list_items INT[];
BEGIN
    -- Update character fields.
    UPDATE personagem
    SET xp = LEAST(xp + p_xp, xp_total), 
        energia_arcana = LEAST(energia_arcana + p_energia_arcana, energia_arcana_maxima)
    WHERE id = p_id;

    -- To-do: if `xp` is equal to `xp_total`, increase `nivel` by 1 and set `xp` to 0, and update attributes.

    -- Get items that can be dropped from this enemy.
    SELECT
        a.item_id,
        a.quantidade,
        i.drop_inimigos_media
    INTO v_armazenamentos
    FROM armazenamento_inimigo AS ai
    JOIN armazenamento AS a ON ai.armazenamento_id = a.id
    JOIN item AS i ON a.item_id = i.id
    WHERE ai.inimigo_id = ei_id;

    -- If the record variable `v_armazenamentos` is null, return the variable `list_items`.
    IF v_armazenamentos IS NULL THEN
        RETURN list_items;
    END IF;

    -- Generate items that will be dropped.
    FOR i IN 1..v_armazenamentos.quantidade LOOP
        IF random() < 1 / v_armazenamentos.drop_inimigos_media THEN
            list_items := list_items || v_armazenamentos.item_id;
        END IF;
    END LOOP;

    -- Add to the table `combate`: inimigo_instancia_id, personagem_id, dano_cauisad, dano_recebido.
    INSERT INTO combate (inimigo_instancia_id, personagem_id, dano_causado, dano_recebido)
    VALUES (ei_id, p_id, p_dano_causado, p_dano_recebido);

    RETURN list_items;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `aprender_feitico`
CREATE OR REPLACE FUNCTION aprender_feitico(
    IN p_personagem_id INT,
    IN p_feitico_id INT
) RETURNS INT AS $$
DECLARE
    v_inventario_id INT;
    v_requisito_id INT;
    v_pre_requisito_aprendido BOOLEAN;
    v_possui_feitico_atual BOOLEAN;
    v_conhecimento_arcano_suficiente BOOLEAN;
BEGIN
    SELECT id
    INTO v_inventario_id
    FROM inventario
    WHERE personagem_id = p_personagem_id;

    SELECT de_id
    INTO v_requisito_id
    FROM feitico_requerimento
    WHERE para_id = p_feitico_id;

    -- Verifica se já possui o feitiço pré-requisito
    SELECT EXISTS (
        SELECT 1
        FROM feitico_aprendido
        WHERE inventario_id = v_inventario_id
          AND feitico_id = v_requisito_id
    ) INTO v_pre_requisito_aprendido;

    -- Verifica se já possui o feitiço atual
    SELECT EXISTS (
        SELECT 1
        FROM feitico_aprendido
        WHERE inventario_id = v_inventario_id
          AND feitico_id = p_feitico_id
    ) INTO v_possui_feitico_atual;

    -- Verifica se possui conhecimento arcano suficiente para o feitiço
    SELECT (p.conhecimento_arcano >= f.conhecimento_arcano_necessario)
    INTO v_conhecimento_arcano_suficiente
    FROM personagem p
    JOIN feitico f ON f.id = p_feitico_id
    WHERE p.id = p_personagem_id;

    -- Só aprende o feitiço se ainda não tiver, já possuir o pré-requisito e tiver conhecimento arcano
    IF NOT v_possui_feitico_atual
       AND v_pre_requisito_aprendido
       AND v_conhecimento_arcano_suficiente THEN
        INSERT INTO feitico_aprendido(inventario_id, feitico_id)
        VALUES (v_inventario_id, p_feitico_id);
    END IF;

    RETURN p_personagem_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `criar_transacao`
CREATE OR REPLACE FUNCTION criar_transacao(
    IN p_mercador_id INT,
    IN p_personagem_id INT,
    IN p_item_id INT
) RETURNS INT AS $$
DECLARE
    v_inventario_id INT;
    v_transacao_id INT;
BEGIN
    -- Select inventario personagem
    SELECT id
    INTO v_inventario_id
    FROM inventario
    WHERE personagem_id = p_personagem_id;

    -- Criar instancia de Item
    INSERT INTO item_instancia (item_id, inventario_id)
    VALUES (p_item_id, v_inventario_id);

    -- Cria transacao
    INSERT INTO transacao (mercador_id, personagem_id, item_id)
    VALUES (p_mercador_id, p_personagem_id, p_item_id)
    RETURNING id INTO v_transacao_id;

    RETURN v_transacao_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `create_instance_quest`
CREATE OR REPLACE FUNCTION create_new_instance_quest(
    IN p_quest_id INT,
    IN p_personagem_id INT,
    IN p_regiao_nome VARCHAR(50)
) RETURNS INT AS $$
DECLARE
    v_quest_instancia_id INT;
BEGIN

    -- Check if a quest with the same id and personagem_id already exists.
    IF EXISTS (
        SELECT 1
        FROM quest_instancia
        WHERE quest_id = p_quest_id AND personagem_id = p_personagem_id
    ) THEN
        RAISE EXCEPTION 'Quest instance already exists for this character and quest.';
    END IF;
    
    INSERT INTO quest_instancia (quest_id, personagem_id, completed)
    VALUES (p_quest_id, p_personagem_id, FALSE)
    RETURNING id INTO v_quest_instancia_id;

    -- Atualiza a situação das sub-regiões da região passada como argumento para "Passável"
    UPDATE sub_regiao_conexao
    SET situacao = 'Passável'
    WHERE sub_regiao_2 IN (
        SELECT id FROM sub_regiao WHERE regiao_id = (
            SELECT id FROM regiao WHERE nome = p_regiao_nome
        )
    );

    RETURN v_quest_instancia_id;
END;
$$ LANGUAGE plpgsql;

-- Remove potion effects and return potion IDs.
CREATE OR REPLACE FUNCTION end_combat(
    IN p_personagem_id INT,
    IN enemies_id INT[]
) RETURNS INT[] AS $$
DECLARE
    v_potions_id INT[];
    item_rec INT[];
    v_dropped_items_id INT[];
    enemy_id INT;
    potion_id INT;
BEGIN
    -- Get potion IDs that were marked as used.
    SELECT ARRAY(
        SELECT item_id
        FROM item_instancia
        WHERE usado = TRUE
          AND mochila_id IN (
            SELECT id FROM inventario WHERE personagem_id = p_personagem_id
        )
    ) INTO v_potions_id;

    -- If v_potions_id is empty, return.
    IF v_potions_id IS NULL THEN
        RETURN v_potions_id;
    END IF;

    -- Loop through each potion's id in v_potions_id and remove their effect from personagem.
    FOREACH potion_id IN ARRAY v_potions_id LOOP
        UPDATE personagem
        SET
            inteligencia = inteligencia / (
                SELECT inteligencia 
                FROM efeito 
                WHERE id IN (
                    SELECT efeito_id 
                    FROM pocao_efeito 
                    WHERE pocao_id = potion_id
                )
            ),
            vida_maxima = vida_maxima / (
                SELECT vida 
                FROM efeito 
                WHERE id IN (
                    SELECT efeito_id 
                    FROM pocao_efeito 
                    WHERE pocao_id = potion_id
                )
            ),
            energia_arcana_maxima = energia_arcana_maxima / (
                SELECT energia_arcana 
                FROM efeito 
                WHERE id IN (
                    SELECT efeito_id 
                    FROM pocao_efeito 
                    WHERE pocao_id = potion_id
                )
            )
        WHERE id = p_personagem_id;
    END LOOP;

    DELETE FROM item_instancia
    WHERE usado = TRUE
      AND mochila_id IN (
        SELECT id FROM inventario WHERE personagem_id = p_personagem_id
    );

    v_dropped_items_id := '{}';

    -- For each enemy, append all of its drop items to v_dropped_items_id.
    FOREACH enemy_id IN ARRAY enemies_id LOOP
        FOR item_rec IN
            SELECT
                a.item_id,
                a.quantidade,
                COALESCE(p.drop_inimigos_media, ac.drop_inimigos_media, po.drop_inimigos_media)
            FROM armazenamento_inimigo ai
            JOIN armazenamento a ON ai.armazenamento_id = a.id
            JOIN item i ON a.item_id = i.id
            JOIN acessorio ac ON i.id = ac.id
            JOIN pergaminho p ON i.id = p.id
            JOIN pocao po ON i.id = po.id
            WHERE ai.inimigo_id = enemy_id
        LOOP
            FOR counter IN 1..item_rec.quantidade LOOP
                IF random() < 1.0 / item_rec.drop_inimigos_media THEN
                    v_dropped_items_id := array_append(v_dropped_items_id, item_rec.item_id);
                END IF;
            END LOOP;
        END LOOP;
    END LOOP;

    RETURN v_dropped_items_id;
END;
$$ LANGUAGE plpgsql;
```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 03/02/2025 | Criação   | Grupo |
| `2.0`  | 10/02/2025 | Atualização   | Grupo |