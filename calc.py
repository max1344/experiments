
def addition (x,y,):
     
    return x+y

def subtraktion(x,y):
    return x-y

def multiplikation(x,y):
    return x*y

def divition(x,y):
    return x/y

choice = input("Choose: \n1 additon   \n2 subtraktion \n3 multiplikation \n4 divition\n")
x = int(input("Choose4 first number: "))
y = int(input("Choose second number: "))


if choice == "1":
    print(addition(x,y))
elif choice == "2":
    print(subtraktion(x,y))
elif choice == "3":
    print(multiplikation(x,y))
elif choice == "4":
    print(divition(x,y))
