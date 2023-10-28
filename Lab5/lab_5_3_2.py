from random import randint
from time import time
from concurrent.futures import ProcessPoolExecutor


def calculate_element(i, j):
    return 1 / (1 + (q[i] - p[j])**2)


def create_row(n, i):
    return [calculate_element(i, j) for j in range(n)]


def create_matrix(n):
    arr = []
    for i in range(n):
        row = [calculate_element(i, j) for j in range(n)]
        arr.append(row)
    return arr


def main():
    arr = []
    with ProcessPoolExecutor() as executor:
        for row in executor.map(create_row, [5000]*5000, range(5000)):
            arr.append(row)
    return arr


q = [randint(1, 1000) for _ in range(5000)]
p = [randint(1, 1000) for _ in range(5000)]


if __name__ == '__main__':
    start = time()
    m = create_matrix(5000)
    print("Время без concurrent.futures:", time() - start)
    new_start = time()
    matrix = main()
    print("Время с concurrent.futures:", time() - new_start)
