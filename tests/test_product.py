from src.product import Product


def test_init_products():
    product_1 = Product("Яблоко", "Зеленое", 60, 2)
    assert product_1.price == 60
    assert product_1.description == "Зеленое"
    assert product_1.name == "Яблоко"
    assert product_1.quantity == 2
