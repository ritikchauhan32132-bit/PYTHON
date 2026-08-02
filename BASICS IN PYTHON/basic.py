import string
from tkinter.font import names

# squre 
num1 = int(input("Enter Number: "))
print("Squre: ",num1**2) #ya num1 * num1 = num1 squre

#bolean data type?

a = 10
b = 20
tum = a > b
print(type(tum))

# average
a = 12
b = 13

average = (a+b)/2

print((average))



# string

name = "Ritik kumar bca-III"

nameshort = name[0:3]
print(nameshort)       # 0 - 2 tak ka string print karayega

character = name[1]
print(character) #ye index number 1 ka string print karayega

lenth = len(name)
print(lenth) # ye string ka length batayega number me


print(name[-4:-1]) # last se first ki or aayea or -1 ginti me nahi aayega

print(name[1:4]) # last wala index print nahi hota


print(name[1:]) # 1 se by default last  tak jayega

print(name[ :6]) # YE BY defult 0 - 6 tak jayega

a = "0123456789"
print(a[1:7:3]) # 1 se start hoga or 7 tak jayega or 1 ke baad 3 step tak jayega yani 2 step jump karne 3 step ko print karega

b = "abcdefgiklmnopqrstuvwxyz"
print(b[1:7:3])   # 1 se start hoga or 7 tak jayega or 1 ke baad 3 step tak jayega yani 2 step jump karne 3 step ko print karega

# Replace


latter = """Dear <|name|>
            you are selected
                <|Date|>"""

print(latter.replace("<|name|>","Ritik").replace("<|Date|>","26-06-2007"))


name = "Ritik is a good boy"

print(name.find("")) # ye space ko fine kar raha hai or isme jo bhi latter
                    # likhenge ya kuchh bhi usko hamare variable me find karega
                    
# List

my_friend = ["Raja","Shubhangi","Vishal","Shankar"]
print(my_friend[0])

my_friend[0] = "raja" # replace ho jayea Raja - raja me
print(my_friend)

my_friend.sort()
print(my_friend)

list = [1,21,32,43,12,32,43]
list.sort() # lower case to upper case me convert kar dega
print(list)

list.reverse()
print(list)

print(list[1:4])
print(list[0])
list.append("Ritik")
print(list)


name = "ritik kumar"

print(len(name))
print(name.endswith("ik"))
print(name.startswith("rit"))
print(name.capitalize()) #first word ko capital kar dega
print(name.title()) #sarre word ke first latter ko capitial karega
name.insert(3,"ram")
name.pop(2)
name.remove()