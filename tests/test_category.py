from src.category import Category
from src.product import Product


def test_init_category(category_1, category_2, category_3):
    category = Category("Фрукты", "Сезонные", category_1)
    assert str(category) == "Название категории Фрукты, количество продуктов: 10 шт."
    assert category.name == "Фрукты"
    assert category.description == "Сезонные"
    assert category.products == category_2
    assert Category.category_count == 1
    assert Category.product_count == 2
    product = Product("Мандарин", "Сладкий", 50, 30)
    category.add_product(product)
    assert category.products == category_3
