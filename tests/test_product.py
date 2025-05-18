import pytest

from src.product import Product


def test_product(product):
    assert product.name == "смородина"
    assert product.description == "ягода"
    assert product.price == 20.21
    assert product.quantity == 123


def test_new_product_dict():
    new_product = Product.new_product_dict({"name": "Яблоко", "description": "фрукт", "price": 10.10, "quantity": 100})
    assert new_product.name == "Яблоко"
    assert new_product.description == "фрукт"
    assert new_product.price == 10.10
    assert new_product.quantity == 100


def test_price_setter(product, capsys):
    product.price = -10
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"
    product.price = 10
    assert product.price == 10


def test_add_product(product, two_product):
    assert product + two_product == 4509.83
    with pytest.raises(TypeError):
        product + "не продукт"


def test_str_user(product):
    assert str(product) == "смородина, 20.21 руб. Остаток: 123 шт."
