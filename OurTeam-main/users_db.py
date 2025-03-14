import sqlite3

# Создание базы данных и таблицы
def create_database():
    connection = sqlite3.connect('users.db')  # Создание базы данных
    cursor = connection.cursor()

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()
    print("База данных и таблица пользователей созданы.")