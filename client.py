import os
import sqlite3
from pathlib import Path

from music_data_base import MusicDataBase


class Client:
    def __init__(self, db: MusicDataBase):
        self.db = db

    def load_dir_to_db(self, dir_: str | Path, table_name: str):
        tracks = [str(fpath).rsplit(".", 1) for fpath in os.listdir(dir_)]

        try:
            self.db.create_new_table(table_name)
        except sqlite3.OperationalError:
            print(f"Table {table_name} already exists! Skipping table creation.")

        self.db.insert_into_table(table_name, tracks)
        self.db.commit()
