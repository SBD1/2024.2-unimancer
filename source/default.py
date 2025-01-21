from database import Database
from utils import debug
from defaults.regions import regions
from defaults.sub_regions import sub_regions
from defaults.sub_regions_connections import sub_regions_connections
from defaults.items import rings

def populate_database(db: Database):
    try:
        # Map.
        regions()
        sub_regions()
        sub_regions_connections()
        
        # Items.
        
        # -- Precisa do procedure `create_acessorio` para funcionar.
        # -- rings()

        db.conn.commit()

    except Exception as e:
        db.conn.rollback()
        debug(f"default: Error occurred while adding regions and subregions: {e}")
