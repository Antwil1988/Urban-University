import sqlite3


def initiate_db(Products):
    try:
        connection = sqlite3.connect(Products)
        cursor = connection.cursor()

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )''')

        records = [
            ('Витамин B9', 'Описание 1', 100),
            ('Витамин D3', 'Описание 2', 200),
            ('Магний B6', 'Описание 3', 300),
            ('Цинк', 'Описание 4', 400)
        ]

        cursor.executemany(
            'INSERT INTO Products (title, description, price) VALUES (?,?,?)', records)

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )''')

        connection.commit()
        connection.close()

        print(f"Создана база данных {Products}")
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")


def get_all_products(Products):
    try:
        connection = sqlite3.connect(Products)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Products')
        records = cursor.fetchall()
        connection.close()
        return records
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
        return []


def add_user(username, email, age):
    try:
        connection = sqlite3.connect('Products.db')
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', {age}, 1000)")
        connection.commit()
        connection.close()
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")


def is_included(username):
    conn_user = sqlite3.connect('Products.db')
    cursor1 = conn_user.cursor()
    cursor1.execute("SELECT * FROM Users WHERE username = ?", (username,))
    result = cursor1.fetchone()
    conn_user.close()
    return result is not None



initiate_db('Products.db')


