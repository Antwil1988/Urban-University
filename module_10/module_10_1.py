from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = time()

write_words(10, f'example1.txt')
write_words(30, f'example2.txt')
write_words(200, f'example3.txt')
write_words(100, f'example4.txt')

print(f'Время работы функций {time() - start} секунд')


start = time()

threads = []

t1 = Thread(target=write_words, args=(10, 'example5.txt'))
t2 = Thread(target=write_words, args=(30, 'example6.txt'))
t3 = Thread(target=write_words, args=(200, 'example7.txt'))
t4 = Thread(target=write_words, args=(100, 'example8.txt'))
threads = [t1, t2, t3, t4]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Время работы потоков {time() - start} секунд')