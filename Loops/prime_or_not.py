n = int(input("Enter Number: "))

if (n % 2)==0:
    print(f"This number is not a prime: {n}")
else:
    print("This number is prime: ")



num = int(input("Enter a number: "))

for i in range(2, num):
    if(num % i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")