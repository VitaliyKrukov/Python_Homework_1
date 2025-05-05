import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("смородина", "ягода", 20.21, 123)


@pytest.fixture
def one_category():
    return Category(name="малина", description="ягоды лесные сборные", products=["вишня", "малина", "земляника"])
