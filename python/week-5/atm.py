balance = 1000
valid_amounts = [50, 100, 200, 500]

while True:
    print("\--- ATM Menu ---")
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("0 - Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print(f"Current Balance: {balance} SAR")
        
    elif choice == "2":
        while True:
            try:
                amount = int(input("Choose amount to deposit (50, 100, 200, 500) or 0 to cancel: "))
                if amount == 0:
                    break
                if amount in valid_amounts:
                    balance += amount
                    print(f"Deposited {amount} SAR. New Balance: {balance} SAR")
                    break
                else:
                    print("Invalid amount. Please choose 50, 100, 200, or 500.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "3":
        while True:
            try:
                amount = int(input("Choose amount to withdraw (50, 100, 200, 500) or 0 to cancel: "))
                if amount == 0:
                    break
                if amount in valid_amounts:
                    if amount <= balance:
                        balance -= amount
                        print(f"Withdrew {amount} SAR. New Balance: {balance} SAR")
                        break
                    else:
                        print("Insufficient funds")
                        break
                else:
                    print("Invalid amount. Please choose 50, 100, 200, or 500.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "0":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
