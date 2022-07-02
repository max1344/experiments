import random 

list = [i for i in range(0,100)]
random.shuffle(list)
print(list)

def BubbleSort(l):
    sorted = False
    while sorted == False: 
        sorted = True
        for i in range(0,len(l)):
            if (i+ 1 < len(l)):
                if (l[i] > l[i + 1]):
                    sorted = False
                    l[i], l[i+1] = l[i+1], l[i]



    



    

    return l

sortedList = BubbleSort(list)
print(sortedList)
