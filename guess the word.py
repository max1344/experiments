import random 

file = open('words.txt','r')
words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace("\n","")

def guesstheword():
    print(words[random.randint(0, len(words))])
    