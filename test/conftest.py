import pytest

from client import Client
from data_base import DataBase


@pytest.fixture
def client():
    client = Client(DataBase(":memory:"))
    client.load_dir_tree_to_db(dir_="D:\\Marko muzika\\Neptune Disc", table_name="neptune")
    yield client
    client.db.con.close()
