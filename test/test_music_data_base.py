import pytest


class TestMusicDataBase:

    @pytest.fixture(scope="class", autouse=True)
    def create_new_table(self, db):
        db.create_new_table("test_table")
        db.insert_into_table("test_table",
                             [["foo", "mp3"], ["bar", "mp3"]])
        db.commit()

    def test_table_name(self, db):
        res = db.cur.execute("SELECT name FROM sqlite_master")
        assert res.fetchone() == ("test_table",)

    def test_table_columns(self, db):
        res = db.cur.execute("PRAGMA table_info(test_table)")
        assert res.fetchall() == [(0, 'id', 'INTEGER', 0, None, 1),
                                  (1, 'title', '', 0, None, 0),
                                  (2, 'format', '', 0, None, 0),
                                  (3, 'count', 'INTEGER', 0, None, 0)]

    def test_table_rows(self, db):
        res = db.cur.execute("SELECT * FROM test_table")
        assert res.fetchall() == [(1, 'foo', 'mp3', 0),
                                  (2, 'bar', 'mp3', 0)]

    def test_increase_track_play_count(self, db):
        db.increase_track_play_count("test_table", "foo")
        db.commit()

        res = db.cur.execute("SELECT count FROM test_table WHERE title='foo'")
        assert res.fetchone() == (1,)
