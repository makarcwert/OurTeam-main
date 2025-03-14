import sqlite3

def register_user(username, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
        print("Пользователь зарегистрирован успешно!")
    except sqlite3.IntegrityError:
        print("Ошибка: Логин уже существует.")
    finally:
        connection.close()

if __name__ == '__main__':
    user = input("Введите логин: ")
    pwd = input("Введите пароль: ")
    register_user(user, pwd)