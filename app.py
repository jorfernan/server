from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__, static_folder='public', static_url_path='/public')
DB_PATH = os.path.join("database", "database.db")

def get_users():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # para acceder por nombre de columna
    cur = conn.cursor()
    cur.execute("SELECT id, name, password FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows



@app.route("/")
def index():
    users = get_users()
    return render_template("index.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)
