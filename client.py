import abc
import os
from pathlib import Path

import requests

from music_data_base import MusicDataBase


class Client(abc.ABC):

    @abc.abstractmethod
    def load_dir_to_db(self, dir_: str | Path, table_name: str):
        ...


class Local(Client):
    def __init__(self, db: MusicDataBase):
        self.db = db

    def load_dir_to_db(self, dir_: str | Path, table_name: str):
        tracks = [str(fpath).rsplit(".", 1) for fpath in os.listdir(dir_)]
        self.db.create_new_table(table_name)
        self.db.insert_into_table(table_name, tracks)
        self.db.commit()


class Remote(Client):
    def __init__(self, url: str):
        self.url = url

    def load_dir_to_db(self, dir_: str | Path, table_name: str):
        print("Load dir to db")
        tracks = [str(fpath).rsplit(".", 1) for fpath in os.listdir(dir_)]
        requests.post(url=f"{self.url}/add-tracks", data={"table_name": table_name,
                                                          "tracks": tracks})
