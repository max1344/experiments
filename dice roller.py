import random
#\
Playing = True

def rolldice():
    while Playing == True:
        inp = input("Would you like to roll dice\nyes or no\n")
        if inp == "yes":
            print("You rolled: " + str(random.randint(1,6)))
            playag = input("Would you like to roll again?")
            print(playag)
        if playag == "yes":
            Playing = True
            print("You rolled: " + str(random.randint(1,6)))
        else:
            Playing = False
        if inp == "no":
            Playing = False
            print("why not?")
            

        


rolldice()