# Example 

def show(n):
    if(n == 0):
        return
    print(n, end=" ")
    show(n-1)
      
show(5)

# Nutural number sum using recursiveFunction

def rec_func(n):
    if(n == 0):
        return 0
    return rec_func(n-1)+n
    
rec = rec_func(5)
# print(rec)

def calc(n):
    if(n==0):
        return 0
    return calc(n-1)+n

sum = calc(10)
print(sum)


# Recursion in using list

def print_list(list , indx = 0):
    if(indx == len(list)):
        return
    print(list[indx])
    print_list(list , indx + 1)
    
fruits = ["Banana","lichhi","kela","Apple","Mango"]

print_list(fruits)