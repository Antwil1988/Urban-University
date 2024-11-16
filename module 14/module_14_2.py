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

# Удаляем из базы данных запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Считаем общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
print(f'Общее количество записей: {total}')

# Считаем общий баланс всех пользователей
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(f'Общий баланс всех пользователей: {total_balance}')

# Считаем средний баланс всех пользователей
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей: {avg_balance}')


connection.commit()
connection.close()