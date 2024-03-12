#A program to prepare a student budget planner
    
# A function to calculate the balance(income, expenses)
def calculate_balance(income, expenses):
    total_income = sum(income)
    total_expences = sum(expenses)
    balance = total_income - total_expences
    return balance

def main():
    print(f"Welcome to the Student Budget Planner Program!")

    num_income_source = int(input("Enter the number of income sources:"))
    income = [float(input(f"Enter income amount {i + 1}:")) for i in range(num_income_source)]

    num_expenses = int(input("Enter the number of expenses:"))
    expenses = [float(input(f"Enter the expenses amount {i + 1}:")) for i in range(num_expenses)]

    balance = calculate_balance(income, expenses)

    print("\n--- Financial Summary---")
    print(f"Enter Income: ${sum(income)}")
    print(f"Enter Expenses: ${sum(expenses)}")

    if balance>= 0:
        print(f"Congratulation! You have a surplus amount of ${balance}.")

    else:
        print(f"Warning! You have a deficit ${abs(balance)}.")


main()