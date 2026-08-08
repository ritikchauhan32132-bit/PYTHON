# list print 

list = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ]

for el in list:
    print(el)


# search tuple (linear searh)

tuple = ( 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 )

for i in tuple:
    if(i == 16):
        print("Found!")
    else:
        print("Searching...")
    
else:
    print("Loop end")


# 1 - 100 y for loop 

for i in range(1,101):
    print(i)

# 100-1 

for i in range(100, 0, -1):
    print(i)



# multiplication table of a number n

n = int(input("Enter Number : "))
for i in range(1,11):
    print(n*i)