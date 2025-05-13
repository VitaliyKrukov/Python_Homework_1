from src.product import Product


class Category:
    """Создали класс категорий"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0
    sum_quantity = 0

    def __init__(self, name, description, products):
        """Создали конструкцию категорий"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def sum_quantity_products(self):
        """Вычисляет общее количество товаров (штук) в категории"""
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        """Создали пользовательский вывод"""
        return f"{self.name}, количество продуктов: {self.sum_quantity_products} шт."

    def add_product(self, product):
        """Добавляем по одному уникальному продукту в список"""
        if not isinstance(product, Product) or product in self.__products:
            raise TypeError
        else:
            self.__products.append(product)
            Category.product_count += 1


    @property
    def products(self):
        """Создали цикл, который добавляет строковые элементы"""
        products_str = ""
        for product in self.__products:
            products_str += str(product)
        return products_str

    @property
    def product_list(self):
        """Создали вызеваемость приватного параметра"""
        return self.__products
