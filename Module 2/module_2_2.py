# Ввод трех чисел
first = int(input('enter:', ))
second = int(input('enter:', ))
third = int(input('enter:', ))

# Проверка условий и вывод результатов
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
