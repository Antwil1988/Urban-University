
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []


for n in numbers:
    if n > 1:  # Простые числа начинаются с 2
        flag = True

        # Проверка делителей числа, начиная с 2 до корня из number
        for i in range(2, int(n**0.5) + 1):
            # число в степени 0,5 эквивалентно извлечению квадратного корня из number + 1
            if n % i == 0:
                flag = False
                break   # прерывание цикла, если нашёлся делитель
        if flag:
            primes.append(n)
        else:
            not_primes.append(n)

print("Primes:", primes)
print("Not Primes:", not_primes)