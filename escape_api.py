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
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()

    if 'player_id' in request.args:
        id = int(request.args['player_id'])
        query_string = "SELECT * FROM Players WHERE player_id = '{id}'".format(id=id)
        return jsonify(db.execute(query_string).fetchall())

    else:
        query_string = "SELECT * FROM Players"
        return jsonify(db.execute(query_string).fetchall())

@app.route('/api/players/update', methods=['PUT'])
def update_player():
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    
    if 'player_id' not in request.args:
        abort(400)
    if not request.form:
        abort(400)

    id = int(request.args['player_id'])

    for key in request.form:
        query_string = "UPDATE Players SET '{key}' = '{value}' WHERE player_id = '{id}'".format(key=key, value=request.form.get(key), id=id)
        db.execute(query_string)

    query_string = "SELECT * FROM Players WHERE player_id = '{id}'".format(id=id)
    return jsonify(db.execute(query_string).fetchall())

@app.route('/api/puzzles', methods=['GET'])
def get_puzzle():
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()

    if 'puzzle_id' not in request.args:
        abort(400)

    id = int(request.args['puzzle_id'])

    query_string = "SELECT * FROM Puzzle_{id}".format(id=id)
    print(query_string)
    return jsonify(db.execute(query_string).fetchall())

@app.route('/api/puzzles/update', methods=['PUT'])
def update_puzzle():
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()

    if 'puzzle_id' not in request.args:
        abort(400)
    if not request.form:
        abort(400)

    id = int(request.args['puzzle_id'])

    for key in request.form:
        query_string = "UPDATE Puzzle_{id} SET '{key}' = '{value}'".format(id=id, key=key, value=request.form.get(key))
        db.execute(query_string)

    query_string = "SELECT * FROM Players_{id}".format(id=id)
    return jsonify(db.execute(query_string).fetchall())

@app.route('/api/push_notifications', methods=['GET'])
def get_notification():
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()

    if 'player_id' in request.args:
        id = int(request.args['player_id'])
        query_string = "SELECT * FROM Notifications WHERE player_id = '{id}'".format(id=id)
        return jsonify(db.execute(query_string).fetchall())

    else:
        query_string = "SELECT * FROM Notifications"
        return jsonify(db.execute(query_string).fetchall())

@app.route('/api/push_notifications/update', methods=['PUT'])
def update_notification():
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    
    if 'player_id' not in request.args:
        abort(400)
    if not request.form:
        abort(400)

    id = int(request.args['player_id'])

    for key in request.form:
        query_string = "UPDATE Notifications SET '{key}' = '{value}' WHERE player_id = '{id}'".format(key=key, value=request.form.get(key), id=id)
        db.execute(query_string)

    query_string = "SELECT * FROM Notifications WHERE player_id = '{id}'".format(id=id)
    return jsonify(db.execute(query_string).fetchall())

if __name__ == "__main__":
    app.run(host='0.0.0.0')