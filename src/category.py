from src.product import Product

class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        if isinstance(product, Product) and product not in self.__products:
            self.__products.append(product)

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def product_list(self):
        return self.__products


# empr1 = Product("name", "description", 12.12, 12)
# empr2 = Product("name", "description", 13.12, 13)
#
# print(empr1)
# print(empr2)
#
# emp1 = Category( "name", "description", [empr1, empr2])
# emp2 = Category( "name", "description", [empr1, empr2])
#
# print(emp1.name)
# print(emp1.description)
# print(emp1.products)
#
# print(emp2.name)
# print(emp2.description)
# print(emp2.products)