def bigNum(a,b,c):
    if(a > b and a > 8):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c
    else:
        print("All Numbers are Same")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

result = bigNum(a,b,c)
print(result)