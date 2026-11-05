class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
