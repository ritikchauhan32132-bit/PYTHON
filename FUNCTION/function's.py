# 1. print length of list

def list_len(n):
    print(len(n))
    return

list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

list_len(list)


# 2. print list in singlr line 

def single_line(n):
    for i in range(1,):
        print(n, end=" ")
    return

list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

single_line(list)


# 3. factorial of n 

def fect_n(n):
    j = 1
    for i in range(1, n+1):
        j *= i
    print(j)
    return


fect_n(5)


# 4. convert USD to INR 

def usd(usd_val):
    ind_val = usd_val * 83
    print(ind_val)
    
usd(5)


# write a function to find to odd or even 

def find(n):
    if (n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

find(6)