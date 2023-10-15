def check_menu(mn, mx):
    num = input("Введите номер функции: ")
    while True:
        try:
            num = int(num)
            if mn <= num <= mx:
                return num
            num = input(f"Введите заново число от {mn} до {mx}: ")
        except ValueError:
            num = input(f"Введите заново число от {mn} до {mx}: ")


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


def check_limited_int(mn, mx):
    num = input(f"Введите целое число от {mn} до {mx}: ")
    while True:
        try:
            num = int(num)
            if mn <= num <= mx:
                return num
            num = input(f"Введите заново целое число от {mn} до {mx}: ")
        except ValueError:
            num = input(f"Введите заново целое число от {mn} до {mx}: ")