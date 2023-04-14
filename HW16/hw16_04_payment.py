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

    def get_total(self) -> float:
        amount_product: list = []
        for item in range(len(self.products)):
            amount_product.append((self.products[item].price / self.products[item].unit) * self.quantities[item])
        return float((sum(amount_product))/100)


class PaymentValidator:
    def is_valid(self):
        return True if self else False


class PaymentProcessor:
    def purchase(self):
        "Нічого не повертає.Це абстрактний клас для майбутнього використання."


class CashValidator(PaymentValidator):
    def is_valid(self):
        return True


class CodeValidator(PaymentValidator):
    def __init__(self, security_code):
        self.security_code = security_code

    def is_valid(self):
        code_entry = input("Введіть пароль картки ")
        if self.security_code == code_entry:
            return True
        else:
            print("Не вірний пароль")
            return False


class CashPaymentProcessor(CashValidator, PaymentProcessor):
    def purchase(self, cart_shopping):
        print("Обробка готівкового платежу...")
        print("Рахунок у кошику: ", ShoppingCart.get_total(cart_shopping))


class CardPaymentProcessor(CodeValidator, PaymentProcessor):

    def purchase(self, code):
        print("Обробка платежу карткою...")
        self.is_valid()
        print("Код безпеки: ", code)


cart = ShoppingCart()
cart.add_product(Product("juice", 3655, 1), 1)
cash_processor = CashPaymentProcessor()
cash_processor.purchase(cart)  # Cart bill: 36.55
card_processor = CardPaymentProcessor("1234")
card_processor.purchase(cart)  # Security code: 1234
