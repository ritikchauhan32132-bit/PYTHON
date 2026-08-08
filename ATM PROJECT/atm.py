import random
dics = {}

print("Welcome to the ATM Project")

while True:
    print("_"*30)
    print("=== ATM Menu ===")
    print("1. Create Account: ")
    print("2. Check Balance: ")
    print("3. Deposit Money: ")
    print("4. View Account Details: ")
    print("5. Withdraw Money: ")
    print("6. Change Your PIN: ")
    print("7. Transaction History: ")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("_"*30)
            print("=== Create Account ===")
            name = input("Enter your name: ")
            acc_no = random.randint(100000, 999999)
            pin = input("Enter your PIN: ")
            balance = float(input("Enter initial balance: "))
            
            dics[name] = {"Account Number": acc_no, "PIN": pin, "Balance": balance}
            print("Account created successfully!")
            print(f"Your account number is: {acc_no}")
            
            choose = input("Do you want to create another account? (Yes/No): ").lower()
            if choose == "yes":
                continue
        case 2:
            print("_"*30)
            print("=== Check Balance ===")
            acc_no = int(input("Enter your account number: "))
            for name, details in dics.items():
                if details["Account Number"] == acc_no:
                    print(f"Your balance is: ${details['Balance']}")
                    break
            else:
                print("Account not found.")
                
        case 3:
            print("_"*30)
            print("=== Deposit Money ===")
            acc_no = int(input("Enter your account number: "))
            for name, details in dics.items():
                if details["Account Number"] == acc_no:
                    amount = float(input("Enter amount to deposit: "))
                    details["Balance"] += amount
                    print(f"Deposited ${amount}. New balance is: ${details['Balance']}")
                    break
            else:
                print("Account not found.")
                
        case 4:
            print("_"*30)
            print("=== View Account Details ===")
            acc_no = int(input("Enter your account number: "))
            for name, details in dics.items():
                if details["Account Number"] == acc_no:
                    print(f"Name: {name}")
                    print(f"Account Number: {details['Account Number']}")
                    print(f"Balance: ${details['Balance']}")
                    break
            else:
                print("Account not found.")
                
        case 5:
            print("_"*30)
            print("=== Withdraw Money ===")
            acc_no = int(input("Enter your account number: "))
            for name, details in dics.items():
                if details["Account Number"] == acc_no:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount <= details["Balance"]:
                        details["Balance"] -= amount
                        print(f"Withdrew ${amount}. New balance is: ${details['Balance']}")
                    else:
                        print("Insufficient balance.")
                    break
            else:
                print("Account not found.")
                
        case 6:
            print("_"*30)
            print("=== Change Your PIN ===")
            acc_no = int(input("Enter your account number: "))
            for name, details in dics.items():
                if details["Account Number"] == acc_no:
                    new_pin = input("Enter new PIN: ")
                    details["PIN"] = new_pin
                    print("PIN changed successfully!")
                    break
            else:
                print("Account not found.")
                
        case 7:
            print("_"*30)
            print("=== Transaction History ===")
            acc_no = int(input("Enter your account number: "))
            for name, details in dics.items():
                if details["Account Number"] == acc_no:
                    print(f"Transaction history for {name}:")
                    # Placeholder for transaction history logic
                    break
            else:
                print("Account not found.")
                
        case _:
            print("Invalid choice. Please try again.")