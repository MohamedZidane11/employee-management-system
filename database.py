import sqlite3


def create_table():
    conn = sqlite3.connect("Employees.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            role TEXT,
            gender TEXT,
            status TEXT)
    ''')
    conn.commit()
    conn.close()

