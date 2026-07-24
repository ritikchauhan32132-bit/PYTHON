def fahrenheit():

    f = int(input("Enter Fahrenheit: "))
    c = 5 * (f - 32) / 9

    print(f"{c}°C")

fahrenheit()

print("a")
print("b")
print("c" , end=" ") # new line print hone se rokta hai
print("d" , end=" ")


'''

sum
if you in(10)
print(10): 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1   =   55

'''

def sum(n):
    if(n==1):
        return 1
    return sum(n - 1) + n

print(sum(10))