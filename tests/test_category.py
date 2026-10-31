from src.category import Category


def test_init_category(category_1):
    category = Category("Фрукты", "Сезонные", category_1)
    assert category.name == "Фрукты"
    assert category.description == "Сезонные"
    assert category.products[0].name == "Банан"
    assert Category.category_count == 1
    assert Category.product_count == 2
