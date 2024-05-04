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


def fetch_employees():
    conn = sqlite3.connect("Employees.db")
    cursor = conn.cursor()

    cursor.execute('select * from Employees')
    all_employees = cursor.fetchall()
    conn.close()
    return all_employees


def insert_employee(name, role, gender, status):
    conn = sqlite3.connect("Employees.db")
    cursor = conn.cursor()
    cursor.execute('insert into Employees (name, role, gender, status) values (?, ?, ?, ?)',
                   (name, role, gender, status))
    conn.commit()
    conn.close()


def delete_employee(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('delete from Employees where id = ?', (id,))
    conn.commit()
    conn.close()


def update_employee(new_name, new_role, new_gender, new_status, id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('update Employees set name=?, role=?, gender=?, status=? where id=?',
                   (new_name, new_role, new_gender, new_status, id))
    conn.commit()
    conn.close()


def id_exists(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('select count(*) from Employees where id=?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


create_table()
