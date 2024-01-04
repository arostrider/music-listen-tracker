import os

import pytest


class NewTestTrack:
    title = "new_test_track"
    format = "mp3"


@pytest.mark.parametrize("env", ["local", "remote"], indirect=True)
class TestClient:
    def test_load_dir_to_db(self, client, test_data, db):
        client.load_dir_to_db(dir_=test_data.tracks_dir, table_name=test_data.table_name)

        res = db.cur.execute("SELECT * FROM neptune")
        assert res.fetchall() == list(test_data.table_content)

    def test_reloading_dir_to_db_does_not_change_anything_if_dir_content_is_same(self, client, test_data, db):
        client.load_dir_to_db(dir_=test_data.tracks_dir, table_name=test_data.table_name)

        res = db.cur.execute("SELECT * FROM neptune")
        assert res.fetchall() == list(test_data.table_content)

    @pytest.fixture(scope="class")
    def add_temp_file_to_dir(self, test_data):
        file_path = f"{test_data.tracks_dir}\\{NewTestTrack.title}.{NewTestTrack.format}"
        with open(file_path, 'w'):
            pass
        yield
        os.remove(file_path)

    def test_load_dir_to_db_adds_new_entry_to_db_if_there_is_new_file_in_dir(self,
                                                                             client,
                                                                             test_data,
                                                                             add_temp_file_to_dir,
                                                                             db):
        client.load_dir_to_db(dir_=test_data.tracks_dir, table_name=test_data.table_name)

        res = db.cur.execute("SELECT * FROM neptune")
        rows = res.fetchall()

        assert all(i in rows for i in test_data.table_content), \
            f"Table list of rows from test_data is not a sublist of current rows list."

        new_entry = rows[-1]
        id_, title, format_, count = new_entry
        assert id_ > max([row[0] for row in test_data.table_content])
        assert title == NewTestTrack.title
        assert format_ == NewTestTrack.format
        assert count == 0
