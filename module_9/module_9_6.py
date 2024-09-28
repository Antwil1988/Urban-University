def all_variants(text):
    for length in range(1, len(text) + 1):
        for i in range(len(text) - length + 1):
            yield text[i:i + length]


# пример работы функции
a = all_variants("abc")
for i in a:
    print(i)

# результат работы программы:
# a
# b
# c
# ab
# bc
# abc
