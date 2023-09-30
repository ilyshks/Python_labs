def check_menu():
    num = input("Введите число: ")
    while True:
        try:
            num = int(num)
            if num == 1 or num == 2:
                return num
            num = input("Введите заново 1 или 2: ")
        except ValueError:
            num = input("Введите заново 1 или 2: ")


def check_numbers_of_dishes(min_number, max_number):
    numbers = input(f"Введите числа через пробел от {min_number} до {max_number}: ").split()
    while True:
        try:
            numbers = list(map(int, numbers))
            for number in numbers:
                if not(min_number <= number <= max_number):
                    raise ValueError
            return numbers
        except ValueError:
            numbers = input(f"Введите заново числа через пробел от {min_number} до {max_number}: ").split()


def check_numbers_of_goods(min_number, max_number):
    numbers = input(f"Введите числа через пробел от {min_number} до {max_number}: ").split()
    while True:
        try:
            numbers = list(map(int, numbers))
            for number in numbers:
                if not(min_number <= number <= max_number):
                    raise ValueError
            return numbers
        except ValueError:
            numbers = input(f"Введите заново числа через пробел от {min_number} до {max_number}: ").split()
