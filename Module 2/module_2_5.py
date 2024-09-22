def get_matrix(n, m, value,):
    matrix = []
    for i in range(n):     # Перебираем количество строк
        matrix.append([])
        for j in range(m): # Перебираем количество столбцов
            matrix[i].append(value) # Добавить значение в текущую строку
    return(matrix)         # Вернуть завершенную матрицу

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)