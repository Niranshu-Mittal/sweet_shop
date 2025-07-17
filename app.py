# app.py
from sweet_shop import SweetShop
from sweet import Sweet

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
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        #Here the sweets would be given by the user
        sid = int(input("Sweet ID: "))
        name = input("Sweet Name: ")
        category = input("Sweet Category: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        sweet = Sweet(sid, name, category, price, qty)
        try:
            shop.add_sweet(sweet)
            print("Sweet added sucessfully")
        except ValueError as e:
            print(f"Error: {e}")

    # Here the sweets would be deleted by the user
    elif choice == "2":
        sid = int(input("ID to delete: "))
        try:
            shop.delete_sweet(sid)
            print("Sweet deleted.")
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
        sid = int(input("Sweet ID: "))
        qty = int(input("Quantity to buy: "))
        try:
            shop.purchase(sid, qty)
            print("Purchase successful.")
        except ValueError as e:
            print(f"Error: {e}")
    