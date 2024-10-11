import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

urls = [
    'https://www.wikipedia.org/',
    'https://urban-university.ru/',
    'https://stepik.org/'
]

for url in urls:
    try:
        # отправляется HTTP-запрос на текущий URL
        response = requests.get(url)
        # после отправки запроса проверяется статус ответа
        response.raise_for_status()
        # Если статус ответа равен 200, то HTML-контент ответа парсится
        soup = BeautifulSoup(response.text, 'html.parser')
        # извлекается заголовок страницы
        title = soup.title.string
        print(f"Заголовок страницы {url}: {title}")
        # если во время выполнения кода возникает исключение 
    except requests.RequestException as e:
        print(f"Ошибка при получении {url}: {e}")


# Считывание данных из файла
data = pd.read_csv('data.csv')

# Проверка количества строк и столбцов
print(f"Количество строк: {data.shape[0]}")
print(f"Количество столбцов: {data.shape[1]}")

# Получение статистики данных по каждому столбцу
print(data.describe())

# Вычисление среднего значения по столбцу "Age"
mean_age = data['Age'].mean()
print(f"Средний возраст: {mean_age}")

# Вычисление медианы по столбцу "Salary"
median_salary = data['Salary'].median()
print(f"Медиана зарплаты: {median_salary}")

# Вывод количества мужчин и женщин
print(f"Количество мужчин: {data['Sex'].value_counts()['M']}")
print(f"Количество женщин: {data['Sex'].value_counts()['F']}")

# Вывод количества записей с высшим образованием
print(f"Количество записей с высшим образованием: {data['Education'].value_counts()['High School']}")


# Считывание данных из файла
data = pd.read_csv('data.csv')


# круговая диаграмма для визуализации распределения полов
plt.pie(data['Sex'].value_counts(), labels=['Мужчины', 'Женщины'], autopct='%1.1f%%')
plt.title('Распределение полов')
plt.show()

# столбчатая диаграмма для визуализации распределения уровней образования
plt.bar(data['Education'].value_counts().index, data['Education'].value_counts().values, alpha=0.7, color='lightgreen')
plt.xlabel('Уровень образования')
plt.ylabel('Количество')
plt.title('Распределение уровней образования')
plt.show()

# линейная диаграмма для визуализации распределения зарплат
plt.plot(data['Salary'], marker='o', linestyle='-', color='red')
plt.xlabel('Зарплата')
plt.ylabel('Количество')
plt.title('Распределение зарплат')
plt.show()