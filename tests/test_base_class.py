import pytest

from src.base_class import BaseProduct


def test_base_class():
    class Test(BaseProduct):
        def __init__(self, name, price):
            self.name = name
            self.price = price

        @classmethod
        def new_product(cls, dict_test):
            return cls(dict_test["name"], dict_test["price"])

    test1 = Test.new_product({"name": "Домашка", "price": 5})
    assert test1.name == "Домашка"


def test_base_error():
    class Test(BaseProduct):
        def __init__(self, name, price):
            self.name = name
            self.price = price

    with pytest.raises(TypeError):
        Test("Домашка", 5)
