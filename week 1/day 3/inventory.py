inventory={}
def add_items():
    name=input("ENTER ITEM NAME: ")
    price=int(input("ENTER PRICE: "))
    quantity=int(input("ENTER QUANTITY: "))

    inventory[name]={
        "price":price,
        "quanity":quantity
    }
def view_items():
    if len(inventory)==0:
        print("NO ITEMS YET")
    else:
        print("\nALL ITEMS")
        for item,info in inventory.items():
            print("\nNAME")
            print("PRICE: {info['phone']}")
            print("QUANTITY: {info['quanity']}")

def update_items():
    name=input("ENTER ITEM NAME TO UPDATE: ").lower()

    if name in inventory:
        new_qty=int(input("ENTER NEW QUANTITY: "))
        inventory[name]["quanitity"]=new_qty
        print("QUANTITY UPDATED")
    else:
        print("ITEM NOT FOUND")

def total_value():
    total=0
    for details in inventory.values():
        total+=details["price"]*details["quantity"]
    print(f"TOTAL INVENTORY VALUE=",total)

while True:
        print("===== SHOP INVENTORY =====")
        print("1. Add item")
        print("2. View items")
        print("3. Update quantity")
        print("4. Total inventory value")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_items()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_items()
        elif choice == "4":
            total_value()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice\n")






