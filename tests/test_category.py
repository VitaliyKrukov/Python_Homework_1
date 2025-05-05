def test_category(one_category):
    assert one_category.name == "малина"
    assert one_category.description == "ягоды лесные сборные"
    assert len(one_category.products) == 3

    assert one_category.category_count == 1
    assert one_category.product_count == 3
