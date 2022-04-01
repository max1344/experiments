
from fnmatch import translate
import random
from tkinter import E

file = open('words.txt','r')
words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace("\n","")

#list = alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeoiuz":
            translation = translation + "g"
        else: 
            translation = translation + letter
    return translation



def passwordgen (): 
    inp = input("Enter anything you want included in your password\nIf you want a randomized password write nothing\n")
    if inp == "":
        password = random.choice(words) + random.choice(list)
        print(password)
    if inp == "cRandom":
        password = print("Your password is:" + translator(random.choice(words) + "%189389013"))
        print(password)
    else: 
        password = inp + random.choice(list)
        print(password)


passwordgen()





