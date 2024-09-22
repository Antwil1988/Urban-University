def generate_password(n):
    result = []
    # Перебираем все возможные пары чисел от 1 до n
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Проверяем, кратна ли сумма пары числу n
            if (i + j) % n == 0:
                result.append(f"{i}{j}")
    # Преобразуем список пар в строку
    return ''.join(result)

for n in range(3, 21):
    print(f"{n} - {generate_password(n)}")