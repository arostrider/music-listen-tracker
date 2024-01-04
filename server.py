from flask import Flask, request, jsonify, Response
from music_data_base import MusicDataBase

app = Flask(__name__)

DB = 'db.db'


@app.route('/')
def index():
    return 'Hello from server!'


@app.route('/new-table', methods=['POST'])
def create_new_table():
    data = request.get_json()
    with MusicDataBase(DB) as db:
        db.create_new_table(data['table_name'])
        return "", 204


if __name__ == '__main__':
    app.run(debug=True)
