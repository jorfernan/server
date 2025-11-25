import os
import sqlite3

def init_database():
    # Ruta de la carpeta donde estará la base de datos
    db_folder = "database"
    db_path = os.path.join(db_folder, "database.db")

    # Crear carpeta si no existe
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)
        print(f"Carpeta creada: {db_folder}")

    # Conectar a la base de datos
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tabla actualizada
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """)

    # Insertar 3 usuarios
    users = [
        ("Alice", "pass123"),
        ("Bob", "qwerty"),
        ("Charlie", "123456")
    ]

    cursor.executemany("INSERT INTO users (name, password) VALUES (?, ?);", users)

    conn.commit()
    conn.close()
    print(f"Base de datos inicializada y usuarios insertados en: {db_path}")


if __name__ == "__main__":
    init_database()
