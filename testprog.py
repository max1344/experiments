

from random import random
import random, os, signal

def calculateWinner(p1, p2):
    if (p2+1) % 3 == p1:
        print("You won")
    elif p1 == p2:
        print("It's a tie!")
    else:
        print("Opponent won!")

def rps():
    dicionary = {
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}
    while True:
        choosing = True
        while choosing == True:
            print("Choose: \n1. rock \n2. paper \n3. scissors")
            inp = input() 
            if inp in ["1","2","3"]:      
                print("You chose: " + dicionary[int(inp)])
                opponent = random.randint(1,3)
                print("Opponent chose: " + dicionary[opponent])
                choosing = False
            else:
                print("Invalid alternative")
        print("\n ")
        calculateWinner(int(inp) - 1, int(opponent)-1)
        print("\n ")
        again = input("Play again? y/n: ")
        print("\n ")
        if again != "y":
            os.kill(os.getppid(), signal.SIGHUP)
            break

rps()




