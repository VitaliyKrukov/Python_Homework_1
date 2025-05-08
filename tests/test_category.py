from src.product import Product


def test_category(one_category):
    assert one_category.name == "малина"
    assert one_category.description == "ягоды лесные сборные"

    assert one_category.category_count == 1
    assert one_category.product_count == 1

def test_category_property(one_category):
    assert one_category.products == 'смородина, 20.21 руб. Остаток: 123 шт.\n'

def test_category_add_product(one_category):
    one_category.add_product(Product("ежевика", "ягода", 20.20, 12))
    assert len(one_category.product_list) == 2

