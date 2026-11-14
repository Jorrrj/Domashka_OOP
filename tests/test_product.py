from src.product import Product


def test_init_products(product_2):
    product_1 = Product("Яблоко", "Зеленое", 60, 2)
    assert product_1.price == 60
    assert product_1.description == "Зеленое"
    assert product_1.name == "Яблоко"
    assert product_1.quantity == 2
    product_1.price = 70
    assert product_1.price == 70
    product_1.price = -10
    assert product_1.price == 70
    red_product = Product.new_product(product_2)
    assert red_product.name == "Банан"
    product_2 = Product("Мандарин", "Сладкий", 120, 5)
    assert product_1 + product_2 == 740
