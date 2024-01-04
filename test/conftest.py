import pytest

from client import Client
from music_data_base import MusicDataBase

import pytest


@pytest.fixture(scope="class")
def db():
    return MusicDataBase(":memory:")


@pytest.fixture(scope="class")
def client(db):
    client = Client(db)
    yield client
    client.db.con.close()


class TestData:
    tracks_dir = "D:\\Marko muzika\\Neptune Disc"
    table_name = "neptune"
    table_content = (
        (1, 'Ash Is & Tape Hiss - Ash Is - Tape Hiss - ND001 - 01 Ash Is - Changing', 'mp3', 0),
        (2, 'Ash Is & Tape Hiss - Ash Is - Tape Hiss - ND001 - 02 Ash Is - EQZ', 'mp3', 0),
        (3, 'Ash Is & Tape Hiss - Ash Is - Tape Hiss - ND001 - 03 Tape Hiss - Fantasia 990', 'mp3', 0),
        (4, 'Ash Is & Tape Hiss - Ash Is - Tape Hiss - ND001 - 04 Tape Hiss - Oblivion', 'mp3', 0),
        (5, 'Neptune Discs - Astro - Cecil - ND004 - 01 Astro - Into Dust', 'mp3', 0),
        (6, 'Neptune Discs - Astro - Cecil - ND004 - 02 Astro - Lost', 'mp3', 0),
        (7, 'Neptune Discs - Astro - Cecil - ND004 - 03 Cecil - Arcadian', 'mp3', 0),
        (8, 'Neptune Discs - Astro - Cecil - ND004 - 04 Cecil - Chaser', 'mp3', 0),
        (9, 'Neptune Discs - ND007 Robert Cecil - Orbit EP - 01 Robert Cecil - This Time Around', 'mp3', 0),
        (10, 'Neptune Discs - ND007 Robert Cecil - Orbit EP - 02 Robert Cecil - Star', 'mp3', 0),
        (11, 'Neptune Discs - ND007 Robert Cecil - Orbit EP - 03 Robert Cecil - Erosion', 'mp3', 0),
        (12, 'Neptune Discs - ND007 Robert Cecil - Orbit EP - 04 Robert Cecil - Phase', 'mp3', 0),
        (13, 'Neptune Discs - ND008 Various Artists - Neptune Discs Vol 4. - 01 Featherstone - Amber', 'mp3', 0),
        (14, 'Neptune Discs - ND008 Various Artists - Neptune Discs Vol 4. - 02 Pentland Park - New Generation', 'mp3',
         0),
        (15, 'Neptune Discs - ND008 Various Artists - Neptune Discs Vol 4. - 03 Astro - Blaze', 'mp3', 0),
        (16, 'Neptune Discs - ND008 Various Artists - Neptune Discs Vol 4. - 04 Plastic GRN - Holding On', 'mp3', 0),
        (17, 'Neptune Discs - ND008 Various Artists - Neptune Discs Vol 4. - 05 Adam BFD - Ninety Six', 'mp3', 0)
    )


@pytest.fixture(scope="class")
def test_data():
    return TestData
