import time
cart = []

while True:
    print()

    print("1. Add Items")
    print("2. Remove Items")
    print("3. Check Cart")
    print("4. Exit!")
    print()

    choice = input("Enter Your Choice: ")

    if choice.isdigit():
        choice = int(choice)
    else:
        print("Please enter only numbers!")
        continue
    
    
    print()
    if(choice == 1):
        item = input("Enter Item: ").title()
        print()
        cart.append(item)
        print("Add Seccessfully")
        print()

    elif(choice == 2):
        item = input("Enter Remove Item: ").title()
        print()
        if item in cart:
            cart.remove(item)
            print("Remove Seccessfully")
            print()
        else:
            print(f"{item}, Is not In The Cart")
            print()

    elif(choice == 3):
        print(cart)
        print()

    elif(choice == 4):
        
        time.sleep(3)
        print()
        exit()
    else:
        print("Invailed Choice!")
        print()
    
