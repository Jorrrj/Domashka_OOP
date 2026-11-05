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

    def add_products(self, Product):
        self.__products.append(Product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"Название продукта {product.name}, {product.price} руб., {product.quantity} шт..\n"
        return product_str
