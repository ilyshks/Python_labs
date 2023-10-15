from Dish import Dish
from ProductCard import ProductCard
import Check
import functions

dishes = [Dish("Салат", 500, ("Помидоры", "Огурцы", "Оливковое масло")),
          Dish("Стейк", 1000, ("Мясо", "Соус томатный")),
          Dish("Пицца", 550, ("Мясо", "Сыр", "Помидоры", "Майонез", "Кетчуп")),
          Dish("Бургер", 350, ("Булка", "Котлета", "Ломтики помидора", "Ломтики огурца", "Кетчуп")),
          Dish("Суп", 400, ("Кусочки говядины", "Морковь", "Картошка", "Вермишель"))]

goods = [ProductCard("Часы", 10000), ProductCard("Палатка", 6000, '111111'),
         ProductCard("Удочка", 5000), ProductCard("PS 5", 25000), ProductCard("Монитор", 20000)]

addresses_of_restaurants = ["ул. Арбат, 44, стр. 1", "Страстной бул., 8А",
                            "2-я Брестская ул., 48", "Новослободская ул., 16"]

addresses_of_delivery_points = ["Волков пер., 9, стр. 1", "Мещанская ул., 14",
                                "Заводской пр., 10", "Котельническая наб., 25, корп. 2"]
restaurant_orders = []
market_orders = []
functions.menu()
task = Check.check_menu(1, 7)
while task != 7:
    if task == 1:
        file_name = input("Введите название файла: ")
        load_dishes, load_goods, load_addresses_of_restaurants, load_addresses_of_delivery_points, \
            load_restaurant_orders, load_market_orders = functions.load_data(file_name)
        if all([load_dishes, load_goods, load_addresses_of_restaurants, load_addresses_of_delivery_points]):
            dishes, goods, addresses_of_restaurants = load_dishes, load_goods, load_addresses_of_restaurants
            addresses_of_delivery_points = load_addresses_of_delivery_points
            restaurant_orders, market_orders = load_restaurant_orders, load_market_orders

    elif task == 2:
        print("\nУкажите в каком ресторане Вы хотите сделать заказ.")
        print("Выберите ресторан по адресу, указав ID:")
        print("ID\tАдрес")
        for i, address in enumerate(addresses_of_restaurants, 1):
            print(f"{i}\t{address}")
        number_of_restaurant = Check.check_limited_int(1, len(addresses_of_restaurants))

        print("\nМеню ресторана:")
        for i, dish in enumerate(dishes, 1):
            print(f"\nНомер блюда: {i}")
            print(dish)

        print("Введите номера блюд через пробел, которые хотите заказать: ")
        numbers_of_dishes = Check.check_numbers_of_dishes(1, len(dishes))
        print("Спасибо за заказ!\n Готовим...\n")

        functions.make_restaurant_order(dishes, numbers_of_dishes, addresses_of_restaurants,
                                        number_of_restaurant, restaurant_orders)

    elif task == 3:
        print("\nТовары доступные к заказу:")
        for i, good in enumerate(goods, 1):
            print(f"\nНомер товара: {i}")
            print(good)

        print("Введите номера товаров через пробел, которые хотите заказать: ")
        numbers_of_goods = Check.check_numbers_of_goods(1, len(goods))
        print("Выберите пункт выдачи:")
        print("ID\tАдрес")
        for i, address in enumerate(addresses_of_delivery_points, 1):
            print(f"{i}\t{address}")
        number_of_market = Check.check_limited_int(1, len(addresses_of_delivery_points))

        print("Спасибо за заказ!\n Собираем...\n")

        functions.make_online_market_order(goods, numbers_of_goods, addresses_of_delivery_points,
                                           number_of_market, market_orders)
    elif task == 4:
        functions.show_all_rest_orders(restaurant_orders)
    elif task == 5:
        functions.show_all_market_orders(market_orders)
    elif task == 6:
        functions.dump_data(dishes, goods, addresses_of_restaurants, addresses_of_delivery_points,
                            restaurant_orders, market_orders)
    functions.menu()
    task = Check.check_menu(1, 7)
print("Выход из программы!")
