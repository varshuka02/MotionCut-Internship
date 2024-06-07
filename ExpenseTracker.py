import uuid
import datetime

expenses = {}

def generate_unique_id():
    return str(uuid.uuid4())

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        category = input("Enter expense category (e.g., Food, Transportation, Entertainment): ")
        date = input("Enter date (DD-MM-YYYY) or leave blank for today: ")
        if not date:
            date = datetime.date.today().strftime("%d-%m-%Y")
        else:
            datetime.datetime.strptime(date, "%d-%m-%Y")
        expense_id = generate_unique_id()
        expenses[expense_id] = {"amount": amount, "description": description, "category": category, "date": date}
        print("Expense added successfully! Expense ID:", expense_id)
    except ValueError as e:
        print("Invalid input:", e)

def display_expenses(expenses_list):
    if not expenses_list:
        print("No expenses to display.")
    for expense_id, expense in expenses_list.items():
        print("ID:", expense_id, ", Amount: ₹{:.2f}, Description: {}, Category: {}, Date: {}".format(expense['amount'], expense['description'], expense['category'], expense['date']))

def view_summary():
    category_summary = {}
    monthly_summary = {}

    for expense in expenses.values():
        category = expense['category']
        month = expense['date'][3:10]

        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += expense['amount']

        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += expense['amount']

    print("\nCategory-wise Summary:")
    for category, total in category_summary.items():
        print("{}: ₹{:.2f}".format(category, total))

    print("\nMonthly Summary:")
    for month, total in monthly_summary.items():
        print("{}: ₹{:.2f}".format(month, total))

def update_expense():
    expense_id = input("Enter ID of expense to update: ")
    if expense_id in expenses:
        try:
            new_amount = input("Enter new amount (or leave blank): ")
            new_description = input("Enter new description (or leave blank): ")
            new_category = input("Enter new category (or leave blank): ")
            new_date = input("Enter new date (DD-MM-YYYY) (or leave blank): ")

            if new_amount:
                expenses[expense_id]['amount'] = float(new_amount)
            if new_description:
                expenses[expense_id]['description'] = new_description
            if new_category:
                expenses[expense_id]['category'] = new_category
            if new_date:
                datetime.datetime.strptime(new_date, "%d-%m-%Y")
                expenses[expense_id]['date'] = new_date

            print("Expense updated successfully!")
        except ValueError as e:
            print("Invalid input:", e)
    else:
        print("Invalid expense ID!")

def remove_expense():
    expense_id = input("Enter ID of expense to remove: ")
    if expense_id in expenses:
        del expenses[expense_id]
        print("Expense removed successfully!")
    else:
        print("Invalid expense ID!")

def main_menu():
    print("\nExpense Tracker Application")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Update Expense")
    print("5. Remove Expense")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

while True:
    choice = main_menu()
    if choice == '1':
        add_expense()
    elif choice == '2':
        print("\nExpenses:")
        display_expenses(expenses)
    elif choice == '3':
        view_summary()
    elif choice == '4':
        update_expense()
    elif choice == '5':
        remove_expense()
    elif choice == '6':
        print("Exiting application...")
        break
    else:
        print("Invalid choice. Please try again.")
