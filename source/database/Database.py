from colorama import Fore, Style
from utils import debug
import psycopg2

class Database:
    
    def __init__(self, host, db, user, password):
        
        self.conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=password
        )
        
        if not self.conn.status:
            debug("Database: Connection failed with server.")
            exit(1)

        self.cur = self.conn.cursor()

    def delete_tables(self) -> None:
        try:
            # Reset completely the database, stopping all connections and transactions.
            self.cur.execute("ROLLBACK;")
            self.cur.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'rpg' AND pid <> pg_backend_pid();")
            self.conn.commit()

            # Delete all tables, types and procedures.
            self.cur.execute("DROP SCHEMA public CASCADE ; CREATE SCHEMA public;")
            self.conn.commit()

        except Exception as e:
            debug(f"database: Error deleting tables: {e}")

        debug("database: deleted all tables.")

    # Execute a SQL file in the database.
    def execute_file(self, path: str) -> None:
        debug(f"database: exeuting file {Style.BRIGHT + path + Style.NORMAL}")
        with open(path, encoding='utf8', mode='r') as file:
            sql = file.read()
            self.cur.execute(sql)
            self.conn.commit()