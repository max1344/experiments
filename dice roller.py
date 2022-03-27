import random
#\
Playing = True

def rolldice():
    inp = input("Would you like to roll dice\nyes or no\n")
    if inp == "yes":
        print("You rolled: " + str(random.randint(1,6)))
        playag = input("Would you like to roll again?")
        print(playag)
        if playag == "yes":
            global Playing
            Playing = True
        else:
            global Playing
            Playing = False
    if inp == "no":
        global Playing
        Playing = False
        print("why not?")
        

        
while Playing == True:
    rolldice()