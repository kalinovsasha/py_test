import sqlite3


# cursor.execute("INSERT INTO users (tg_id, name) VALUES ('7640422432', 'sasha')")


def main():
    users = []
    with sqlite3.connect('./db/my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    print(users)


def init_data():
    connection = sqlite3.connect('./db/my_database.db')
    cursor = connection.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER UNIQUE,
    name TEXT NOT NULL
)
""")
    cursor.execute(
        "INSERT INTO users (tg_id, name) VALUES ('7640422432', 'sasha')")
    connection.commit()
    connection.close()


def delete_user(id):
    with sqlite3.connect('./db/my_database.db') as con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM users WHERE tg_id=?", (id,))


def add_user(id: int, name: str):
    with sqlite3.connect('./db/my_database.db') as con:
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO users (tg_id, name) VALUES (?, ?)", (id, name))


if __name__ == "__main__":
    main()


"""
with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT ...")
    """
