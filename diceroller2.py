import random, sys
from turtle import distance
playing = False

def rolldice():
    print("you rolled: " + str(random.randint(1,6)))
            
def CheckIfEven(a):
    rest = a % 2
    if rest == 0:
        return "it is even"
    else:
        return "it is not even"
    

print(CheckIfEven(8))

inp = input("Wanna play a game? y/n")
if inp == "y":
    playing = True
    rolldice()
else:
    print("see ya!")

while playing == True:
    inp = input("Play again?")
    if inp == "y":
        rolldice()
    else:
        print("see ya!")
        break