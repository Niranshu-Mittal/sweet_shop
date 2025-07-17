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

# View test for sweets
    def test_view_sweets(self):
            s1 = Sweet(13, "Ladoo", "Festival", 15.0, 10)
            s2 = Sweet(14, "Kaju Katli", "Nut", 25.0, 5)
            self.shop.add_sweet(s1)
            self.shop.add_sweet(s2)
            sweets = self.shop.view_sweets()
            self.assertEqual(len(sweets), 2)
            self.assertEqual(sweets[0].name, "Ladoo")
            self.assertEqual(sweets[1].name, "Kaju Katli")

# Search test for sweets
    def test_search_by_name(self):
        self.shop.add_sweet(Sweet(20, "Ladoo", "Festival", 10, 5))
        self.shop.add_sweet(Sweet(21, "Barfi", "Milk", 20, 10))
        results = self.shop.search(name="ladoo")
        self.assertEqual(len(results), 1)

    def test_search_by_category(self):
        self.shop.add_sweet(Sweet(22, "Barfi", "Milk", 20, 10))
        results = self.shop.search(category="Milk")
        self.assertEqual(len(results), 1)

    def test_search_by_price_range(self):
        self.shop.add_sweet(Sweet(23, "Ladoo", "Festival", 10, 5))
        self.shop.add_sweet(Sweet(24, "Barfi", "Milk", 20, 10))
        results = self.shop.search(price_range=(15, 25))
        self.assertEqual(len(results), 1)

# Sort test for arranging sweets by name, price,quantity
    def test_sort_by_name(self):
        self.shop.add_sweet(Sweet(30, "Gulab Jamun", "Milk", 30, 10))
        self.shop.add_sweet(Sweet(31, "Barfi", "Milk", 25, 10))
        sorted_sweets = self.shop.sort_sweets(key="name")
        self.assertEqual([s.name for s in sorted_sweets], ["Barfi", "Gulab Jamun"])

    def test_sort_by_price_descending(self):
        self.shop.add_sweet(Sweet(32, "Barfi", "Milk", 20, 10))
        self.shop.add_sweet(Sweet(33, "Gulab Jamun", "Milk", 30, 10))
        sorted_sweets = self.shop.sort_sweets(key="price", reverse=True)
        self.assertEqual([s.price for s in sorted_sweets], [30, 20])

# Purchase or Inventory test
    def test_purchase_success(self):
        sweet = Sweet(40, "Ladoo", "Festival", 15.0, 10)
        self.shop.add_sweet(sweet)
        self.shop.purchase(40, 3)
        self.assertEqual(self.shop.sweets[0].quantity, 7)

    def test_purchase_insufficient_stock(self):
        sweet = Sweet(41, "Ladoo", "Festival", 15.0, 2)
        self.shop.add_sweet(sweet)
        with self.assertRaises(ValueError):
            self.shop.purchase(41, 5)

if __name__ == '__main__':
    unittest.main()