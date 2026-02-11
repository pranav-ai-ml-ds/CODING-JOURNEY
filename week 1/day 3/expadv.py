import csv
from datetime import datetime
import os

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Categories and their monthly budgets
CATEGORIES = {
    "Food": 5000,
    "Transport": 2000,
    "Entertainment": 3000,
    "Shopping": 4000,
    "Bills": 6000,
    "Other": 2000
}

def load_expenses():
    """Load expenses from CSV file"""
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    return expenses

def save_expense(expense):
    """Save a single expense to CSV"""
    file_exists = os.path.exists(EXPENSE_FILE)
    
    with open(EXPENSE_FILE, 'a', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(expense)

def add_expense():
    """Add a new expense"""
    print("\n=== ADD EXPENSE ===")
    
    # Show categories
    print("\nCategories:")
    for i, (cat, budget) in enumerate(CATEGORIES.items(), 1):
        print(f"{i}. {cat} (Budget: ₹{budget}/month)")
    
    # Get category
    choice = int(input("\nChoose category (1-6): "))
    category = list(CATEGORIES.keys())[choice - 1]
    
    # Get amount
    amount = float(input("Enter amount: ₹"))
    
    # Get description
    description = input("Enter description: ")
    
    # Create expense
    expense = {
        'date': datetime.now().strftime("%Y-%m-%d"),
        'category': category,
        'amount': amount,
        'description': description
    }
    
    # Save it
    save_expense(expense)
    
    print("✓ Expense added!")
    
    # Check if over budget
    check_budget_alert(category)

def check_budget_alert(category):
    """Alert if category spending exceeds budget"""
    expenses = load_expenses()
    current_month = datetime.now().strftime("%Y-%m")
    
    # Calculate spending for this category this month
    monthly_spending = sum(
        exp['amount'] 
        for exp in expenses 
        if exp['category'] == category and exp['date'].startswith(current_month)
    )
    
    budget = CATEGORIES[category]
    
    if monthly_spending > budget:
        print(f"\n⚠️  ALERT! {category} spending (₹{monthly_spending:.2f}) exceeds budget (₹{budget})!")
    elif monthly_spending > budget * 0.8:
        print(f"\n⚠️  Warning: {category} at {(monthly_spending/budget*100):.0f}% of budget")

def view_all_expenses():
    """View all expenses"""
    expenses = load_expenses()
    
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    print("\n=== ALL EXPENSES ===")
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10} {'Description':<30}")
    print("-" * 70)
    
    total = 0
    for exp in expenses:
        print(f"{exp['date']:<12} {exp['category']:<15} ₹{exp['amount']:>9.2f} {exp['description']:<30}")
        total += exp['amount']
    
    print("-" * 70)
    print(f"{'TOTAL':>27} ₹{total:>9.2f}")

def monthly_summary():
    """Show monthly spending summary"""
    expenses = load_expenses()
    
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    current_month = datetime.now().strftime("%Y-%m")
    
    # Filter this month's expenses
    monthly_expenses = [exp for exp in expenses if exp['date'].startswith(current_month)]
    
    if not monthly_expenses:
        print("\nNo expenses this month!")
        return
    
    print(f"\n=== MONTHLY SUMMARY ({datetime.now().strftime('%B %Y')}) ===\n")
    
    # Calculate category totals
    category_totals = {}
    grand_total = 0
    
    for exp in monthly_expenses:
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
        grand_total += exp['amount']
    
    # Display
    print(f"{'Category':<15} {'Spent':>10} {'Budget':>10} {'Remaining':>12} {'Status'}")
    print("-" * 60)
    
    for cat, budget in CATEGORIES.items():
        spent = category_totals.get(cat, 0)
        remaining = budget - spent
        percentage = (spent / budget * 100) if budget > 0 else 0
        
        status = "✓" if spent <= budget else "⚠️ OVER"
        
        print(f"{cat:<15} ₹{spent:>9.2f} ₹{budget:>9.2f} ₹{remaining:>11.2f} {status}")
    
    print("-" * 60)
    total_budget = sum(CATEGORIES.values())
    print(f"{'TOTAL':<15} ₹{grand_total:>9.2f} ₹{total_budget:>9.2f} ₹{total_budget-grand_total:>11.2f}")
    
    # Visual bar chart
    print("\n--- Spending Visualization ---")
    for cat, budget in CATEGORIES.items():
        spent = category_totals.get(cat, 0)
        percentage = int((spent / budget * 100) if budget > 0 else 0)
        bar_length = min(percentage, 100) // 2  # Max 50 chars
        bar = "█" * bar_length
        print(f"{cat:<15} {bar} {percentage}%")

def category_breakdown():
    """Show expenses by category"""
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES.keys(), 1):
        print(f"{i}. {cat}")
    
    choice = int(input("\nChoose category: "))
    category = list(CATEGORIES.keys())[choice - 1]
    
    expenses = load_expenses()
    cat_expenses = [exp for exp in expenses if exp['category'] == category]
    
    if not cat_expenses:
        print(f"\nNo expenses in {category}!")
        return
    
    print(f"\n=== {category.upper()} EXPENSES ===")
    print(f"{'Date':<12} {'Amount':>10} {'Description':<30}")
    print("-" * 55)
    
    total = 0
    for exp in cat_expenses:
        print(f"{exp['date']:<12} ₹{exp['amount']:>9.2f} {exp['description']:<30}")
        total += exp['amount']
    
    print("-" * 55)
    print(f"{'TOTAL':>22} ₹{total:>9.2f}")

def main_menu():
    """Main menu loop"""
    while True:
        print("\n" + "="*50)
        print("💰 EXPENSE TRACKER")
        print("="*50)
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Monthly summary")
        print("4. Category breakdown")
        print("5. Exit")
        print("="*50)
        
        choice = input("\nChoose option (1-5): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_breakdown()
        elif choice == "5":
            print("\n💾 All data saved to expenses.csv")
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice!")

# Run the program
if __name__ == "__main__":
    main_menu()