choice = None
name = None
mobile = None
account = None
age = None
father = ""
balance = 0
deposite = None
Withdrow = None
details = {}
dics_balance = {}


while True:
    print("_" * 30)
    print("===What want to do you?===")
    print("1. Apply For ATM!")
    print("2. View ATM Details!")
    print("3. Add Balance!")
    print("4. Check Balance!")
    print("5. Withrow Balance!")
    print("6. Exit!")
    print("_" * 30)
    choice = int(input("Enter Choice: "))

    match choice:
        case 1:
            print("Please fill the form!")
            print("_" * 30)

            name = input("Enter Name: ").title()
            account = int(input("Enter Account Number: "))
            password = input("Create a Password: ")
            age = int(input("Enter Age: "))
            mobile = int(input("Enter Mobile Number: "))
            father = input("Enter Your Father Name: ").title()

            details[account] = {
                "Name": name,
                "Account": account,
                "Password": password,
                "Age": age,
                "Mobile": mobile,
                "Father": father,
                "Balance": balance,
            }

            check = input("Do You Want to add more Account for ATM(Yes/No): ").title()

            if "Yes" in check:
                continue

        case 2:
            ac = int(input("Enter ATM No: "))
            pas = input("Enter Password: ")
            if ac == account:
                if pas == password:
                    print("_" * 30)
                    print("===Account Detail===")
                    print(details[account].items())
                else:
                    print("Invalid Password!")
            else:
                print("===Invalid ATM No===")

            check = input("Do You Want to add more Account for ATM(Yes/No): ").title()

            if check=="Yes" :
                continue

        case 3:
            print("_" * 30)

            ac = int(input("Enter ATM No: "))
            pas = input("Enter Password: ")
            if ac == account:
                if pas == password:
                    print("_" * 30)
                    ammount = float(input("Enter Your Deposite Balance: "))

                    balance = balance + ammount
                    print(f"Your Current Balance : {details[account]['Balance']}")

            check = input("Do you have more some Deposite balance: ").title()
            if check=="Yes" :
                continue

        case 4:

            ac = int(input("Enter ATM No: "))
            pas = input("Enter Password: ")
            if ac == account:
                if pas == password:
                    print(details[account]['Name'])
                    print(f"Current Balance : {details[account]['Balance']}")

            check = input("Do you stay on that page? : ").title()

            if check=="Yes" :
                continue

        case 5:
            # withdrow

            ac = int(input("Enter ATM No: "))
            pas = input("Enter Password: ")
            if ac == account:
                if pas == password:
                    ammount = float(input("Enter your Withdrowal Ammount: "))
                    details[account]['Balance'] = details[account]['Balance'] - ammount

                    print(f"Current Balance: {details[account]['Balance']}")

            print("_" * 30)
            check = input("Do you withdrow more some money: (Yes/No):").title()

            if check=="Yes" :
                continue

        case 6:
            print("Exiting Program seccussfully!")
            break
