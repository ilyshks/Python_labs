from Product import Product


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
