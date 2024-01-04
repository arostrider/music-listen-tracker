from pathlib import Path

from flask import Flask, request

from music_data_base import MusicDataBase


def create_app(db_file: str | Path):
    app = Flask(__name__)
    db_file = db_file

    @app.route('/')
    def index():
        return 'Hello from server!'

    @app.route('/add-tracks', methods=['POST'])
    def add_tracks():
        print("Adding tracks...")
        data = request.get_json()

        with MusicDataBase(db_file) as db:
            db.create_new_table(data['table_name'])

            if tracks := data.get('tracks'):
                db.insert_into_table(table=data['table_name'],
                                     tracks=[[track['title'], track['format']] for track in tracks])

            db.commit()
        print(f"Tracks added: {data}")
        return "", 204

    return app


if __name__ == '__main__':
    app = create_app(db_file='test.db')
    app.run(debug=True)
