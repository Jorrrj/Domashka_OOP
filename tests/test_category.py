from src.category import Category


def test_init_category(category_1):
    category = Category("Фрукты", "Сезонные", category_1)
    assert category.name == "Фрукты"
    assert category.description == "Сезонные"
    assert category.products[0].name == "Банан"
    assert Category.count_category == 1
    assert Category.count_products == 2
