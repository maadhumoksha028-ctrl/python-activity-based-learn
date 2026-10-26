# Assignment 7: ATM Transaction Simulation
# Menu for deposits, withdrawals, and balance checking.

balance = 5000.0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposit Successful")
        else:
            print("Amount must be greater than zero.")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Current Balance:", round(balance, 2))

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")
