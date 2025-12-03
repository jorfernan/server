from flask import Flask, render_template
import sqlite3
import os
import json
import sys

app = Flask(__name__, static_folder='public', static_url_path='/public')

DB_PATH = os.path.join("database", "database.db")
CONFIG_PATH = os.path.join("config", "settings.json")

if not os.path.exists(DB_PATH):
    print("\033[91m\033[1m\n[ERROR] Base de datos no inicializada, por favor, ejecute el archivo init.py antes de iniciar el servidor\n\033[0m")
    sys.exit(1)

if not os.path.exists(CONFIG_PATH):
    print("\033[91m\033[1m\n[ERROR] Archivo de configuración no encontrado en ("+ CONFIG_PATH +"), descargue la carpeta del repositorio original nuevamente antes de iniciar el servidor\n\033[0m")
    sys.exit(1)


DEFAULT_CONFIG = {
    "site_title": "Mi Aplicación",
    "site_language": "es",
    "site_last_year_update": "2024",
    "site_auhor": "Alumno alumno alumno",
    "site_description": "Playground para los alumnos de lenguaje de marcas",
    "site_keywords": "lenguaje de marcas, html, css, xml, json, javascript, etiquetas, atributos, sintaxis, estructura, documento, web, maquetación, diseño web, hojas de estilo, validación, semántica, front end, desarrollo web, prácticas, ejercicios, codificación, estándares web, w3c"
}

def load_config():
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"[WARN] Error al cargar config.json: {e}")
    return DEFAULT_CONFIG

def get_users():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # para acceder por nombre de columna
    cur = conn.cursor()
    cur.execute("SELECT id, name, password FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

@app.context_processor
def inject_config():
    return {"config": load_config()}

@app.route("/")
def index():
    users = get_users()
    return render_template("index.html", users = users)

@app.route("/tasks")
def tasks():
    return  render_template("tasks.html")

if __name__ == "__main__":
    app.run(debug=True)
