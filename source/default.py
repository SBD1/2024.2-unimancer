from database import Database
from utils import debug

# Map:
from defaults.regions import regions
from defaults.sub_regions import sub_regions
from defaults.sub_regions_connections import sub_regions_connections
from defaults.enemies import default_enemies 
from defaults.enemies_instances import create_enemy_instances

# Acessories:
from defaults.acessories import rings
from defaults.acessories import hats

# Npcs:
from defaults.npcs.citizens import citizens
from defaults.npcs.merchants import merchants
from defaults.npcs.questers import questers

def populate_database(db: Database):
    try:
        # Map.
        regions(db)
        sub_regions(db)
        sub_regions_connections(db)
        default_enemies(db)
        create_enemy_instances(db)

        citizens(db)
        merchants(db)
        questers(db)
        
        # Items: precisa do procedure `create_acessorio` para funcionar.
        # -- rings()
        # -- hats()

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding regions and subregions: {e}")
