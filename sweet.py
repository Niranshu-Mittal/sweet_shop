# sweet.py
class Sweet:
    def __init__(self, sweet_id: int, name: str, category: str, price: float, quantity: int):
        if not isinstance(sweet_id, int):
            raise ValueError("Sweet ID must be an integer")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string")

        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")

        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
