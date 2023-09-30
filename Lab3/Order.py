class Order:
    """Родительский класс для представления заказов"""

    __VAT_rate = 1.2  # ставка НДС

    def __init__(self, components: list) -> None:
        self.__check_components(components)
        self.__components = components[:]  # состав заказа
        self.__count = len(components)  # кол-во товаров

    @staticmethod
    def __check_components(components):
        if not (isinstance(components, list)):
            raise TypeError("Список продуктов должен быть типа list")

    def is_equal(self, other) -> bool:
        """Проверяет объекты на равенство полей"""

        if not isinstance(other, Order) or self.__count != other.__count:
            return False
        for i in range(self.__count):
            if self.__components[i] != other.__components[i]:
                return False
        return True

    def price_of_components(self) -> list:
        """Возвращает информацию о стоимости всех товаров в заказе с учётом НДС"""

        return [(product.name, product.price * self.__VAT_rate) for product in self.__components]

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, new_components):
        self.__check_components(new_components)
        self.__components = new_components[:]

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if not (isinstance(count, int) and count >= 0):
            raise ValueError("Кол-во товаров в заказе должно быть целым неотрицательным числом")
        self.__count = count
