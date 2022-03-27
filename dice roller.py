import random
#\

playing = True

def rolldice():
    inp = input("Would you like to roll dice\nyes or no\n")
    if inp == "yes":
        print("You rolled: " + str(random.randint(1,6)))
        playag = input("Would you like to roll again?")
        print(playag)
        if playag == "yes":
            global playing
            playing = True
            print("You rolled: " + str(random.randint(1,6)))
        else:
            global playing
            Playing = False
    if inp == "no":
        global playing
        playing = False
        print("why not?")
            

while playing == True:
    rolldice()