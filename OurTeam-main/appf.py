from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE_FILE = "people.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Чтобы получать результаты как словари
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, photo_filename, info FROM people")
    people = cursor.fetchall()  # Получаем все строки
    conn.close()

    return render_template('index.html', people=people)  # Передаем данные в шаблон

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return 'Вы вошли в систему!'
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)