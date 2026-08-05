a = int(input("Enter 1 Number: "))
b = int(input("Enter 2 Number: "))
c = int(input("Enter 3 Number: "))

if(a > b and a > c):
    print(f"{a} is greater")
    
elif(b > a and b > c):
    print(f"{b} is greater")
    
elif(c > a and c > b):
    print(f"{c} is greater")
    
else:
    print("All number are same ", a)