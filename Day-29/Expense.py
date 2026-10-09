def add_expense():
    title = input("Expense Name: ")

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be positive.")
            return

        with open("expense.txt", "a") as file:
            file.write(f"{title},{amount}\n")

        print("Expense saved!")

    except ValueError:
        print("Please enter a valid number.")


def view_expenses():
    try:
        with open("expense.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.")
            return

        for expense in expenses:
            print(expense.strip())

    except FileNotFoundError:
        print("No expense file found yet.")


def total_expenses():
    total = 0

    try:
        with open("expense.txt", "r") as file:
            for line in file:
                title, amount = line.strip().split(",")
                total += float(amount)

        print("Total expenses:", total)

    except FileNotFoundError:
        print("No expenses found yet.")


while True:
    print("\nWelcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice.")
