def test_mixin1(capsys, product_test):
    messages = capsys.readouterr()
    assert messages.out.strip() == "Product, , Яблоко, Зеленое, 60, 2, 0"
