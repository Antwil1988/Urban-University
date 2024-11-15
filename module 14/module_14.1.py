import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

for i in range(1, 11):
    username = f'User{i}'
    email = f'example{i}@gmail.com'
    age = i * 10
    balance = 1000
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, balance))

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

# Удаляем каждую 3ую запись в таблице начиная с 1ой
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# Выбираем все записи, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
records = cursor.fetchall()

# Выводим записи в консоль
for record in records:
    print(f'Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}')


connection.commit()
connection.close()