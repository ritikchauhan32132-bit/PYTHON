num1 = int(input("Enter 1 number: "))

num2 = int(input("Enter 2 number: "))

num3 = int(input("Enter 3 number: "))

if(num1 > num2 and num1 > num3):
    print(f"First number is Big: {num1}")
    
elif(num2 > num1 and num2 > num3):
    print(f"Secoend number is Big: {num2}")
    
elif(num3 > num1 and num3 > num2):
    print(f"Third number is Big: {num3}")
    
else:
    print(f"All number are same : {num1}")