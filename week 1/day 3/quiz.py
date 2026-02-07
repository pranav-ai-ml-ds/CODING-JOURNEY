expenses=[]
categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]

def add_expense():
    print("\n ===ADD EXPENSE=== ")
    for i,cat in enumerate(categories):
        print(f"{i+1}.{cat}")
    cat_choice=int(input("CHOOSE CATEGORY(1-6):"))-1
    category=categories[cat_choice]
    amount=float(input("ENTER AMMOUNT: "))
    description=input("ENTER DESCRIPTION: ")
    
    expense = {
    "category": category,
    "amount": amount,
    "description": description
   }
    expenses.append(expense)
    print("EXPENSE ADDED")

def view_all_expenses():
   if len(expenses) == 0:
    print("\nNo expenses yet!")
    return
print("\n=== ALL EXPENSES ===")
total = 0

for i, exp in enumerate(expenses):
    print(f"\n{i+1}. {exp['description']}")
    print(f"   Category: {exp['category']}")
    print(f"   Amount: ₹{exp['amount']:.2f}")
    total += exp['amount']

print(f"\nTotal Spending: ₹{total:.2f}")