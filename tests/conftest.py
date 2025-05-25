import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
        products=[Product("смородина", "ягода", 20.21, 100), Product("земляника", "ягода", 10.12, 200)],
    )


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def lawngrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def category_without_product():
    return Category(name="ягоды", description="ягоды лесные сборные", products=[])
