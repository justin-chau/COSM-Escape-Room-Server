import flask
from flask import request, jsonify, abort
from flask_cors import CORS
import sqlite3
import random
import logging

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

server_started = False

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
        update_player_value(id, key, request.form.get(key))

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
        update_puzzle_value(id, key, request.form.get(key))

    query_string = "SELECT * FROM Puzzle_{id}".format(id=id)
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

def update_player_value(player_id, key, value):
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    query_string = "UPDATE Players SET '{key}' = '{value}' WHERE player_id = '{id}'".format(key=key, value=value, id=player_id)
    db.execute(query_string)
    server_update_string = "[COSMOS] Updating Player Status: '{key}' to '{value}' for player with ID '{id}'".format(key=key, value=value, id=player_id)
    print(server_update_string)

def update_puzzle_value(puzzle_id, key, value):
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    query_string = "UPDATE Puzzle_{id} SET '{key}' = '{value}'".format(id=puzzle_id, key=key, value=value)
    db.execute(query_string)
    server_update_string = "[COSMOS] Updating Puzzle Status: '{key}' to '{value}' for puzzle with ID '{id}'".format(key=key, value=value, id=puzzle_id)
    print(server_update_string)

def send_notification(player_id, key, value):
    db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
    db_connection.row_factory = convert_dict
    db = db_connection.cursor()
    query_string = "UPDATE Notifications SET '{key}' = '{value}' WHERE player_id = '{id}'".format(key=key, value=value, id=player_id)
    db.execute(query_string)
    if (key == 'notification'):
        query_string = "UPDATE Notifications SET 'received' = '0' WHERE player_id = '{id}'".format(id=player_id)
        db.execute(query_string)
        server_update_string = "[COSMOS] Sending SIREBand Notification: '{value}' to player with ID '{id}'".format(value=value, id=player_id)
        print(server_update_string)
    else:
        server_update_string = "[COSMOS] Sending SIREBand Data: '{key}' to '{value}' to player with ID '{id}'".format(key=key, value=value, id=player_id)
        print(server_update_string)
    
if __name__ == "__main__":
    print("[COSMOS] **CTRL+C TO START SERVER LOGIC")
    app.run(host='0.0.0.0')
    spy_band = random.randint(0, 2)

    while(True):
        db_connection = sqlite3.connect('escape_database.db', isolation_level=None)
        db_connection.row_factory = convert_dict
        db = db_connection.cursor()
        query_string = "SELECT * FROM Puzzle_1"
        puzzle_1_data = db.execute(query_string).fetchall()
        query_string = "SELECT * FROM Puzzle_2"
        puzzle_2_data = db.execute(query_string).fetchall()
        query_string = "SELECT * FROM Puzzle_3"
        puzzle_3_data = db.execute(query_string).fetchall()
        query_string = "SELECT * FROM Puzzle_4"
        puzzle_4_data = db.execute(query_string).fetchall()
        puzzle_1_complete = puzzle_1_data[0]['is_finished']
        puzzle_2_complete = puzzle_2_data[0]['is_finished']
        puzzle_3_complete = puzzle_3_data[0]['is_finished']
        puzzle_4_complete = puzzle_4_data[0]['is_finished']
        
        if (server_started == False):
            print("[COSMOS] **RESETTING PLAYER VALUES")
            update_player_value(0, 'name', 'Player 1')
            update_player_value(1, 'name', 'Player 2')
            update_player_value(2, 'name', 'Player 3')
            update_player_value(0, 'oxygen', 100)
            update_player_value(1, 'oxygen', 100)
            update_player_value(2, 'oxygen', 100)
            update_player_value(0, 'is_spy', 0)
            update_player_value(1, 'is_spy', 0)
            update_player_value(2, 'is_spy', 0)
            update_player_value(0, 'current_rfid', 0)
            update_player_value(1, 'current_rfid', 0)
            update_player_value(2, 'current_rfid', 0)
            update_player_value(0, 'chest_key', 0)
            update_player_value(1, 'chest_key', 0)
            update_player_value(2, 'chest_key', 0)
            update_player_value(0, 'spy_key', 0)
            update_player_value(1, 'spy_key', 0)
            update_player_value(2, 'spy_key', 0)
            print("[COSMOS] **RESETTING PUZZLE VALUES")
            update_puzzle_value(1, 'current_code', 0)
            update_puzzle_value(1, 'is_correct', 0)
            update_puzzle_value(1, 'is_finished' , 0)
            update_puzzle_value(2, 'current_coordinates', 0)
            update_puzzle_value(2, 'is_correct', 0)
            update_puzzle_value(2, 'is_finished' , 0)
            update_puzzle_value(3, 'pc_1_inserted', 0)
            update_puzzle_value(3, 'pc_2_inserted', 0)
            update_puzzle_value(3, 'pc_complete', 0)
            update_puzzle_value(3, 'is_finished' , 0)
            update_puzzle_value(4, 'band_slot_1', 0)
            update_puzzle_value(4, 'band_slot_2', 0)
            update_puzzle_value(4, 'excluded_player', 0)
            update_puzzle_value(4, 'is_finished' , 0)
            print("[COSMOS] **SENDING STARTING MESSAGE TO BANDS")
            send_notification(0, 'trigger_morse', 0)
            send_notification(1, 'trigger_morse', 0)
            send_notification(2, 'trigger_morse', 0)
            send_notification(0, 'notification', 'Transmission: Escape from the HELIOS Ship. Lock the doors.')
            send_notification(1, 'notification', 'Transmission: Escape from the HELIOS Ship. Lock the doors.')
            send_notification(2, 'notification', 'Transmission: Escape from the HELIOS Ship. Lock the doors.')
            print("[COSMOS] **RANDOMIZING SPY")
            update_player_value(spy_band, 'is_spy', 1)
            print("[COSMOS] **SERVER STARTED")
            server_started = True

        if (puzzle_1_complete == False):
            if (puzzle_1_data[0]['current_code'] == 832):
                print ("[COSMOS] **PLAYERS HAVE ENTERED THE CORRECT CODE FOR PUZZLE 1")
                #FLASH LEDS AND PLAY NOISE
                update_puzzle_value(1, 'is_correct', 1)
                update_puzzle_value(1, 'is_finished', 1)
                send_notification(0, 'notification', 'Transmission: Sending encrypted message.')
                send_notification(1, 'notification', 'Transmission: Sending encrypted message.')
                send_notification(2, 'notification', 'Transmission: Sending encrypted message.')
                send_notification(0, 'trigger_morse', 1)
                send_notification(1, 'trigger_morse', 1)
                send_notification(2, 'trigger_morse', 1)

        if (puzzle_2_complete == False):
            if (puzzle_2_data[0]['current_coordinates'] == 123456):
                print ("[COSMOS] **PLAYERS HAVE ENTERED THE CORRECT COORDINATES FOR PUZZLE 2")
                #FLASH LEDS AND PLAY NOISE
                update_puzzle_value(2, 'is_correct', 1)
                update_puzzle_value(2, 'is_finished', 1)
                send_notification(0, 'trigger_morse', 0)
                send_notification(1, 'trigger_morse', 0)
                send_notification(2, 'trigger_morse', 0)
                send_notification(0, 'notification', 'Transmission: Transmitted to Metalliance Authentication Key')
                send_notification(1, 'notification', 'Transmission: Transmitted to Metalliance Authentication Key')
                send_notification(2, 'notification', 'Transmission: Transmitted to Metalliance Authentication Key')
                send_notification(spy_band, 'notification', 'Transmission: You are the spy. Scan the emblem.')

        if (puzzle_3_complete == False):
            #LOGIC FOR SPY GETTING CORRUPTED KEY
            #LOGIC FOR GETTING CHEST KEY
            if (puzzle_3_data[0]['pc_1_inserted'] and puzzle_3_data[0]['pc_2_inserted']):
                print ("[COSMOS] **PLAYERS HAVE ENTERED THE CORRECT COORDINATES FOR PUZZLE 2")
                #FLASH LEDS AND PLAY NOISE
                update_puzzle_value(3, 'pc_complete', 1)
                update_puzzle_value(3, 'is_finished', 1)
                send_notification(0, 'notification', 'Transmission: Ship Status: OK - Scan two correct authentication keys.')
                send_notification(1, 'notification', 'Transmission: Ship Status: OK - Scan two correct authentication keys.')
                send_notification(2, 'notification', 'Transmission: Ship Status: OK - Scan two correct authentication keys.')
                send_notification(spy_band, 'notification', 'Transmission: You are the spy. Scan the emblem.')

        # if (puzzle_4_complete == False):
            #LOGIC FOR REBELS SCANNING
            