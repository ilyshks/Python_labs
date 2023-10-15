import Check
import random
import pickle
from datetime import datetime
from OnlineMarketOrder import OnlineMarketOrder
from RestaurantOrder import RestaurantOrder
from MyExceptions import *


def menu():
    print("\nМеню:")
    print("Прочитать данные с файла\t\t1")
    print("Сделать заказ в ресторане\t\t2")
    print("Сделать заказ на онлайн маркете\t\t3")
    print("Посмотреть все заказы в ресторанах\t\t4")
    print("Посмотреть все заказы на онлайн маркете\t\t5")
    print("Записать данные в файл\t\t6")
    print("Выход из программы\t\t7")
    print("******************************")


def make_restaurant_order(dishes, numbers_of_dishes, rest_addresses, number_of_restaurant, rest_orders):
    console_dishes = [dishes[number - 1] for number in numbers_of_dishes]
    console_restaurant_order = RestaurantOrder(console_dishes, random.randint(1, 10),
                                               rest_addresses[number_of_restaurant-1])
    rest_orders.append(console_restaurant_order)
    print("Блюда у Вас на столе!")

    print(*[dish.name for dish in console_dishes], sep='\n')
    print("Пришло время заплатить за заказ, Ваш чек:")
    money = console_restaurant_order.price_of_components()
    s = 0
    for name, price in money:
        print(name, price, sep='\t')
        s += price
    print("Итого: ", s, "р.")

    print("Заказ оплачен, спасибо!")


def make_online_market_order(goods, numbers_of_goods, market_addresses, number_of_market, market_orders):

    console_goods = [goods[number - 1] for number in numbers_of_goods]
    console_online_market_order = OnlineMarketOrder(console_goods, market_addresses[number_of_market-1],
                                                    datetime(2023, 10, random.randint(1, 15), 15))
    market_orders.append(console_online_market_order)

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


def show_all_rest_orders(rest_orders):
    if rest_orders:
        for rest_order in rest_orders:
            print(rest_order)
    else:
        print("Нет заказов в ресторанах!")


def show_all_market_orders(market_orders):
    if market_orders:
        for market_order in market_orders:
            print(market_order)
    else:
        print("Нет заказов на онлайн маркете!")


def load_data(file_name):

    load_dishes, load_goods, load_rest_addresses, load_delivery_addresses = [], [], [], []
    load_rest_orders, load_market_orders = [], []
    try:
        with open(file_name, 'rb') as file:
            try:
                cnt_dishes = pickle.load(file)
                for _ in range(cnt_dishes):
                    load_dishes.append(pickle.load(file))
            except Exception:
                raise LoadDishesError("Ошибка загрузки блюд!")
            try:
                cnt_goods = pickle.load(file)
                for _ in range(cnt_goods):
                    load_goods.append(pickle.load(file))
            except Exception:
                raise LoadGoodsError("Ошибка загрузки товаров!")
            try:
                cnt_rest_addresses = pickle.load(file)
                for _ in range(cnt_rest_addresses):
                    load_rest_addresses.append(pickle.load(file))
            except Exception:
                raise LoadRestAddressesError("Ошибка загрузки адресов ресторанов!")
            try:
                cnt_delivery_addresses = pickle.load(file)
                for _ in range(cnt_delivery_addresses):
                    load_delivery_addresses.append(pickle.load(file))
            except Exception:
                raise LoadMarketAddressesError("Ошибка загрузки адресов пунктов выдачи!")
            try:
                cnt_rest_orders = pickle.load(file)
                for _ in range(cnt_rest_orders):
                    load_rest_orders.append(pickle.load(file))
            except Exception:
                raise LoadRestOrdersError("Ошибка загрузки заказов в ресторане!")
            try:
                cnt_market_orders = pickle.load(file)
                for _ in range(cnt_market_orders):
                    load_market_orders.append(pickle.load(file))
            except Exception:
                raise LoadMarketOrdersError("Ошибка загрузки заказов на онлайн маркете!")
            print("Данные загружены из файла успешно!")

    except FileNotFoundError:
        print("Запрашиваемый файл не найден!")
    except (LoadDishesError, LoadGoodsError, LoadRestAddressesError, LoadMarketAddressesError) as e:
        print(e)
    except (LoadRestOrdersError, LoadMarketOrdersError) as e:
        print(e)
    finally:
        return load_dishes, load_goods, load_rest_addresses, load_delivery_addresses, \
            load_rest_orders, load_market_orders


def dump_data(dishes, goods, rest_addresses, market_addresses, rest_orders, market_orders, test=False):
    file_name = "Data.dat" if not test else "Test.dat"
    with open(file_name, 'wb') as output:
        pickle.dump(len(dishes), output)
        for i in range(len(dishes)):
            pickle.dump(dishes[i], output)

        pickle.dump(len(goods), output)
        for i in range(len(goods)):
            pickle.dump(goods[i], output)

        pickle.dump(len(rest_addresses), output)
        for i in range(len(rest_addresses)):
            pickle.dump(rest_addresses[i], output)

        pickle.dump(len(market_addresses), output)
        for i in range(len(market_addresses)):
            pickle.dump(market_addresses[i], output)

        pickle.dump(len(rest_orders), output)
        for i in range(len(rest_orders)):
            pickle.dump(rest_orders[i], output)

        pickle.dump(len(market_orders), output)
        for i in range(len(market_orders)):
            pickle.dump(market_orders[i], output)

        print("Данные записаны в файл успешно!")





