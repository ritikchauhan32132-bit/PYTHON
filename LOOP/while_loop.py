# # 1 - 100 print

# i = 1
# while (i <= 100):
#     print((i))
#     i += 1


# #  100 - 1 

# j = 100
# while(j >= 1):
#     print(j)
#     j -= 1


# # multiplication of n

# n = int(input("Enter n: "))
# i = 1
# while(i <= 10):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# # list print using loop

# list = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ]
# i = 0
# while(i < len(list)):
#     print(list[i])
#     i += 1


# # tuple using loop 

# tuple = ( 1 , 4 , 9 , 16 , 25 , 36 , 49 , 36 , 81 , 100 )
# x = 36
# i = 0
# while(i < len(tuple)):
#     if(tuple[i] == x):
#         print("Found!")
#     else:
#         print("Searching...")
    
#     i += 1
    
# sum of n numbers 

n = int(input("Enter a Number: "))
sum = 0
i = 0
while(i <= n):
    sum = sum + i
    
    i += 1
    print(sum)