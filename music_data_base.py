import sqlite3
from pathlib import Path


class MusicDataBase:
    def __init__(self, file: str | Path):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()

    def commit(self):
        self.con.commit()

    def create_new_table(self, name: str):
        self.cur.execute(f"CREATE TABLE {name}"
                         f"(id INTEGER PRIMARY KEY AUTOINCREMENT, title, format, count INTEGER)")

    def insert_into_table(self, table: str, tracks: list[list[str, str]]):
        self.cur.executemany(f"INSERT INTO {table} (title, format, count) VALUES(?, ?, 0)", tracks)

    def increase_track_play_count(self, table: str, track_title: str):
        self.cur.execute(f"UPDATE {table} SET count=count+1 WHERE title='{track_title}'")
