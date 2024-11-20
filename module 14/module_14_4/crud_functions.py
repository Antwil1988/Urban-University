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
        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?,?,?)', records)
        connection.commit()
        connection.close()
        print(f"создана база данных {Products}")
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


initiate_db('Products.db')



