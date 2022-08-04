import random
import readline

file = open('words.txt','r')

words = file.readlines()

for i in range(len(words)):
    words[i] = words[i].replace("\n","")

activeWord = words[random.randint(0,len(words))]

def LineSpam(amount):
    for i in range(amount):
        print("\n ")

def hangman():
    reveal = ""
    playing = True
    for i in range(len(activeWord)):
        reveal += "_"
    while playing:
        LineSpam(50)
        print(reveal)
        guess = input("Choose your letter: ")


        



hangman()