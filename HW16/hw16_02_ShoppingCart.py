class Product:
    name: str = 'unknown'
    price: int = 0
    unit: float = 0.1

    def get_total(self, unit_prod=unit) -> int:
        total_price: float = self.price * unit_prod / self.unit
        return int(total_price)


class ShoppingCart:
    products: list = []
    quantities: list = []

    def add_product(self, product, unit_prod=1) -> None:
        if unit_prod is None:
            unit_prod = product.unit
        self.products.append(product)
        self.quantities.append(unit_prod)

    def get_total(self) -> int:
        total_prod: list = []
        for i in range(len(self.products)):
            total_prod.append((self.products[i].price / self.products[i].unit) * self.quantities[i])
        return int(sum(total_prod))


product_obj = Product()
product_obj.name = "juice"
product_obj.price = 3655
product_obj.unit = 1
cart_obj = ShoppingCart()
cart_obj.add_product(product_obj, 3)  # put 3 packs of juice to cart
cart_obj.add_product(product_obj)     # add one more (unit = 1)
cart_obj.get_total()           # == 14620 , 3655 x 4
