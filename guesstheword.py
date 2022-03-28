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

def guesstheword():
    global playing
    active_word = (words[random.randint(0, len(words))])
    guesses = 10
    while playing == True:
        print(len(str(active_word)))
        inp = input("Enter a letter: ")
        LineSpam(50)
        print("you guessed: " + inp)
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


guesstheword()

        
    
    
