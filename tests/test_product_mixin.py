from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_product(capsys):
    Product("смородина", "ягода", 20.21, 123)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(смородина, ягода, 20.21, 123)"

def test_smartphone(capsys):
    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

def test_lawngrass(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"