# sweet_shop.py
import sweet as Sweet
class SweetShop:
    def __init__(self):
        self.sweets = []
# Add Implementation
    def add_sweet(self, sweet):
        if any(s.id == sweet.id for s in self.sweets):
            raise ValueError("Sweet with this ID already exists.")
        self.sweets.append(sweet)

# Delete Implementation
    def delete_sweet(self, sweet_id):
        initial_count = len(self.sweets)
        self.sweets = [s for s in self.sweets if s.id != sweet_id]
        if len(self.sweets) == initial_count:
            raise ValueError("Sweet not found for deletion.")
        
# View Implementation
    def view_sweets(self):
        return self.sweets
    
# Search implementation

    def search(self, name=None, category=None, price_range=None):
        results = self.sweets
        if name:
            results = [s for s in results if name.lower() in s.name.lower()]
        if category:
            results = [s for s in results if category.lower() in s.category.lower()]
        if price_range:
            min_price, max_price = price_range
            results = [s for s in results if min_price <= s.price <= max_price]
        return results
    
# Sort with Name, Price, Quantity Implementation 

    def sort_sweets(self, key="name", reverse=False):
        valid_keys = {"name", "price", "quantity"}
        if key not in valid_keys:
            raise ValueError("Invalid sort key. Use 'name', 'price', or 'quantity'.")
        return sorted(self.sweets, key=lambda s: getattr(s, key), reverse=reverse)

# Purchase order implementation
    def purchase(self, sweet_id, quantity):
        for s in self.sweets:
            if s.id == sweet_id:
                if s.quantity < quantity:
                    raise ValueError("Not enough stock")
                s.quantity -= quantity
                return
        raise ValueError("Sweet not found")
    
# Restock
    def restock(self, sweet_id, quantity):
        for s in self.sweets:
            if s.id == sweet_id:
                s.quantity += quantity
                return
        raise ValueError("Sweet not found")