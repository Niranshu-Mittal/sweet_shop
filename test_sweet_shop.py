# test_sweet_shop.py
import unittest
from sweet import Sweet
from sweet_shop import SweetShop

# Other Validations used here
class TestSweetValidation(unittest.TestCase):
    def test_invalid_id_type(self):
        with self.assertRaises(ValueError):
            Sweet("abc", "Ladoo", "Dessert", 10.0, 5)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Sweet(1, "   ", "Candy", 10.0, 5)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Sweet(2, "Rasgulla", "Milk", -5.0, 10)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            Sweet(3, "Barfi", "Milk", 20.0, -1)

# Here we are measuring the TestCases
class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.shop = SweetShop()

# Add test
    def test_add_sweet_successfully(self):
        sweet = Sweet(1, "Ladoo", "Festival", 15.0, 10)
        self.shop.add_sweet(sweet)
        self.assertEqual(len(self.shop.sweets), 1)
        self.assertEqual(self.shop.sweets[0].name, "Ladoo")

    def test_add_duplicate_id_raises_error(self):
        sweet1 = Sweet(1, "Ladoo", "Festival", 15.0, 10)
        sweet2 = Sweet(1, "Barfi", "Milk", 12.0, 8)
        self.shop.add_sweet(sweet1)
        with self.assertRaises(ValueError):
            self.shop.add_sweet(sweet2)

# Delete test
    
    def test_delete_existing_sweet(self):
        sweet = Sweet(12, "Jalebi", "Fried", 10.0, 5)
        self.shop.add_sweet(sweet)
        self.shop.delete_sweet(12)
        self.assertEqual(len(self.shop.sweets), 0)


if __name__ == '__main__':
    unittest.main()