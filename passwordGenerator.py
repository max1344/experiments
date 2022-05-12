import random 

bokst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
siffr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symb = ['!', '#', '€', '%', '&', '/', '(', ')']

dict = {
    0 : bokst,
    1 : siffr,
    2 : symb
}

def Generate(length):
    password = ''
    for x in range(0,length):
        curList = dict[random.randint(0,2)]
        password += curList[random.randrange(0,len(curList))]
    return password


inp = input("What lenght? ")
print("Password: " + Generate(int(inp)))

while True:
    print(random.randint(0,9))



