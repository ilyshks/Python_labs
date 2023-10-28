class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, price: (int, float)):
        self.check_name(name)
        self.__name = name

        self.check_price(price)
        self.__price = price

    @staticmethod
    def check_name(name):
        if not (isinstance(name, str) and name and name[0].isupper()):
            raise ValueError("Название товара должно быть строкой с заглавной буквы")

    @staticmethod
    def check_price(price):
        if not (isinstance(price, (int, float)) and price > 0):
            raise ValueError("Цена товара должна быть положительным числом")

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __eq__(self, other):
        return isinstance(other, Product) and (self.__name, self.__price) == (other.__name, other.__price)

    def __str__(self):
        return f"{self.name}\t{self.price} р."


class Dish(Product):
    """Класс для представления блюда в ресторане"""

    def __init__(self, name: str, price: (int, float), ingredients: tuple):
        super().__init__(name, price)

        self.__check_ingredients(ingredients)
        self.__ingredients = ingredients

    @staticmethod
    def __check_ingredients(ingredients):
        if not (isinstance(ingredients, tuple) and all(isinstance(elem, str) for elem in ingredients)):
            raise ValueError("Ингредиенты должны быть представлены в виде кортежа строк")

    @property
    def ingredients(self):
        return self.__ingredients

    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, Dish) and self.__ingredients == other.__ingredients

    def __str__(self):
        return f"{self.name}\t{self.price} р.\tСостав: {', '.join(self.__ingredients)}"
