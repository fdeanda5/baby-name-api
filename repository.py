from database import Database
from models import BabyNameRecord


class BabyNameRepository:
    def __init__(self):
        self.db = Database()
        self.db.initialize()

    def insert(self, record: BabyNameRecord):
        with self.db.connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO baby_names VALUES (?, ?, ?)",
                (record.name, record.year, record.count)
            )

    def find_by_name(self, name: str):
        with self.db.connect() as conn:
            cur = conn.execute(
                "SELECT year, count FROM baby_names WHERE name = ?",
                (name.capitalize(),)
            )
            return cur.fetchall()

    def update(self, name: str, year: int, count: int):
        with self.db.connect() as conn:
            conn.execute(
                "UPDATE baby_names SET count = ? WHERE name = ? AND year = ?",
                (count, name.capitalize(), year)
            )

    def delete(self, name: str, year: int):
        with self.db.connect() as conn:
            conn.execute(
                "DELETE FROM baby_names WHERE name = ? AND year = ?",
                (name.capitalize(), year)
            )
