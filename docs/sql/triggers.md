# TRIGGERS

## Introdução

Stored Procedures são blocos de código SQL armazenados no banco de dados, permitindo a execução de várias instruções em uma única unidade. Elas melhoram o desempenho ao reduzir a comunicação entre a aplicação e o banco, além de oferecerem mais segurança ao restringir o acesso direto a tabelas. Outra vantagem é a manutenção simplificada, já que a lógica pode ser centralizada no banco de dados, facilitando atualizações sem a necessidade de alterar a aplicação. 

## Triggers

```sql
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
    
    IF EXISTS (SELECT 1 FROM armazenamento_mercador WHERE mercador_id = NEW.mercador_id AND armazenamento_id = NEW.item_id) THEN
        
        UPDATE armazenamento
        SET quantidade = quantidade + 1
        WHERE id = NEW.item_id;
    ELSE
        
        INSERT INTO armazenamento_mercador (mercador_id, armazenamento_id)
        VALUES (NEW.mercador_id, NEW.item_id);
        
        
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
        WHERE quest_id = (SELECT id FROM quest WHERE sub_regiao_id = NEW.sub_regiao_id);

        -- Retrieve the personagem_id associated with the quest
        SELECT personagem_id
        INTO v_personagem_id
        FROM quest_instancia
        WHERE quest_id = (SELECT quest_id FROM quest WHERE sub_regiao_id = NEW.sub_regiao_id);

        -- Update character coins
        UPDATE personagem
        SET moedas = moedas + 100, xp = xp + 2
        WHERE id = v_personagem_id;

        -- Give to character the quest armazenamento items
        INSERT INTO item_instancia (item_id, mochila_id, usado)
        SELECT a.item_id, m.id, FALSE
        FROM armazenamento a
        JOIN quest q ON q.armazenamento_id = a.id
        JOIN quest_instancia qi ON qi.quest_id = q.id AND qi.personagem_id = v_personagem_id
        JOIN inventario i ON i.personagem_id = v_personagem_id
        JOIN mochila m ON m.id = i.id
        WHERE q.sub_regiao_id = NEW.sub_regiao_id;

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
CREATE OR REPLACE FUNCTION use_potion()
RETURNS TRIGGER AS $$
DECLARE
   v_personagem_id INT;
BEGIN

    -- If not potion, return.
    IF NOT EXISTS (SELECT 1 FROM pocao WHERE id = NEW.item_id) THEN
        RETURN NEW;
    END IF;

    -- Get `´personagem_id` from the `item_instancia` table.
    SELECT
        inventario.personagem_id INTO v_personagem_id
    FROM item_instancia
        JOIN mochila ON mochila.id = item_instancia.mochila_id
        JOIN inventario ON inventario.id = mochila.id
    WHERE item_instancia.id = NEW.id;

    UPDATE personagem
    SET
        inteligencia = inteligencia * (SELECT inteligencia FROM efeito WHERE id IN (SELECT efeito_id FROM pocao_efeito WHERE pocao_id = NEW.item_id)),
        vida = vida * (SELECT vida FROM efeito WHERE id IN (SELECT efeito_id FROM pocao_efeito WHERE pocao_id = NEW.item_id)),
        vida_maxima = vida_maxima * (SELECT vida FROM efeito WHERE id IN (SELECT efeito_id FROM pocao_efeito WHERE pocao_id = NEW.item_id)),
        energia_arcana_maxima = energia_arcana_maxima * (SELECT energia_arcana FROM efeito WHERE id IN (SELECT efeito_id FROM pocao_efeito WHERE pocao_id = NEW.item_id)),
        energia_arcana = energia_arcana * (SELECT energia_arcana FROM efeito WHERE id IN (SELECT efeito_id FROM pocao_efeito WHERE pocao_id = NEW.item_id))
    WHERE id = v_personagem_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- After updating "item_instancia" column value "usado", execute "use_potion" function.
CREATE TRIGGER trigger_use_potion
AFTER UPDATE ON item_instancia
FOR EACH ROW
WHEN (NEW.usado = TRUE)
EXECUTE FUNCTION use_potion();
```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 03/02/2025 | Criação   | Grupo |
| `2.0`  | 10/02/2025 | Atualização   | Grupo |