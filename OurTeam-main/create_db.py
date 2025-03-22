import sqlite3
import os

DATABASE_FILE = "people.db"
IMAGE_DIR = "images"  # Папка, где находятся изображения JPG

def create_database(db_file):
    """Создает базу данных и таблицу для хранения информации о людях и их фотографий."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Создаем таблицу, если она еще не существует
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                photo_filename BLOB NOT NULL,
                info TEXT
            )
        """)
        conn.commit()
        print(f"База данных '{db_file}' и таблица 'people' успешно созданы.")

    except sqlite3.Error as e:
        print(f"Ошибка SQLite: {e}")
    finally:
        if conn:
            conn.close()

def insert_person(db_file, name, photo_filename, info):
    """Вставляет информацию о человеке в базу данных."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        sql = "INSERT INTO people (name, photo_filename, info) VALUES (?, ?, ?)"
        cursor.execute(sql, (name, photo_filename, info))
        conn.commit()
        print(f"Информация о '{name}' успешно вставлена.")

    except sqlite3.Error as e:
        print(f"Ошибка SQLite: {e}")
    finally:
        if conn:
            conn.close()

# --- Main ---
if __name__ == "__main__":
    # 1. Создаем базу данных
    create_database(DATABASE_FILE)

    # 2. Убеждаемся, что папка с изображениями существует
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    # 3. Вставляем информацию о членах команды
    insert_person(DATABASE_FILE, "Караоглонян Лиза", "img/Liza.jpg", "дизайнер")
    insert_person(DATABASE_FILE, "Дрокина Василиса", "img/Vasilisa.jpg", "дизайнер")
    insert_person(DATABASE_FILE, "Хохлова Аксинья", "img/aksiny.jpg", "дизайнер")
    insert_person(DATABASE_FILE, "Хохлова Аксинья", "img/aksiny.jpg", "дизайнер")
    insert_person(DATABASE_FILE, "Ситдиков Динар", "img/dinar.jpg", "разработчик")
    insert_person(DATABASE_FILE, "Скрыпкин Макар", "img/Makar.jpg", "разработчик")
    insert_person(DATABASE_FILE, "Ситдиков Динар", "img/Sergey.jpg", "разработчик")
    insert_person(DATABASE_FILE, "Панченко Злата", "img/Zlata.jpg", "разработчик.Камень я не дам")
    insert_person(DATABASE_FILE, "Сулацкий Владимир", "img/vova.jpg", "тестировщик")
    insert_person(DATABASE_FILE, "Исаев Денис", "img/Denis.jpg", "тестировщик")
    insert_person(DATABASE_FILE, "Мамедов Аликпер", "img/Alik.jpg", "тестировщик")
    insert_person(DATABASE_FILE, "Резанов Кирилл", "img/Rezanov.jpg", "тестировщик")
    insert_person(DATABASE_FILE, "Пильчук Семён", "img/Pilchuk.jpg", "тестировщик") 
    insert_person(DATABASE_FILE, "Александр Елисеев", "img/selisey.jpg", "поддержка")
    insert_person(DATABASE_FILE, "Убушаев Эльвег", "img/Elveg.jpg", "поддержка")
    insert_person(DATABASE_FILE, "Дегтярев Александр", "img/Degtyar.jpg", "поддержка")
    print("База данных создана и заполнена.")

    print("Готово.")