import pytest

from src.product import Product


@pytest.fixture
def category_1():
    p1 = Product("Банан", "Спелый", 55, 8)
    p2 = Product("Яблоко", "Зеленое", 60, 2)
    list_product = [p1, p2]
    return list_product


@pytest.fixture
def category_2():
    return "Название продукта Банан, 55 руб. Остаток: 8 шт.\nНазвание продукта Яблоко, 60 руб. Остаток: 2 шт.\n"


@pytest.fixture
def product_2():
    return {"name": "Банан", "description": "Спелый", "price": 55, "quantity": 8}


@pytest.fixture
def category_3():
    return "Название продукта Банан, 55 руб. Остаток: 8 шт.\nНазвание продукта Яблоко, 60 руб. Остаток: 2 шт.\nНазвание продукта Мандарин, 50 руб. Остаток: 30 шт.\n"
