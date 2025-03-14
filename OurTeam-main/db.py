import sqlite3

def create_database():
    conn = sqlite3.connect('team.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            photo TEXT, 
            info TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_person(name, photo, info):
    conn = sqlite3.connect('team.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO team (name, photo, info) VALUES (?, ?, ?)", (name, photo, info))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    add_person("Караоглонян Лиза", "img/Liza.jpg", "дизайнер")
    add_person("Дрокина Василиса", "img/Vasilisa.jpg", "дизайнер")
    add_person("Хохлова Аксинья", "img/aksiny.jpg", "дизайнер")
    add_person("Ситдиков Динар", "img/dinar.jpg", "разработчик")
    add_person("Скрыпкин Макар", "img/Makar.jpg", "разработчик")
    add_person("Ситдиков Динар", "img/Sergey.jpg", "разработчик")
    add_person("Панченко Злата", "img/Zlata.jpg", "разработчик.Камень я не дам")
    add_person("Сулацкий Владимир", "img/vova.jpg", "тестировщик")
    add_person("Исаев Денис", "img/Denis.jpg", "тестировщик")
    add_person("Мамедов Аликпер", "img/Alik.jpg", "тестировщик")
    add_person("Резанов Кирилл", "img/Rezanov.jpg", "тестировщик")
    add_person("Пильчук Семён", "img/Pilchuk.jpg", "тестировщик") 
    add_person("Александр Елисеев", "img/selisey.jpg", "поддержка")
    add_person("Убушаев Эльвег", "img/Elveg.jpg", "поддержка")
    add_person("Дегтярев Александр", "img/Degtyar.jpg", "поддержка")
    print("База данных создана и заполнена.")