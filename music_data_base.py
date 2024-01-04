import sqlite3
from pathlib import Path


class MusicDataBase:
    def __init__(self, file: str | Path):
        self.file = file
        self.con = None
        self.cur = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Closing connection due to {exc_type}: {exc_value}")
        self.close()

    def connect(self):
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()

    def close(self):
        try:
            self.con.close()
        except AttributeError:
            print(f"Can not close connection: {self.con}")
        finally:
            self.con = None
            self.cur = None

    def commit(self):
        self.con.commit()

    def create_new_table(self, name: str):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {name} "
                         f"(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                         f"title TEXT UNIQUE, "
                         f"format TEXT, "
                         f"count INTEGER)")

    def insert_into_table(self, table: str, tracks: list[list[str, str]]):
        self.cur.executemany(f"INSERT OR IGNORE INTO {table} (title, format, count) VALUES(?, ?, 0)", tracks)

    def increase_track_play_count(self, table: str, track_title: str):
        self.cur.execute(f"UPDATE {table} SET count=count+1 WHERE title='{track_title}'")
