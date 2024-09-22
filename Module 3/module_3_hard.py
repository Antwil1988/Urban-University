def calculate(data):
    count = 0

    if isinstance(data, dict):
        # Для словарей
        for key, value in data.items():
            count += calculate(key)
            count += calculate(value)
    elif isinstance(data, (list, tuple, set)):
        # Для списков, кортежей и множеств
        for item in data:
            count += calculate(item)
    elif isinstance(data, str):
        # Добавляем длину строки к общей сумме
        count += len(data)
    elif isinstance(data, (int, float)):
        # Добавляем числовое значение к общей сумме
        count += data

    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


print(calculate(data_structure))