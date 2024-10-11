# simple banking program

def show_balance(balance):
    print(f"Your balance is {balance:.2f} BDT\n")


def deposit():
    deposit_amount = float(input("Enter deposit amount: "))
    print()

    if deposit_amount <= 0:
        print("Invalid amount\n")
        return 0
    else:
        return deposit_amount


def withdraw(balance):
    withdraw_amount = float(input("Enter withdraw amount: "))
    print()

    if balance < withdraw_amount:
        print("Insufficient funds\n")
        return 0
    elif withdraw_amount <= 0:
        print("Withdraw amount must be grather then 0\n")
        return 0
    else:
        return withdraw_amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("----- Banking Service -----")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid Input!!!\n")

    print("--- Bank Service Closed ---")


if __name__ == "__main__":
    main()