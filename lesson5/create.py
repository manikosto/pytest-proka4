import sqlite3
import random
import string

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      department TEXT NOT NULL
                      );""")
    conn.commit()

def insert_employee(conn, employee):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", employee)
    conn.commit()

def random_name(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def main():
    database = "test.db"

    conn = create_connection(database)

    if conn is not None:
        create_table(conn)

        # Customize the number of records and departments as needed
        num_records = 100
        departments = ['HR', 'IT', 'Sales', 'Marketing', 'Finance']

        for _ in range(num_records):
            name = random_name(10)
            age = random.randint(20, 60)
            department = random.choice(departments)
            insert_employee(conn, (name, age, department))

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
