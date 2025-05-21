import pytest

from src.product import Product


def test_category(one_category):
    assert one_category.name == "ягоды"
    assert one_category.description == "ягоды лесные сборные"

    assert one_category.category_count == 1
    assert one_category.product_count == 2


def test_category_property(one_category):
    assert one_category.products == ("смородина, 20.21 руб. Остаток: 123 шт." "земляника, 10.12 руб. Остаток: 200 шт.")


def test_category_add_product(one_category):
    one_category.add_product(Product("ежевика", "ягода", 20.20, 12))
    assert len(one_category.product_list) == 3
    with pytest.raises(TypeError):
        one_category.add_product("")


def test_category_str_user(one_category):
    assert str(one_category) == "ягоды, количество продуктов: 323 шт."


def test_sum_quantity(one_category):
    """Тест вычисления общего количества товаров"""
    assert one_category.sum_quantity_products == 323
