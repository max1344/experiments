import random


playing = True


def function():
  answer = random.randint(1,10)
  inp = input("Guess your number: ")
  while inp not in ["1", "2", "3","4","5","6","7","8","9","10"]:
      #inp = input("Invalid guess again: ")
      print("invalid")
      return 
  print("The correct answer was: " + str(answer))
  if answer == int(inp):
    global playing
    playing = False
    print("correct answer")
  else: 
    print("Wrong number")

x = [1,2,3]
print(type(x))
print(x)

set = {"apple", "banana", "orange", "pear", "olive", "grape", }
print(set)

while playing == True:
  function()





