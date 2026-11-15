import pytest

from src.product import LawnGrass, Product, Smartphone


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
    with pytest.raises(ValueError):
        Product("Яблоко", "Зеленое", 60, 0)


def test_init_subsidiary_class():
    smartphone1 = Smartphone("Nokia", "Быстрый", 5600, 2, 70, 206, 64, "Черный")
    assert smartphone1.price == 5600
    lawnGrass = LawnGrass("Газонная трава", "Густая", 8000, 2, "Россия", 8, "Зеленая")
    assert lawnGrass.price == 8000
    smartphone2 = Smartphone("Aple", "Шустрый", 9500, 5, 70, 206, 64, "Черный")
    assert smartphone2 + smartphone1 == 58700
    with pytest.raises(TypeError):
        smartphone1 + lawnGrass
