from flask import Flask, render_template
import sqlite3
import os
import json

app = Flask(__name__, static_folder='public', static_url_path='/public')

DB_PATH = os.path.join("database", "database.db")
CONFIG_PATH = os.path.join("config", "settings.json")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

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
    config = load_config()

    return render_template("index.html", users = users, config=config)

if __name__ == "__main__":
    app.run(debug=True)
