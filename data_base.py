import sqlite3
from pathlib import Path


class DataBase:
    def __init__(self, file: str | Path):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
