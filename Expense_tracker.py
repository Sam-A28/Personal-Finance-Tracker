import calendar
import datetime
from expense import Expense

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get User input for expense details
    expense = get_user_expense()

    # Write the expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read the expenses from the file and display them
    summarize_expenses(expense_file_path, budget)

def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
    print (f"Expense Name: {expense_name}, Expense Amount: ${expense_amount:.2f}")

    expense_catergories = [
        "Food", 
        "Transportation", 
        "Entertainment", 
        "Utilities", 
        "Other"
    ]

    while True:
        print("Select Expense category:")
        for i, category_name in enumerate(expense_catergories):
            print(f"{i+1}. {category_name}")
        
        value_range = f"[1-{len(expense_catergories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: "))-1

        if i in range(len(expense_catergories)):
            selected_category = expense_catergories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
                )
            return new_expense
        else:
            print(f"Invalid input. Please enter a number {value_range}.")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving Expense to File: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing Expenses...")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expense By category:")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")

    total_sum = sum(x.amount for x in expenses)
    print(f"You've spent a total of ${total_sum:.2f} this month.")

    remaining_budget = budget - total_sum
    print(f"You have ${remaining_budget:.2f} remaining in your budget of ${budget:.2f}.")

    # Get Current date
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"You have {remaining_days} days left in the month.")

    daily_budget = remaining_budget / remaining_days
    print (f"Budget per day: ${daily_budget:.2f}")



if __name__ == "__main__":
    main()