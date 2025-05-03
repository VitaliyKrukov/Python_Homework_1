class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name if name else ""
        self.description = description if description else ""
        self.price = price if price else 0
        self.quantity = quantity if quantity else 0
