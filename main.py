import random

computer = random.choice([1,0,-1])
'''
0 for Gun
1 for snack
-1 for water
'''

print("""
      Chose...
      g for Gun
      s for snack
      w for water
      """)

yourstr = input("Enter Your Choice: ").lower()

youDisc = {"s": 1, "g": 0, "w":-1}

reveseDisc = {1 : "Snack", 0 : "Gun", -1 :"Water"}

you = youDisc[yourstr]

print(f"You Chose {reveseDisc[you]} \n Computer Chose {reveseDisc[computer]}")


if(computer == you):
    print("Match Die! Both are same chosed!")
else:
    if(computer == 1 and you == 0):
        print("You Win! 👍")
        
    elif(computer == 1 and you == -1):
        print("You Lose 🤦‍♂️")
        
    elif(computer == 0 and you == 1):
        print("You Lose 🤦‍♂️")
    
    elif(computer == 0 and you == -1):
        print("You Lose 🤦‍♂️")
        
    elif(computer == -1 and you == 1):
        print("You Win👍")
        
    elif(computer == -1 and you == 0):
        print("You Win👍")
    
    else:
        print("Something went wrong! ")
        