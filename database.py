import sqlite3

DB_PATH = "baby_names.db"


class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        with self.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS baby_names (
                    name TEXT,
                    year INTEGER,
                    count INTEGER,
                    PRIMARY KEY (name, year)
                )
            """)
