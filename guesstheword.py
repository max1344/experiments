import random 

file = open('words.txt','r')
words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace("\n","")

#dog = "xdasds"
 #if "x" is in dog:
      #print "Yes!"

playing = True

def LineSpam(amount):
    for i in range(amount):
        print("\n")

def updateReveal(inp, reveal):
    global active_word
    for i, char in enumerate(active_word):
        if inp == char:
            reveal = reveal[:i] + inp + reveal[i+1:]
    return reveal

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def guesstheword():
    global playing, active_word
    active_word = words[random.randint(0, len(words))]
    guesses = 10
    reveal = ""
    for i in range(len(active_word)):
        reveal += "_"
    while playing == True:
        if ("_" not in reveal):
            print(reveal)
            print("you won!")
            #playing = False
            break
        print(reveal)
        inp = input("Enter a letter: ")
        LineSpam(50)
        print("you guessed: " + inp)
        if inp not in alfabet:
            print("invalid character")
            guesses += 1
        if inp in active_word:
            print("letter was in word")
        if inp not in active_word:
            print("letter not in word")
            guesses -= 1
            print("Number of guesses left: " + str(guesses))
            if guesses <= 0:
                playing = False
                print("Game Over ")
                print(active_word)
        reveal = updateReveal(inp, reveal)
        


guesstheword()

        
    
    
