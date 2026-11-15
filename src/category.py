from src.product import Product


class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self):
        full_quantity_products = 0
        for product in self.__products:
            full_quantity_products += product.quantity
        return f"Название категории {self.name}, количество продуктов: {full_quantity_products} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Данные не относятся к классу продуктов")

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 1)
        except ZeroDivisionError:
            return 0
