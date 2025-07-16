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


        