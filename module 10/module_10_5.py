import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line.strip():
            all_data.append(line)
            line = f.readline()


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = time.time()
    for name in filenames:
        read_info(name)
    print(f'Линейный подход: {time.time() - start} секунд')

    start = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f'Многопроцессный подход: {time.time() - start} секунд')
