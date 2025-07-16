# sweet_shop.py
class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        if any(s.id == sweet.id for s in self.sweets):
            raise ValueError("Sweet with this ID already exists.")
        self.sweets.append(sweet)
    
