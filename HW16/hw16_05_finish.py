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

    def get_total(self, unit_prod) -> int:
        total_price: float = self.price * unit_prod / self.unit
        return int(total_price)


class ShoppingCart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def __float__(self):
        return self.get_total() / 100

    def __eq__(self, other):
        return isinstance(other, ShoppingCart) and self.products == other.products and\
            self.quantities == other.quantities

    def add_product(self, product, unit_prod) -> None:
        if product not in self.products:
            self.products.append(product)
            self.quantities.append(unit_prod)
        else:
            index = self.products.index(product)
            self.quantities[index] += unit_prod

    def get_total(self) -> int:
        return int(sum(product.get_total(quantity) for product, quantity in self))

    def __len__(self):
        return len(self.products)

    def __getitem__(self, key):
        return self.products[key], self.quantities[key]

    def __iter__(self):
        return zip(self.products, self.quantities)

    def remove_product(self, product) -> None:
        if product in self.products:
            index = self.products.index(product)
            self.products.pop(index)
            self.quantities.pop(index)
        else:
            print("No product")

    def sub_product(self, product, unit_prod) -> None:
        index = self.products.index(product)
        self.quantities[index] -= unit_prod
        if self.quantities[index] <= 0:
            self.remove_product(product)
        else:
            print("No product")


candy = Product("candy", 1059, 0.1)
sweet = Product("candy", 1059, 0.1)
juice = Product("juice", 3655, 1)
cart = ShoppingCart()
cart.add_product(candy, 0.75)
cart.add_product(sweet, 0.75)
cart.add_product(juice, 3)
print(len(cart))
print(cart[0])
for cart_item, purchase in zip(cart, ((candy, 1.5), (juice, 3))):
    print(cart_item == purchase)
cart.remove_product(candy)
print(len(cart))
cart.sub_product(juice, 2)
print(cart[0][1])
cart.sub_product(juice, 2)
print(not cart)


class PaymentValidator:
    def is_valid(self):
        raise NotImplementedError


class PaymentProcessor:
    def purchase(self):
        raise NotImplementedError


class CashValidator(PaymentValidator):
    def is_valid(self):
        return True


class CodeValidator(PaymentValidator):
    def __init__(self, security_code):
        self.security_code = security_code

    def is_valid(self):
        code_entry = input("Введіть пароль картки ")
        return self.security_code == code_entry


class CashPaymentProcessor(CashValidator, PaymentProcessor):
    def purchase(self, cart_shopping):
        if self.is_valid():
            print("Обробка готівкового платежу...")
            print("Рахунок у кошику: ", ShoppingCart.get_total(cart_shopping))
        else:
            print("Пуста корзина")


class CardPaymentProcessor(CodeValidator, PaymentProcessor):
    def purchase(self, code):
        if self.is_valid():
            print("Обробка платежу карткою...")
            print("Код безпеки: ", code)
        else:
            print("Не вірний код")


cart = ShoppingCart()
cart.add_product(Product("juice", 3655, 1), 1)
cash_processor = CashPaymentProcessor()
cash_processor.purchase(cart)  # Cart bill: 36.55
card_processor = CardPaymentProcessor("1234")
card_processor.purchase(cart)  # Security code: 1234
