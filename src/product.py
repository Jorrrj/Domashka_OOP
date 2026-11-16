from src.base_class import BaseProduct
from src.mixin import MixinPrint


class Product(BaseProduct, MixinPrint):
    name: str
    description: str
    price: int
    quantity: int
    full_price: int

    def __init__(self, name, description, price, quantity, full_price=0):
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        self.full_price = full_price
        super().__init__()

    def __str__(self):
        return f"Название продукта {self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Нельзя складывать разные типы данных")

    @classmethod
    def new_product(cls, product_dict):
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    efficiency: int
    model: int
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color, full_price=0):
        super().__init__(name, description, price, quantity, full_price)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color, full_price=0):
        super().__init__(name, description, price, quantity, full_price)
        self.country = country
        self.germination_period = germination_period
        self.color = color
