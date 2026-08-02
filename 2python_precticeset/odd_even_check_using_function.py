# odd or even ka check karo number odd hai ya even

def check():
    number = int(input("Enter a Number: "))
    
    if(number%2==0):
        print(f"This is a odd number: {number}")
    
    elif(number%2==1):
        print(f"This is a Even number: {number}")
    
    else:
        print("Invailed number!")
        
check()