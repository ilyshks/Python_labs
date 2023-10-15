from Product import Product


class ProductCard(Product):
    """Класс для представления товара на маркетплейсе"""

    def __init__(self, name: str, price: (int, float), item_number: (None, str) = None):
        super().__init__(name, price)
        if item_number is None:
            self.__item_number = str(id(self))
        else:
            self.check_item_number(item_number)
            self.__item_number = item_number

    @staticmethod
    def check_item_number(item_number):
        if not (isinstance(item_number, str)):
            raise TypeError("Артикул товара должен быть строкой")

    @property
    def item_number(self):
        return self.__item_number

    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, ProductCard) and self.__item_number == other.__item_number
