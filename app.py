from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'users.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dob DATE NOT NULL,
            occupation TEXT NOT NULL
        )''')

@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name,dob,occupation) VALUES (?,?,?)",
                    (data['name'], data['dob'], data['occupation']))
        conn.commit()
    return jsonify({'status': 'success'})

@app.route('/users', methods=['GET'])
def get_users():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, dob, occupation FROM users")
        users = cur.fetchall()
    return jsonify(users)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
