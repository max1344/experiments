import time 
import random
import time
import pygame
import keyboard


def reactiontime():
    inp = input("would you like to play? y or n? \n")
    while inp not in ["y", "n"]:
        print("invalid character")
        break
    if inp == "y":
        print("ready")
        time.sleep(1)
        print("set")
        time.sleep(random.randint(2,3))
        print("gooo")
        
    else:
        print("Game Over")
        











reactiontime()




