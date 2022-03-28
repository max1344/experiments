import random
#\

playing = True

def rolldice():
    inp = input("Would you like to roll dice\nyes or no\n")
    if inp == "yes":
        print("You rolled: " + str(random.randint(1,6)))
        playag = input("Would you like to roll again?")
        #print(playag)
        while playag == "yes":
        #if playag == "yes":
            break
        else:
            global playing
            playing = False
    if inp == "no":
        playing = False
        print("maybe later :)")
            

while playing == True:
    rolldice()



