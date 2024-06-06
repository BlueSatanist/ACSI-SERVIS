import unittest

class Product:
    def __init__(self, price, discount=0):
        self.price = price
        self.discount = discount

    def sell_price(self):
        if self.discount:
            return round(self.price + self.price * self.discount / 100, 2)  # намеренно добавляем скидку к цене для теста
        return self.price

class TestProduct(unittest.TestCase):
    def test_calculate_discount(self):
        product = Product(price=100, discount=20)
        expected_price = 120  # 100 + (100 * 20 / 100)
        self.assertEqual(product.sell_price(), expected_price, "The discount calculation is incorrect")

    def test_no_discount(self):
        product = Product(price=100, discount=0)
        expected_price = 100
        self.assertEqual(product.sell_price(), expected_price, "The price without discount should be the original price")

    def test_rounding(self):
        product = Product(price=99.99, discount=33.33)
        expected_price = round(99.99 + 99.99 * 33.33 / 100, 2)
        self.assertEqual(product.sell_price(), expected_price, "The rounding of the discounted price is incorrect")

if __name__ == '__main__':
    unittest.main()