import pytest

from src.product import Product


@pytest.fixture
def category_1():
    p1 = Product("Банан", "Спелый", 55, 8)
    p2 = Product("Яблоко", "Зеленое", 60, 2)
    list_product = [p1, p2]
    return list_product
