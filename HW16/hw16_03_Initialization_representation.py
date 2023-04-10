class Product:

    def __init__(self, name, price, unit):
        self.name = name
        self.price = price
        self.unit = unit

    def __str__(self):
        return self.name

    def __float__(self):
        return self.price / 100

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name and\
            self.price == other.price and self.unit == other.unit

    def __ne__(self, other):
        return isinstance(other, Product) and self.name != other.name and\
            self.price != other.price and self.unit != other.unit

    def get_total(self, unit_prod) -> int:
        total_price: float = self.price * unit_prod / self.unit
        return int(total_price)


class ShoppingCart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def __float__(self):
        return self.get_total() / 100

    def __bool__(self):
        return True if self.products is None else False

    def __eq__(self, other):
        return isinstance(other, ShoppingCart) and self.products == other.products and\
            self.quantities == other.quantities

    def __ne__(self, other):
        return isinstance(other, ShoppingCart) and self.products != other.products and\
            self.quantities != other.quantities

    def add_product(self, product, unit_prod: float = 1) -> None:
        if unit_prod is None:
            unit_prod = product.unit
        self.products.append(product)
        self.quantities.append(unit_prod)

    def get_total(self) -> int:
        amount_product: list = []
        for item in range(len(self.products)):
            amount_product.append((self.products[item].price / self.products[item].unit) * self.quantities[item])
        return int(sum(amount_product))


candy = Product("candy", 1059, 0.1)
sweet = Product("candy", 1059, 0.1)
juice = Product("juice", 3655, 1)
cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_product(candy, 1)
cart_1.add_product(sweet, 0.5)
cart_2.add_product(juice)
assert cart_1.get_total()          # == 15885
assert str(candy)                  # == "candy"
assert float(candy)                # == 10.59
assert float(cart_2)               # == 36.55
assert candy == sweet
assert sweet != juice
