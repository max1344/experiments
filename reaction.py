import time
import random
import keyboard    #pip3 install keyboard 


#timeAtStart = time.time()

#ready = False
#set = False
#go = False

#time.sleep(2.4)


while True:
    if keyboard.read_key() == "p":
        print("you pressed p")
        break

while True: 
    if keyboard.is_pressed("q"):
        print("you pressed q")
        break

#timer = random.randint(3,7)

#while True:
    #timeSinceStart = (time.time() - timeAtStart)

   # if timeSinceStart > 1 and ready == False:
      #  print("Ready!")
      #  ready = True
   # if timeSinceStart > 2 and set == False:
       # print("Set!")
        #set = True
   # if timeSinceStart > timer and go == False:
      #  print("Go!")
      #  go = True
