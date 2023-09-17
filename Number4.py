import os
from string import ascii_letters,  digits
from random import randint, sample, shuffle


def create_files(count=1000):
    used_names = set()
    for _ in range(count):
        name_of_file = list(''.join(sample(ascii_letters, randint(1, 7))) + ''.join(sample(digits, randint(1, 7))))
        shuffle(name_of_file)
        name_of_file = ''.join(name_of_file)
        while name_of_file in used_names:
            name_of_file = list(''.join(sample(ascii_letters, randint(1, 7))) + ''.join(sample(digits, randint(1, 7))))
            shuffle(name_of_file)
            name_of_file = ''.join(name_of_file)
        file = open("example/" + name_of_file + '.txt', 'w')
        file.close()


name = 'example'
try:
    os.mkdir(name)
    print('Директория успешно создана!')
except FileExistsError:
    print(f'Директория с именем {name} уже существует!')
finally:
    create_files()
