import flask
from flask import request, jsonify, abort
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def convert_dict(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/api/players', methods=['GET'])
def get_player():
    results = []
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    players = db.execute('SELECT * FROM Players').fetchall()

    if 'id' in request.args:
        id = int(request.args['id'])

        for player in players:
            if player['id'] == id:
                results.append(player)

        return jsonify(results)

    else:
        return jsonify(players)

@app.route('/api/players/update', methods=['PUT'])
def update_player():
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    
    if 'id' not in request.args:
        abort(400)
    if not request.form:
        abort(400)
    
    id = int(request.args['id'])
    return jsonify(db.execute('SELECT FROM Players WHERE id=2'))

if __name__ == "__main__":
    app.run()