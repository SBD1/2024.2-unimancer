-- PostGreSQL: Create in the table `npc` first with (nome, tipo), then in the table `inimigo` linking the id to the table `npc` and adding the other attributes.

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

-- CREATE OR REPLACE PROCEDURE criar_personagem(
--     p_sub_regiao_id INT,
--     p_nome VARCHAR(20),
--     p_elemento TIPO_ELEMENTO,
--     p_conhecimento_arcano INT,
--     p_vida INT,
--     p_vida_maxima INT,
--     p_xp INT,
--     p_xp_total INT,
--     p_energia_arcana INT,
--     p_energia_arcana_maxima INT,
--     p_inteligencia INT,
--     p_moedas INT,
--     p_nivel INT
-- )
-- LANGUAGE plpgsql
-- AS $$
-- DECLARE
--     v_personagem_id INT;
--     v_inventario_mochila_id INT;
--     v_inventario_grimorio_id INT;
-- BEGIN
-- INSERT INTO personagem (
--         sub_regiao_id,
--         nome,
--         elemento,
--         conhecimento_arcano,
--         vida,
--         vida_maxima,
--         xp,
--         xp_total,
--         energia_arcana,
--         energia_arcana_maxima,
--         inteligencia,
--         moedas,
--         nivel
--     )
--     VALUES (
--         p_sub_regiao_id,
--         p_nome,
--         p_elemento,
--         p_conhecimento_arcano,
--         p_vida,
--         p_vida_maxima,
--         p_xp,
--         p_xp_total,
--         p_energia_arcana,
--         p_energia_arcana_maxima,
--         p_inteligencia,
--         p_moedas,
--         p_nivel
--     )
-- RETURNING id INTO v_personagem_id;
-- Criar o inventário do tipo Mochila
-- INSERT INTO inventario (personagem_id, tipo)
-- VALUES (v_personagem_id, 'Mochila')
-- RETURNING id INTO v_inventario_mochila_id;

-- INSERT INTO mochila (id, peso, peso_total)
-- VALUES (v_inventario_mochila_id, 0, 20);

 -- Criar o inventário do tipo Grimório
-- INSERT INTO inventario (personagem_id, tipo)
-- VALUES (v_personagem_id, 'Grimório')
-- RETURNING id INTO v_inventario_grimorio_id;

-- INSERT INTO grimorio (id, num_pag, num_pag_maximo)
-- VALUES (v_inventario_grimorio_id, 0, 5);

-- RETURN npc_id;
-- END;
-- $$;
