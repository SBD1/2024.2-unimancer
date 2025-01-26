from utils import debug, error
from database.Database import Database

import database.defaults.maps.regions as regions
import database.defaults.maps.sub_regions as sub_regions
import database.defaults.maps.sub_regions_connections as sub_regions_connections

import database.defaults.npcs.enemies.enemies as default_enemies 
import database.defaults.npcs.enemies.enemies_instances as create_enemy_instances

import database.defaults.npcs.citizens.citizens as citizens
import database.defaults.npcs.citizens.merchants as merchants
import database.defaults.npcs.citizens.questers as questers

import database.defaults.item.acessory.boots as boots
import database.defaults.item.acessory.rings as rings
import database.defaults.item.acessory.hats as hats

def populate_database(db: Database):
    try:
        # Map.
        regions(db)
        sub_regions(db)
        sub_regions_connections(db)
        
        # Enemies.
        default_enemies(db)
        create_enemy_instances(db)

        # Citizens.
        citizens(db)
        merchants(db)
        questers(db)
        
        # Items: precisa do procedure `create_acessorio` para funcionar.
        rings()
        hats()
        boots()

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while populating the database: {e}")
        