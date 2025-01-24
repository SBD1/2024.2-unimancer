-- PostGreSQL: create trigger when creating a new row at the table `quest`, it will increment the number of quests of the `quester`.
CREATE OR REPLACE FUNCTION incrementar_num_quests()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE quester
    SET num_quests = num_quests + 1
    WHERE id = NEW.quester_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

