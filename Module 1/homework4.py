my_string = input("Введите текст: ")
print("Количество символов в введенном тексте:", len(my_string))
print("Строка в верхнем регистре:", my_string.upper())
print("Строка в нижнем регистре:", my_string.lower())
my_string_no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", my_string_no_spaces)

print('Первый символ текста:',my_string[0])
print('Последний символ текста: ',my_string[-1])