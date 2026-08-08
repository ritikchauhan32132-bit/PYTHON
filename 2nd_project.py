import random

computer = random.randint(1, 100)

you = input("Do you play the game?  ").upper()
print()

if(you != "YES"):
    print("Don't worry meet me next time")
    print()
else:
    print("Let's Go.....")
    
    while True:
        chose = int(input("Enter a number between 1 and 100: "))
        
        if(chose == computer):
            print("Wow Your are finaly chosing the number🎉")
            print()
            break
            
        elif(chose < computer):
            print("Your Number Is lessThen Computer Number!")
            print()
            
        elif(chose > computer):
            print("Your Number Is GreaterThen Computer Number!")
            print()
            
        else:
            print("Please enter the vailed number (1 - 100)")
            print()
            