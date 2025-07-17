import random

computer = random.choice([-1, 0, 1])
youstr = input("enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict ={1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youstr]

print(f"You Chose {reversedDict[you]}\nComputer Chose {reversedDict[computer]}")

if(computer == you):
    print("Its a Draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You win!")

    else:
        print("Somthing Went Wrong!")
