class Product:
    name: str
    description: str
    price: int
    quantity: int
    full_price: int

    def __init__(self, name, description, price, quantity, full_price=0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.full_price = full_price

    def __str__(self):
        return f"Название продукта {self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)

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
