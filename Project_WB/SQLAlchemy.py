import sqlite3

# Создание базы данных
connection = sqlite3.connect('WB.db')

# Создание курсора
cursor = connection.cursor()

# Создание таблицы "users"
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Создание таблицы "queries"
cursor.execute('''CREATE TABLE IF NOT EXISTS queries
                  (id INTEGER PRIMARY KEY, user_id INTEGER, query TEXT, discount REAL,
                   FOREIGN KEY(user_id) REFERENCES users(id))''')

# Создание таблицы "products"
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER PRIMARY KEY, query_id INTEGER, name TEXT, price REAL,
                   previous_price REAL, updated_at TEXT,
                   FOREIGN KEY(query_id) REFERENCES queries(id))''')

# Сохранение изменений
connection.commit()

# Закрытие соединения
connection.close()


