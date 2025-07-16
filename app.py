# app.py
from sweet_shop import SweetShop
from sweet import Sweet

shop = SweetShop()

def print_menu():
    print("\n==== Sweet Shop Menu ====")
    #For Adding Sweets
    print("1. Add Sweet")

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
        