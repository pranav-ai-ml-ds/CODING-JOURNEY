contacts={}
def add_contacts():
    name=input("ENTER NAME: ")
    phone=input("ENTER PHONE: ")
    email=input("ENTER EMAIL:")

    contacts[name]={
        "phone":phone,
        "email":email
    }
    print("CONTACT ADDDED")

def view_contacts():
    if len(contacts)==0:
        print("NO CONTACTS ADDED")
    else:
        print("\n===ALL CONTACTS")
        for name,info in contacts.items():
                print(f"\nNAME: ")
                print(f"PHONE: {info['phone']}")
                print(f"EMAIL: {info['email']}")
def search_contact():
     name=input("ENTER NAME TO SEARCH")
     if name in contacts:
          print(f"\nNAME: {name}")
          print(f"PHONE: {contacts[name]['phone']}")
          print(f"EMAIL: {contacts[name]['email']}")
     else:
          print("CONTACT NOT FOUND")

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Exit")

    choice=input("ENTER CHOICE: ")

    if choice=="1":
         add_contacts()
    elif choice=="2":
         view_contacts()
    elif choice=="3":
         search_contact()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
    





