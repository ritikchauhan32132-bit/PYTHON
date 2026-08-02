print("=====Click to exit for exit=====")
while True:
    
    required = input("What want to doing (+ , - , x , /): ")
    
    if(required == '+'):
        num1 = int(input("Enter 1 Number: "))
        num2 = int(input("Enter 2 Number:"))
        print("Result: ",num1+num2)
    
    elif(required == '-'):
            num1 = int(input("Enter 1 Number: "))
            num2 = int(input("Enter 2 Number:"))
            print("Result: ",num1-num2)
            
    elif(required == 'x'):
            num1 = int(input("Enter 1 Number: "))
            num2 = int(input("Enter 2 Number:"))
            print("Result: ",num1*num2)
    
    elif(required == '/'):
            num1 = int(input("Enter 1 Number: "))
            num2 = int(input("Enter 2 Number:"))
            print("Result: ",num1/num2)
            
    elif(required == "exit"):
        break
    
    else:
        print("Invailed Choice!")