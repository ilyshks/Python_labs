from Order import Order
from ProductCard import ProductCard
from datetime import datetime


class OnlineMarketOrder(Order):
    def __init__(self, goods, delivery_point, delivery_date):
        super().__init__(goods)
        self.__check_delivery_point(delivery_point)
        self.__delivery_point = delivery_point
        self.__check_delivery_date(delivery_date)
        self.__delivery_date = delivery_date

    @staticmethod
    def __check_delivery_point(delivery_point):
        if not (isinstance(delivery_point, str) and delivery_point):
            raise ValueError("Адрес пункута выдачи должен быть непустой строкой")

    @staticmethod
    def __check_delivery_date(delivery_date):
        if not isinstance(delivery_date, datetime):
            raise TypeError("Дата доставки должна быть типа datetime")

    @staticmethod
    def __check_components(components):
        if not (isinstance(components, list)):
            raise TypeError("Список товаров должен быть типа list")
        if not all(isinstance(elem, ProductCard) for elem in components):
            raise ValueError("Каждый элемент списка товаров должен быть объектом класса ProductCard")

    @property
    def delivery_point(self):
        return self.__delivery_point

    @property
    def delivery_date(self):
        return self.__delivery_date

    def __sub__(self, other):
        if not isinstance(other, ProductCard):
            return self
        if other in self.components:
            lst = self.components.copy()
            lst.remove(other)
            return OnlineMarketOrder(lst, self.__delivery_point, self.__delivery_date)
        return OnlineMarketOrder(self.components.copy(), self.__delivery_point, self.__delivery_date)

    def __isub__(self, other):
        obj = self - other
        self.components = obj.components
        self.count = obj.count
        return self

    def __str__(self):
        info = f"Номер заказа: {id(self)}\n"
        info += f"Пункт выдачи: {self.__delivery_point}\n"
        info += f"Дата доставки: {self.__delivery_date}\n"
        info += f"Заказ:\n"
        for good in self.components:
            info += str(good) + "\n"
        return info
