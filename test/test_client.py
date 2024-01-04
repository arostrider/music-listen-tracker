def test_load_dir_to_db(client, test_data):
    client.load_dir_to_db(dir_=test_data.tracks_dir, table_name=test_data.table_name)

    res = client.db.cur.execute("SELECT * FROM neptune")
    assert res.fetchall() == list(test_data.table_content)
