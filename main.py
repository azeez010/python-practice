import bukata


list_of_expenses = []

while True:
    choice = input("1. add expense\n2. View expenses\n3. Show Summary\n4. Exit\n")

    if choice == "1":
        expense = bukata.add_expense()
        if expense is not None:
            list_of_expenses.append(expense)
    elif choice == "2":
        bukata.view_expense(list_of_expenses)
    elif choice == "3":
        bukata.Summarize_expenses(list_of_expenses)
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid input try again!")