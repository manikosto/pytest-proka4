import sqlite3

class TestDBConnect:

    def setup(self):
        # Создание подключения к базе данных SQLite в памяти
        self.conn = sqlite3.connect(':memory:')
        # Создание таблицы "users"
        self.conn.execute('''CREATE TABLE users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL
                        )''')
        # Вставка данных в таблицу "users"
        self.conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("John Smith", "john.smith@example.com"))
        self.conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice Johnson", "alice.johnson@example.com"))
        self.conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob Jones", "bob.jones@example.com"))
        self.conn.commit()
        self.cursors = self.conn.cursor()

    def test_get_users_from_db(self):
        self.cursors.execute("SELECT * FROM users")
        rows = self.cursors.fetchall()
        assert len(rows) == 3
        print(rows)

    def teardown(self):
        self.conn.close()
