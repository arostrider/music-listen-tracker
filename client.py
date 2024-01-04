import os
from pathlib import Path

from data_base import DataBase


class Client:
    def __init__(self, db: DataBase):
        self.db = db

    def load_dir_tree_to_db(self, dir_: str | Path, table_name: str):
        tracks = [str(fpath).rsplit(".", 1) for fpath in os.listdir(dir_)]

        self.db.cur.execute(f"CREATE TABLE {table_name}"
                            f"(id INTEGER PRIMARY KEY AUTOINCREMENT, title, format, count INTEGER)")
        self.db.cur.executemany(f"INSERT INTO {table_name} (title, format, count) VALUES(?, ?, 0)", tracks)

        self.db.con.commit()

    def increase_play_count(self, table: str, track_title: str):
        self.db.cur.execute(f"UPDATE {table} SET count=count+1 WHERE title='{track_title}'")
