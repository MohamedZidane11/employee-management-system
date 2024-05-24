import sqlite3


def create_table():
    conn = sqlite3.connect("Employees.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees(
            emp_id TEXT PRIMARY KEY,
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


def insert_employee(emp_id, name, role, gender, status):
    conn = sqlite3.connect("Employees.db")
    cursor = conn.cursor()

    cursor.execute('insert into Employees (emp_id, name, role, gender, status) values (?, ?, ?, ?, ?)',
                   (emp_id, name, role, gender, status))
    conn.commit()
    conn.close()


def delete_employee(emp_id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('delete from Employees where emp_id = ?', (emp_id,))
    conn.commit()
    conn.close()


def update_employee(new_name, new_role, new_gender, new_status, emp_id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('update Employees set name=?, role=?, gender=?, status=? where emp_id=?',
                   (new_name, new_role, new_gender, new_status, emp_id))
    conn.commit()
    conn.close()


def id_exists(emp_id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('select count(*) from Employees where emp_id=?', (emp_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


create_table()
