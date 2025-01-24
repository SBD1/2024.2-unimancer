-- To-do: see if we can add NOT NULL to some of these arguments.

-- PostGreSQL: create `civil` linking to `npc`
CREATE OR REPLACE FUNCTION criar_civil(
    IN nome VARCHAR(100),
    IN sub_regiao_id INT,
    IN descricao TEXT,
    IN tipo TEXT
) RETURNS INT AS $$
DECLARE 
    npc_id INT;
BEGIN
    INSERT INTO npc (nome, tipo)
    VALUES (nome, 'Civil')
    RETURNING id INTO npc_id;

    INSERT INTO civil (
        id,
        sub_regiao_id,
        descricao,
        tipo
    )
    VALUES (
        id,
        sub_regiao,
        descricao,
        tipo
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
        dialogo,
        num_quests
    )
    VALUES (
        npc_id,
        dialogo,
        0
    );

    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `acessorio`
CREATE OR REPLACE FUNCTION criar_acessorio(
  IN nome VARCHAR(20),
  IN descricao TEXT,
  IN chance_drop INT,
  IN peso INT,
  IN preco INT,
  IN tipo TIPO_ACESSORIO
)
RETURNS INT AS $$
DECLARE
     v_item_id INT;
     v_acessorio_id INT;
BEGIN
     -- Add `acessorio` in `item` table
     INSERT INTO item (tipo, descricao, chance_drop, nome, peso, preco)
     VALUES ('Acessório', descricao, chance_drop, nome, peso, preco)
     RETURNING id INTO v_item_id;

     -- Add at `acessorio` table
     INSERT INTO acessorio (id, tipo)
     VALUES (v_item_id, tipo)
     RETURNING id INTO v_acessorio_id;
 
     RETURN v_acessorio_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `mercador` linking to `npc`
CREATE OR REPLACE FUNCTION criar_mercador(
    IN nome VARCHAR(100),
    IN sub_regiao_id INT,
    IN descricao TEXT,
    IN armazenamento_id INT,
    IN dialogo TEXT
) RETURNS INT AS $$
DECLARE
    npc_id INT;
BEGIN
    npc_id = criar_civil(nome, sub_regiao_id, descricao, 'Mercador');

    INSERT INTO mercador (
        id,
        armazenamento_id,
        dialogo
    )
    VALUES (
        npc_id,
        armazenamento_id,
        dialogo
    );

    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;


-- PostGreSQL: create enemy linking to npc.
CREATE OR REPLACE FUNCTION criar_inimigo(
    IN nome VARCHAR(100),
    IN armazenamento_id INT,
    IN descricao TEXT,
    IN elemento TEXT,
    IN vida_maxima INT,
    IN xp_obtido INT,
    IN inteligencia INT,
    IN moedas_obtidas INT,
    IN conhecimento_arcano INT,
    IN energia_arcana_maxima INT
) RETURNS INT AS $$
DECLARE 
    npc_id INT;
BEGIN
    INSERT INTO npc (nome, tipo)
    VALUES (nome, 'Inimigo')
    RETURNING id INTO npc_id;

    INSERT INTO inimigo (
        id,
        armazenamento_id,
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
        armazenamento_id,
        descricao,
        elemento::TIPO_ELEMENTO,
        vida_maxima,
        xp_obtido,
        inteligencia,
        moedas_obtidas,
        conhecimento_arcano,
        energia_arcana_maxima,
        NULL
    );
    RETURN npc_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `personagem`
CREATE OR REPLACE FUNCTION criar_personagem(
    IN p_sub_regiao_id INT,
    IN p_nome VARCHAR(20),
    IN p_elemento TEXT,
    IN p_conhecimento_arcano INT,
    IN p_vida INT,
    IN p_vida_maxima INT,
    IN p_xp INT,
    IN p_xp_total INT,
    IN p_energia_arcana INT,
    IN p_energia_arcana_maxima INT,
    IN p_inteligencia INT,
    IN p_moedas INT,
    IN p_nivel INT
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
        p_sub_regiao_id,
        p_nome,
        p_elemento::TIPO_ELEMENTO,
        p_conhecimento_arcano,
        p_vida,
        p_vida_maxima,
        p_xp,
        p_xp_total,
        p_energia_arcana,
        p_energia_arcana_maxima,
        p_inteligencia,
        p_moedas,
        p_nivel
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

-- PostGreSQL: create `pocao`
CREATE OR REPLACE FUNCTION criar_pocao(
    IN p_descricao TEXT,
    IN p_chance_drop INT,
    IN p_nome VARCHAR(20),
    IN p_peso INT,
    IN p_preco INT,
    IN p_turnos INT
) RETURNS INT AS $$
DECLARE
    v_item_id INT;
BEGIN
    -- Criar o item da poção
    INSERT INTO item (tipo, descricao, chance_drop, nome, peso, preco)
    VALUES ('Poção', p_descricao, p_chance_drop, p_nome, p_peso, p_preco)
    RETURNING id INTO v_item_id;

    -- Criar a poção
    INSERT INTO pocao (id, turnos, usado)
    VALUES (v_item_id, p_turnos, FALSE);

    RETURN v_item_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `feitico_dano`
CREATE OR REPLACE FUNCTION criar_feitico_dano(
    IN descricao TEXT ,
    IN elemento TEXT, -- ::TIPO_ELEMENTO,
    IN countdown INT,
    IN conhecimento_arcano_necessario,
    IN energia_arcana INT,
    IN dano_total INT
) RETURNS INT AS $$
DECLARE
    v_feitico_id INT;
BEGIN
    -- Criar o feitico
    INSERT INTO feitico (descricao, elemento, countdown, conhecimento_arcano_necessario, energia_arcana, tipo)
    VALUES (descricao, elemento::TIPO_ELEMENTO, countdown, conhecimento_arcano_necessario, energia_arcana, 'Dano')
    RETURNING id INTO v_feitico_id;

    -- Criar a feitico_dano
    INSERT INTO feitico_dano (id, dano_total)
    VALUES (v_feitico_id, dano_total);

    RETURN v_feitico_id;
END;
$$ LANGUAGE plpgsql;


-- PostGreSQL: create `feitico_dano_area`
CREATE OR REPLACE FUNCTION criar_feitico_dano_area(
    IN descricao TEXT ,
    IN elemento TEXT, -- ::TIPO_ELEMENTO,
    IN countdown INT,
    IN conhecimento_arcano_necessario,
    IN energia_arcana INT,
    IN dano INT,
    IN qtd_inimigos_afetados INT
) RETURNS INT AS $$
DECLARE
    v_feitico_id INT;
BEGIN
    -- Criar o feitico
    INSERT INTO feitico (descricao, elemento, countdown, conhecimento_arcano_necessario, energia_arcana, tipo)
    VALUES (descricao, elemento::TIPO_ELEMENTO, countdown, conhecimento_arcano_necessario, energia_arcana, 'Dano de área')
    RETURNING id INTO v_feitico_id;

    -- Criar a feitico_dano_area
    INSERT INTO feitico_dano_area (id, dano, qtd_inimigos_afetados)
    VALUES (v_feitico_id, dano, qtd_inimigos_afetados);

    RETURN v_feitico_id;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL: create `feitico_cura`
CREATE OR REPLACE FUNCTION criar_feitico_cura(
    IN descricao TEXT ,
    IN elemento TEXT, -- ::TIPO_ELEMENTO,
    IN countdown INT,
    IN conhecimento_arcano_necessario,
    IN energia_arcana INT,
    IN qtd_cura INT
) RETURNS INT AS $$
DECLARE
    v_feitico_id INT;
BEGIN
    -- Criar o feitico
    INSERT INTO feitico (descricao, elemento, countdown, conhecimento_arcano_necessario, energia_arcana, tipo)
    VALUES (descricao, elemento::TIPO_ELEMENTO, countdown, conhecimento_arcano_necessario, energia_arcana, 'Cura')
    RETURNING id INTO v_feitico_id;

    -- Criar a feitico_cura
    INSERT INTO feitico_da (id, dano_total)
    VALUES (v_feitico_id, dano_total);

    RETURN v_feitico_id;
END;
$$ LANGUAGE plpgsql;