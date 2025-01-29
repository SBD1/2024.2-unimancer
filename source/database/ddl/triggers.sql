-- PostGreSQL:
-- `incrementar_peso_acessorio`:
-- when character gets a new `acessorio`, it will increment the `peso` of the `mochila`, and if it surpasses `peso_total`, do not allow.
-- PostGreSQL:
CREATE OR REPLACE FUNCTION incrementar_peso_acessorio()
RETURNS TRIGGER AS $$
BEGIN
    -- search weight in table 'item' with 'item_id'
    DECLARE
        item_peso NUMERIC;
    BEGIN
        -- get item weight
        SELECT peso INTO item_peso
        FROM item
        WHERE id = NEW.item_id;

        UPDATE mochila
        SET peso = peso + item_peso
        WHERE id = NEW.inventario_id;

        IF (SELECT peso FROM mochila WHERE id = NEW.inventario_id) > (SELECT peso_total FROM mochila WHERE id = NEW.inventario_id) THEN
            RAISE EXCEPTION 'Peso total da mochila excedido';
        END IF;

        RETURN NEW;
    END;
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