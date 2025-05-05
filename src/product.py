class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name if name else ""
        self.description = description if description else ""
        self.__price = price if price else 0
        self.quantity = quantity if quantity else 0

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data.get("name",""),
            description=product_data.get("description",""),
            price=product_data.get("price",0),
            quantity=product_data.get("quantity",0)
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(new_price)


# new_prod = Product.new_product({'name':'l', 'description':'l', 'price':-10, 'quantity':0})
# new_prod.price = -100
# print(new_prod.price)