from utils import debug, error
from database.Database import Database

from database.data.item.acessory import bracelet, buckle, cane, cloack, collar, gloves, hat, ring, pants, socks, boots, key
from database.data.npc.enemy import enemies, enemies_instances
from database.data.npc.citizen import citizens, merchants, questers
from database.data.storage import quest, storage, enemie_storage, sub_regiao_storage
from database.data.map import regions as r, sub_regions as sr, sub_regions_connections as src
from database.data.item.scroll import area_damage, cure, damage, scroll, writted_scroll, requirements
from database.data.item import effects, potions, potion_effect

def populate_database(db: Database):
    
    try:    
        # Map.
        r.regions(db)
        sr.sub_regions(db)
        src.sub_regions_connections(db)
        
        # Enemies.
        enemies.default_enemies(db)
        enemies_instances.create_enemy_instances(db)
#
        # Citizens.
        citizens.citizens(db)
        merchants.merchants(db)
        questers.questers(db)
        
        #effects
        effects.effects(db)

        # Items: precisa do procedure `create_acessorio` para funcionar.
        item_total = 0
        item_total += boots.boots(db)
        item_total += bracelet.bracelets(db)
        item_total += buckle.buckle(db)
        item_total += cane.cane(db)
        item_total += cloack.cloack(db)
        item_total += collar.collars(db)
        item_total += gloves.gloves(db)
        item_total += hat.hats(db)
        item_total += pants.pants(db)
        item_total += ring.rings(db)
        item_total += socks.socks(db)
        item_total += key.keys(db)

        # Spells:
        spells_id_start = 0
        spells_id_start += area_damage.area_spells(db)
        spells_id_start += cure.cure_spells(db)
        spells_id_start += damage.damage_spells(db)
        
        scrolls_id_start = item_total
        item_total += scroll.scrolls(db)
        
        requirements.insert_spell_requirements(db)
        
        writted_scroll.writted_scrolls(db, scrolls_id_start)
        
        storage.populate_storage(db)
        #enemie_storage.enemie_storage(db)
        sub_regiao_storage.default_subregion_itens(db)
        quest.quests(db)
#
        #potions
        potions.potions(db)
        potion_effect.potion_effect(db)


        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating the database: {e}")
        