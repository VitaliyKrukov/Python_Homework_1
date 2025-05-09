from typing import Any


class Product:
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
        self.quantity = quantity if quantity else 0

    def __str__(self) -> str:
        """Создали пользовательский вывод"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Any:
        """Создали метод вычисления"""
        if isinstance(other, Product):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            return TypeError

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
