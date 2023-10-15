from Order import Order
from Dish import Dish


class RestaurantOrder(Order):
    def __init__(self, dishes, table_number, address):
        super().__init__(dishes)
        self.__check_table_number(table_number)
        self.__table_number = table_number
        self.__check_address(address)
        self.__address = address

    @staticmethod
    def __check_table_number(table_number):
        if not (isinstance(table_number, int) and table_number > 0):
            raise ValueError("Номер столика должен быть целым положительным числом")

    @staticmethod
    def __check_address(address):
        if not isinstance(address, str):
            raise TypeError("Адрес ресторана должен быть строкой")

    @staticmethod
    def __check_components(components):
        if not (isinstance(components, list)):
            raise TypeError("Список блюд должен быть типа list")
        if not all(isinstance(elem, Dish) for elem in components):
            raise ValueError("Каждый элемент списка блюд должен быть объектом класса Dish")

    @property
    def table_number(self):
        return self.__table_number

    @property
    def address(self):
        return self.__address

    def __sub__(self, other):
        if not isinstance(other, Dish):
            return self
        if other in self.components:
            lst = self.components.copy()
            lst.remove(other)
            return RestaurantOrder(lst, self.__table_number, self.__address)
        return RestaurantOrder(self.components.copy(), self.__table_number, self.__address)

    def __isub__(self, other):
        obj = self - other
        self.components = obj.components
        self.count = obj.count
        return self

    def is_equal(self, other) -> bool:
        """Проверяет объекты на равенство полей"""

        if not isinstance(other, RestaurantOrder) or self.count != other.count:
            return False
        for i in range(self.count):
            if self.components[i] != other.components[i]:
                return False
        if not (self.__table_number == other.__table_number and self.__address == other.__address):
            return False
        return True

    def __str__(self):
        info = f"Адрес ресторана: {self.__address}\n"
        info += f"Номер столика: {self.__table_number}\n"
        info += f"Заказ:\n"
        for dish in self.components:
            info += str(dish) + "\n"
        return info

