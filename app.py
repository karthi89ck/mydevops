from flask import Flask, render_template, request, redirect
import psycopg2
import os

app = Flask(__name__)

def get_db_conn():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        occupation = request.form['occupation']
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, dob, occupation) VALUES (%s, %s, %s)",
                    (name, dob, occupation))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    else:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT name, dob, occupation FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
