-- PostGreSQL:
-- `incrementar_peso_acessorio`:
-- when character gets a new `acessorio`, it will increment the `peso` of the `mochila`, and if it surpasses `peso_total`, do not allow.
-- PostGreSQL:
CREATE OR REPLACE FUNCTION incrementar_peso_acessorio()
RETURNS TRIGGER AS $$
DECLARE
    item_peso INT;
BEGIN
    -- get item weight
    SELECT COALESCE(a.peso, po.peso, pe.peso)
    FROM acessorio a
    LEFT JOIN pocao po ON po.id = NEW.item_id
    LEFT JOIN pergaminho pe ON pe.id = NEW.item_id
    INTO item_peso;

    UPDATE mochila
    SET peso = peso + item_peso
    WHERE id = NEW.mochila_id;
    
    IF (SELECT peso FROM mochila WHERE id = NEW.mochila_id) > (SELECT peso_total FROM mochila WHERE id = NEW.mochila_id) THEN
        RAISE EXCEPTION 'Peso total da mochila excedido';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Link the trigger `incrementar_peso_acessorio` to the table `item_instancia` when a new row is created.
CREATE TRIGGER trigger_incrementar_peso_acessorio
AFTER INSERT ON item_instancia
FOR EACH ROW
EXECUTE FUNCTION incrementar_peso_acessorio();

-- PostGreSQL:
-- `decrementar_peso_acessorio`:
-- when one `item_instancia` is deleted, it will decrement the `peso` of the `mochila`.
CREATE OR REPLACE FUNCTION decrementar_peso_acessorio()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE mochila
    SET peso = peso - OLD.peso
    WHERE id = OLD.inventario_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL:
-- When a quest_instancia is created, check if the character has an acessory that is in the armazenamento of the quest.
CREATE OR REPLACE FUNCTION check_acessory()
RETURNS TRIGGER AS $$
BEGIN 
    -- Check if the character already has the item from the quest's armazenamento
    IF EXISTS (SELECT 1 
               FROM item_instancia 
               WHERE item_id IN (SELECT item_id 
                                 FROM armazenamento 
                                 WHERE quest_id = NEW.quest_id) 
               AND inventario_id = NEW.inventario_id) THEN
        RAISE EXCEPTION 'Personagem already has the item';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- PostGreSQL
-- When the character reaches maximum xp, increase the level and total xp
CREATE OR REPLACE FUNCTION update_level()
RETURNS TRIGGER AS $$
BEGIN
    WHILE NEW.xp >= NEW.xp_total LOOP
        NEW.nivel := NEW.nivel + 1;
        NEW.xp_total := NEW.xp_total + 100;
    END LOOP;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--CREATE TRIGGER trigger_atualizar_nivel
--BEFORE UPDATE ON personagem
--FOR EACH ROW
--WHEN (NEW.xp >= NEW.xp_total)
--EXECUTE FUNCTION atualizar_nivel();


-- PostGreSQL: Deletar instância de inimigo
-- CREATE OR REPLACE FUNCTION handle_enemy_death()
-- RETURNS TRIGGER AS $$
-- DECLARE
--     v_armazenatmento RECORD;
--     v_item_instacia_id INT;
-- BEGIN
--     -- verifica se o inimigo morreu
--     IF NEW.vida <= 0 THEN
--         DELETE FROM inimigo_instancia WHERE id = NEW.id;
-- 
--         -- atualiza xp do personagem
--         UPDATE personagem
--         SET xp = xp + NEW.xp
--         WHERE id = NEW.personagem_id;
-- 
--         -- insere itens do inimigo no inventário do personagem
--         FOR v_armazenamento IN
--             SELECT a.item_id, a.quantidade
--             FROM armazenamento a
--             WHERE a.inimigo_id = NEW.inimigo_id
--         LOOP
--             INSERT INTO item_instancia (item_id, inventario_id, quantidade)
--             VALUES (v_armazenamento.item_id, NEW.inventario_id, v_armazenamento.quantidade);
--             RETURNING id INTO v_item_instancia_id;
--         
--             -- atualiza quantidade de itens no inventário
--             UPDATE armazenamento
--             SET quantidade = quantidade - v_armazenamento.quantidade
--             WHERE item_id = v_armazenamento.item_id AND inimigo_id = NEW.inimigo_id;
--         END LOOP;
--     END IF;
-- 
--     RETURN NEW;;
-- END;
-- $$ LANGUAGE plpgsql;

-- Criar trigger para deletar instância de inimigo
-- CREATE TRIGGER trigger_handle_enemy_death
-- AFTER UPDATE ON inimigo_instancia
-- FOR EACH ROW
-- WHEN (NEW.vida <= 0)
-- EXECUTE FUNCTION handle_enemy_death();

-- PostGreSQL
-- Buff character of the same element in the region
CREATE OR REPLACE FUNCTION aplicar_buff()
RETURNS TRIGGER AS $$
DECLARE
    regiao_elemento TIPO_ELEMENTO;
BEGIN
    SELECT r.elemento INTO regiao_elemento
    FROM sub_regiao sr
    JOIN regiao r ON sr.regiao_id = r.id
    WHERE sr.id = NEW.sub_regiao_id;
    
    IF regiao_elemento = NEW.elemento THEN
        NEW.vida_maxima := CEIL(NEW.vida_maxima * 1.2);
        NEW.energia_arcana_maxima := CEIL(NEW.energia_arcana_maxima * 1.1);
    ELSE
        NEW.vida_maxima := OLD.vida_maxima;
        NEW.energia_arcana_maxima := OLD.energia_arcana_maxima;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_aplicar_buff
BEFORE UPDATE ON personagem
FOR EACH ROW
WHEN (NEW.sub_regiao_id IS DISTINCT FROM OLD.sub_regiao_id)
EXECUTE FUNCTION aplicar_buff();

-- PostGreSQL
-- When adding transaction, create item instance in merchant storage
CREATE OR REPLACE FUNCTION criar_instancia_item()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica se a combinação mercador_id e armazenamento_id já existe
    IF EXISTS (SELECT 1 FROM armazenamento_mercador WHERE mercador_id = NEW.mercador_id AND armazenamento_id = NEW.item_id) THEN
        -- Atualiza a quantidade no armazenamento
        UPDATE armazenamento
        SET quantidade = quantidade + 1
        WHERE id = NEW.item_id;
    ELSE
        -- Insere no armazenamento do mercador
        INSERT INTO armazenamento_mercador (mercador_id, armazenamento_id)
        VALUES (NEW.mercador_id, NEW.item_id);
        
        -- Inicializa a quantidade no armazenamento
        UPDATE armazenamento
        SET quantidade = 1
        WHERE id = NEW.item_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_criar_instancia_item
AFTER INSERT ON transacao
FOR EACH ROW
EXECUTE FUNCTION criar_instancia_item();

CREATE OR REPLACE FUNCTION check_conclusion_quest()
RETURNS TRIGGER AS $$
DECLARE
    v_inimigos_restantes INT;
    v_personagem_id INT;  -- Variable to store the personagem_id
BEGIN
    -- Count how many enemies are still alive in the quest subregion
    SELECT COUNT(*)
    INTO v_inimigos_restantes
    FROM inimigo_instancia
    WHERE sub_regiao_id = NEW.sub_regiao_id AND vida > 0;

    -- If there are no enemies remaining, mark the quest as completed
    IF v_inimigos_restantes = 0 THEN
        -- Mark the quest as completed
        UPDATE quest_instancia
        SET completed = TRUE
        WHERE sub_regiao_id = NEW.sub_regiao_id;

        -- Retrieve the personagem_id associated with the quest
        SELECT personagem_id
        INTO v_personagem_id
        FROM quest_instancia
        where completed = TRUE;

        -- Update character coins
        UPDATE personagem
        SET moedas = moedas + 100
        WHERE id = v_personagem_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_check_conclusion_quest
AFTER UPDATE ON inimigo_instancia
FOR EACH ROW
WHEN (NEW.vida <= 0)
EXECUTE FUNCTION check_conclusion_quest();

-- Potion:
--  When an "instance of item" that is an "item" of type "potion" is marked as used:
--  Update character's fields multiplying by each potion's effect field multiplier.
--CREATE OR REPLACE FUNCTION use_potion()
--RETURNS TRIGGER AS $$
--DECLARE
--    v_inimigos_restantes INT;
--BEGIN
--    -- Count how many enemies are still alive in the quest subregion
--    SELECT COUNT(*)
--    INTO v_inimigos_restantes
--    FROM inimigo_instancia
--    WHERE sub_regiao_id = OLD.sub_regiao_id AND vida > 0;
--
--    -- If there are no enemies remaining, mark the quest as completed
--    IF v_inimigos_restantes = 0 THEN
--        UPDATE quest_instancia
--        SET completed = TRUE;
--    END IF;
--
--    -- Update character coins
--    UPDATE personagem
--    SET moedas = moedas + 100
--    WHERE id = NEW.personagem_id;
--
--    -- Give to character the quest armazenamento items
--    
--
--    RETURN NEW;
--END;
--$$ LANGUAGE plpgsql;
--
--

--
