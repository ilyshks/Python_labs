import queue
from threading import Condition, Thread
from queue import Queue
from time import sleep
from Dish import Dish
from random import choice, randint


cv = Condition()
q = Queue()


def initialize_objects(count=10):
    list_of_names = ["Салат", "Стейк", "Пицца", "Бургер", "Суп"]
    list_of_ingredients = ["Помидоры", "Огурцы", "Оливковое масло", "Мясо", "Соус томатный", "Сыр", "Майонез",
                           "Кетчуп", "Кусочки говядины", "Морковь", "Картошка", "Вермишель"]
    length = len(list_of_ingredients)
    dishes = []
    for _ in range(count):
        tp = (list_of_ingredients[randint(0, length-1)], list_of_ingredients[randint(0, length-1)],
              list_of_ingredients[randint(0, length-1)])
        dishes.append(Dish(choice(list_of_names), randint(100, 1000), tp))

    return dishes


# Consumer function
def working_with_dish(name):
    while True:
        with cv:
            # Ждёт пока очередь пуста
            while q.empty():
                cv.wait()
            try:
                # берём данные из очереди
                dish = q.get_nowait()
                print(f"{name}: {dish}")
                # поймали команду стоп => закрыли поток
                if dish == "stop":
                    break
            except queue.Empty:
                pass
            sleep(0.1)


# Запускаем потоки
Thread(target=working_with_dish, args=("thread 1",)).start()
Thread(target=working_with_dish, args=("thread 2",)).start()
Thread(target=working_with_dish, args=("thread 3",)).start()

# кладём данные в очередь
data = initialize_objects(count=15)
for i in range(len(data)):
    q.put(data[i])

# кладём команды для остановки
for _ in range(3):
    q.put("stop")

# уведомляем все потоки о том, что данные появились в очереди
with cv:
    cv.notify_all()
