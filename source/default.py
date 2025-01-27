from database.defaults.item.acessory import bracelet, buckle, cane, cloack, collar, gloves, hat, ring, pants, socks, boots
from utils import debug, error
from database.Database import Database

from database.defaults.npc.enemy import enemies, enemies_instances

from database.defaults.npc.citizen import citizens, merchants, questers

from database.defaults.map import regions as r, sub_regions as sr, sub_regions_connections as src


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
        
        # Items: precisa do procedure `create_acessorio` para funcionar.
        boots.boots(db)
        bracelet.bracelets(db)
        buckle.buckle(db)
        cane.cane(db)
        cloack.cloack(db)
        collar.collars(db)
        gloves.gloves(db)
        hat.hats(db)
        pants.pants(db)
        ring.rings(db)
        socks.socks(db)

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating the database: {e}")
        