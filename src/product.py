from src.base_product import BaseProduct
from src.product_mixin import ProductMixin


class Product(BaseProduct, ProductMixin):
    """Создали класс продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Создали конструкцию класса продуктов"""
        self.name = name if name else ""
        self.description = description if description else ""
        self.__price = price if price else 0
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        """Создали пользовательский вывод"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Создали метод вычисления"""
        if isinstance(self, type(other)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_data):
        """создали класс-метод для работы со словарями"""
        return cls(
            name=product_data.get("name", ""),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0),
            quantity=product_data.get("quantity", 0),
        )

    @property
    def price(self):
        """Создали вызов приватного параметра"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """создали проверку на отрицательные числа и 0"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(new_price)
