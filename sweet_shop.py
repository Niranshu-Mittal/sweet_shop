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