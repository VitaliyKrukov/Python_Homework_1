import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("смородина", "ягода", 20.21, 123)


@pytest.fixture
def two_product():
    return Product("земляника", "ягода", 10.12, 200)


@pytest.fixture
def one_category():
    return Category(
        name="ягоды",
        description="ягоды лесные сборные",
        products=[Product("смородина", "ягода", 20.21, 123), Product("земляника", "ягода", 10.12, 200)],
    )
