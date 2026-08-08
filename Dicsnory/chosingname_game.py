import random

name = ["vishal","sankar","sohan","akash"]
computer = random.randint(name)

print(computer)
man = {
    "vishal" : 1,
    "sankar" : 2,
    "Sohan" : 3,
    "akash" : 4,
}

name = {
    1 : "vishal",
    2 : "sankar",
    3 : "Sohan",
    4 : "akash",
}

chose = input("Enter chose your name: ")

if(chose == name[1]):
    print("hello")