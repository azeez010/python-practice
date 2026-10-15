def add_expense():
    try:
        expense_name = input("what is the expense?")
        expense_amount = int(input("How much did you spend?"))

        print(f"expense added! {expense_name} - {expense_amount}")
        return dict(expense_name=expense_name, amount=expense_amount)
    except ValueError as err:
        print("enter only numbers")

def view_expense(list_of_expenses):
    for expense in list_of_expenses:
        print(f"The expense is {expense["expense_name"]} - {expense["amount"]}")

def Summarize_expenses(list_of_expenses):
    extract_amounts = []

    print(list_of_expenses)
    for expense in list_of_expenses:
        print(expense)
        extract_amounts.append(expense["amount"])
        print(expense["amount"])

    print(extract_amounts)
    print(sum(extract_amounts))
    print(sum(extract_amounts) / len(extract_amounts))
