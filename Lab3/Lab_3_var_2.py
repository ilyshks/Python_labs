from RestaurantOrder import RestaurantOrder
from OnlineMarketOrder import OnlineMarketOrder
from Dish import Dish
from ProductCard import ProductCard
from datetime import datetime
import Check
import random

dishes = [Dish("Салат", 500, ("Помидоры", "Огурцы", "Оливковое масло")),
          Dish("Стейк", 1000, ("Мясо", "Соус томатный")),
          Dish("Пицца", 550, ("Мясо", "Сыр", "Помидоры", "Майонез", "Кетчуп"))]

goods = [ProductCard("Часы", 10000), ProductCard("Палатка", 6000, '111111'),
         ProductCard("Удочка", 5000)]

restaurant_order = RestaurantOrder(dishes=dishes, table_number=10, address="Тверская ул, д. 15")
restaurant_order -= dishes[0]

restaurant_order2 = RestaurantOrder(dishes=dishes[:2], table_number=9, address="Тверская ул, д. 15")

online_market_order = OnlineMarketOrder(goods=goods, delivery_point="Комсомольская ул, д.3",
                                        delivery_date=datetime(2023, 10, 5, 12, 30))

online_market_order2 = OnlineMarketOrder(goods=goods, delivery_point="Ипатьевский пер, д.44",
                                         delivery_date=datetime(2023, 10, 4, 11))

print(restaurant_order)
print("Равны ли заказы в ресторане? -", restaurant_order.is_equal(restaurant_order2))
print()
print(online_market_order)
print("Равны ли онлайн заказы? -", online_market_order.is_equal(online_market_order2))
print()
print("Информация о стоимости товаров в онлайн заказе №1 с учётом НДС:")
price_lst = online_market_order.price_of_components()
for name, price in price_lst:
    print(name, price, sep='\t')

print("Где Вы хотите сделать заказ?")
print("В ресторане - введите 1, на маркетплейсе - 2")
num = Check.check_menu()
if num == 1:
    print("\nМеню ресторана:")
    for i, dish in enumerate(dishes, 1):
        print(f"\nНомер блюда: {i}")
        print(dish)

    print("Введите номера блюд через пробел, которые хотите заказать: ")
    numbers_of_dishes = Check.check_numbers_of_dishes(1, len(dishes))
    print("Спасибо за заказ!\n Готовим...\n")

    console_dishes = [dishes[number-1] for number in numbers_of_dishes]
    console_restaurant_order = RestaurantOrder(console_dishes, random.randint(1, 10), "Тверская ул, д. 34")
    print("Блюда у Вас на столе!")

    print(*[dish.name for dish in console_dishes], sep='\n')
    print("Пришло время заплатить за заказ, Ваш чек:")
    money = console_restaurant_order.price_of_components()
    s = 0
    for name, price in money:
        print(name, price, sep='\t')
        s += price
    print("Итого: ", s, "р.")

else:
    print("\nТовары доступные к заказу:")
    for i, good in enumerate(goods, 1):
        print(f"\nНомер товара: {i}")
        print(good)

    print("Введите номера товаров через пробел, которые хотите заказать: ")
    numbers_of_goods = Check.check_numbers_of_goods(1, len(goods))
    print("Спасибо за заказ!\n Собираем...\n")

    console_goods = [goods[number - 1] for number in numbers_of_goods]
    console_online_market_order = OnlineMarketOrder(console_goods, "Сокольническая пл, д. 15",
                                                    datetime(2023, 10, random.randint(1, 15), 15))

    print("Ваш заказ собран! Вы заказали:")
    print(*[good.name for good in console_goods], sep='\n')
    print()
    print("Заказ передан в доставку!")

    print("Адрес пункта выдачи: ", console_online_market_order.delivery_point)
    print("Примерная дата доставки: ", console_online_market_order.delivery_date)
    print()
    print("Заказ доставлен, Ваш чек:")
    money = console_online_market_order.price_of_components()
    s = 0
    for name, price in money:
        print(name, price, sep='\t')
        s += price
    print("Итого: ", s, "р.")
