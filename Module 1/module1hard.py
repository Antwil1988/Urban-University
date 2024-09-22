# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем словарь с именами учеников в алфавитном порядке и их оценками
sorted_students = sorted(students)
student_grades = dict(zip(sorted_students, grades))

# Вычисляем средний балл для каждого ученика / # Использование items() для получения ключей и значений
average_scores = {student: sum(grades) / len(grades) for student, grades in student_grades.items()}

# Выводим результат
print(average_scores)
