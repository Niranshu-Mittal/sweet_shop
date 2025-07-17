# app.py
from src.sweet_shop import SweetShop
from src.sweet import Sweet

shop = SweetShop()

def print_menu():
    print("\n==== Sweet Shop Menu ====")
    #For Adding Sweets
    print("1. Add Sweet")
    print("2. Delete Sweet")
    print("3. View Sweets")
    print("4. Search Sweet")
    print("5. Sort Sweets")
    print("6. Purchase Sweet")
    print("7. Restock Sweet")
    print("8. Exit")
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            sid_input = input("ID: ")
            if not sid_input.isdigit():
                raise ValueError("ID must be a valid integer.")
            sid = int(sid_input)
            name = input("Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            sweet = Sweet(sid, name, category, price, qty)
            shop.add_sweet(sweet)
            print("Sweet added!")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Here the sweets would be deleted by the user
    elif choice == "2":
        try:
            sid = input("ID to delete: ")
            if not sid.isdigit():
                raise ValueError("ID must be an integer.")
            shop.delete_sweet(int(sid))
            print("Deleted (if it existed).")
        except ValueError as e:
            print(f"Error: {e}")
    
    #Here we are going to view sheets

    elif choice == "3":
        sweets = shop.view_sweets()
        for s in sweets:
            print(f"{s.id} | {s.name} | {s.category} | ₹{s.price} | Qty: {s.quantity}")
    

    # Here we are going to add search funcitonality

    elif choice == "4":
        name = input("Search name")
        category = input("Category")
        min_price = input("Min price")
        max_price = input("Max price")
        results = shop.search(
            name=name or None,
            category=category or None,
            price_range=(
                float(min_price) if min_price else 0,
                float(max_price) if max_price else float('inf')
            ) if min_price or max_price else None
        )
        for s in results:
            print(f"{s.id} | {s.name} | {s.category} | ₹{s.price} | Qty: {s.quantity}")

# Sorting according to the name, Price, Quantity
    elif choice == "5":
        print("Sort by:")
        print("1. Name")
        print("2. Price")
        print("3. Quantity")
        sort_choice = input("Choose sort key: ")

        key_map = {"1": "name", "2": "price", "3": "quantity"}
        key = key_map.get(sort_choice)
        if not key:
            print("Invalid sort option.")
            continue

        order = input("Sort descending? (y/n): ")
        reverse = order.lower() == 'y'

        try:
            sorted_sweets = shop.sort_sweets(key=key, reverse=reverse)
            for s in sorted_sweets:
                print(f"{s.id} | {s.name} | {s.category} | ₹{s.price} | Qty: {s.quantity}")
        except ValueError as e:
            print(f"Error: {e}")

# Purchase or Inventory
    elif choice == "6":
        try:
            sid = input("Sweet ID: ")
            if not sid.isdigit():
                raise ValueError("ID must be a valid integer.")
            qty = int(input("Quantity to buy: "))
            shop.purchase(int(sid), qty)
            print("Purchase successful.")
        except ValueError as e:
            print(f"Error: {e}")
    
# Restock 
    elif choice == "7":
        try:
            sid = input("Sweet ID: ")
            if not sid.isdigit():
                raise ValueError("ID must be a valid integer.")
            qty = int(input("Quantity to restock: "))
            shop.restock(int(sid), qty)
            print("Restocked.")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "8":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice.")