from database import Database
from utils import debug
from defaults.regions import regions
from defaults.sub_regions import sub_regions
from defaults.sub_regions_connections import sub_regions_connections
from defaults.acessories import rings
from defaults.acessories import hats
from defaults.enemies import default_enemies 

def populate_database(db: Database):
    try:
        # Map.
        regions(db)
        sub_regions(db)
        sub_regions_connections(db)
        default_enemies(db)

        # Items: precisa do procedure `create_acessorio` para funcionar.
        # -- rings()
        # -- hats()

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding regions and subregions: {e}")
