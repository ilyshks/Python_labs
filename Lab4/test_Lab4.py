from datetime import datetime

import pytest
import functions
import pickle
from Dish import Dish
from ProductCard import ProductCard
from contextlib import nullcontext as does_not_raise

from OnlineMarketOrder import OnlineMarketOrder
from RestaurantOrder import RestaurantOrder


@pytest.fixture(autouse=True)
def used_data():
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

    return dishes, goods, addresses_of_restaurants, addresses_of_delivery_points, restaurant_orders, market_orders


@pytest.fixture(scope="module")
def empty_file():
    yield
    with open("Test.dat", "wb") as file:
        for _ in range(6):
            pickle.dump(0, file)


@pytest.fixture
def full_file(used_data):
    dishes, goods, rest_addresses, market_addresses, rest_orders, market_orders = used_data
    with open("Test.dat", 'wb') as output:
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


@pytest.mark.parametrize(
    "file_name, result",
    [
        ("Smth.txt", (0, )*6),
        ("Test.txt", (0, )*6),
        ("Test.dat", (5, 5, 4, 4, 0, 0)),
    ]
)
def test_load_data(file_name, result, full_file):
    data = functions.load_data(file_name)
    for i, elem in enumerate(data):
        assert len(elem) == result[i]


@pytest.mark.parametrize(
    "numbers_of_dishes, number_of_restaurant",
    [
        ([1, 4, 3], 1),
        ([2], 2),
        ([1, 2, 3, 3, 3], 3),
    ]
)
def test_make_restaurant_order(numbers_of_dishes, number_of_restaurant):
    dishes, goods, rest_addresses, market_addresses, rest_orders, market_orders = used_data
    old_length = len(rest_orders)
    functions.make_restaurant_order(dishes, numbers_of_dishes, rest_addresses, number_of_restaurant, rest_orders)
    new_length = len(rest_orders)
    assert new_length - old_length == 1


@pytest.mark.parametrize(
    "numbers_of_goods, number_of_market",
    [
        ([1, 2, 3], 1),
        ([1], 2),
        ([1, 2, 3, 4, 5], 3),
    ]
)
def test_make_online_market_order(numbers_of_goods, number_of_market):
    dishes, goods, rest_addresses, market_addresses, rest_orders, market_orders = used_data
    old_length = len(market_orders)
    functions.make_online_market_order(goods, numbers_of_goods, market_addresses, number_of_market, market_orders)
    new_length = len(market_orders)
    assert new_length - old_length == 1


@pytest.mark.parametrize(
    "rest_orders, result, expectation",
    [
        ([], None, does_not_raise()),
        ([RestaurantOrder([Dish("Салат", 500, ("Помидоры", "Огурцы", "Оливковое масло"))], 10,
                          "Волков пер., 9, стр. 1")], None, does_not_raise()),
        (1, None, pytest.raises(TypeError)),
    ]
)
def test_show_all_rest_orders(rest_orders, result, expectation):
    with expectation:
        assert functions.show_all_rest_orders(rest_orders) == result


@pytest.mark.parametrize(
    "rest_orders, result, expectation",
    [
        ([], None, does_not_raise()),
        ([OnlineMarketOrder([ProductCard("Часы", 10000)], "Мещанская ул., 14", datetime(2023, 10, 3, 15))],
         None, does_not_raise()),
        (1, None, pytest.raises(TypeError)),
    ]
)
def test_show_all_market_orders(rest_orders, result, expectation):
    with expectation:
        assert functions.show_all_market_orders(rest_orders) == result


def test_dump_data():
    dishes, goods, rest_addresses, market_addresses, rest_orders, market_orders = used_data
    assert functions.dump_data([], [], [], [], [], [], True) is None
    assert functions.dump_data(dishes, goods, rest_addresses, market_addresses, rest_orders, market_orders, True) is None


