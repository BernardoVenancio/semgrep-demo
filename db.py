import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "instance" / "books.db"


def get_db():
    DATABASE.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    schema_path = BASE_DIR / "schema.sql"

    connection = get_db()
    with schema_path.open("r", encoding="utf-8") as schema_file:
        connection.executescript(schema_file.read())
    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()
    print(f"Banco criado em: {DATABASE}")
