items = []
my = set()
print("_"*30)

while True:
    print("1. Add an items!")
    print("2. Display all items!")
    print("3. Remove an items!")
    print("4. Check whether an item exist!")
    print("5. Display Uniqe items!")
    print("6. Exit!")
    print("_"*30)
    
    usser = int(input("Enter Choice: "))
    
    match usser:
        case 1:
            print("_"*30)
            print("You are selected ! Add an items...")
            saman = input("Enter Item: ").lower()
            items.append(saman)
            print("Item Add Seccussfully✅")
            
            choice = input("Do you want to add more items! (Yes/No): ").lower()
            
            if(choice == "yes"):
                continue
            
        case 2:
            print("_"*30)
            print("=== All items ===")
            
            if items:
                for i in items:
                    print(i)
            else:
                print("Don't exist item in the list!")
                print("_"*30)
                
            
                
        case 3:
            print("_"*30)
            
            if choice in items:
                items.remove(choice)
                print("Item removed successfully!")
            else:
                print("Item does not exist!")
                
            choice = input("Do you want to remove more items! (Yes/No): ").lower()
                        
            if(choice == "yes"):
                continue
                
        case 4:
            print("_"*30)
            choice = input("Enter item name: ").lower()
            
            if choice in items:
                print("Item exists!")
            else:
                print("Item does not exist!")
                
            choice = input("Do you want to Check more items! (Yes/No): ").lower()
                        
            if(choice == "yes"):
                continue
                
        case 5:
            print("_"*30)
            
            unique_items = set(items)

            for i in unique_items:
               print(i)
                
            
        case 6:
            print("Exit...")
            break
            
        case _ :
            print("Invailed Choice!")
            
            