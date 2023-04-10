class Product:
    name: str = 'unknown'
    price: int = 0
    unit: int = 1

    def get_total(self, unit_prod=unit) -> int:
        total_price = self.price * unit_prod / self.unit
        return int(total_price)


product1 = Product()
product1.name = 'apple'
product1.price = 20
product1.unit = 3
product2 = Product()
product2.name = 'orange'
product2.price = 10
product2.unit = 5
print(product1.get_total(10))
print(product2.get_total())
