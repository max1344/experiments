



def calc(z,x,y):
    if välj == "+":
        res1 = x + y
        print("Svar: " + str(res1))
    if välj == "-":
        res1 = x - y
        print("Svar: " + str(res1))
    if välj == "x":
        res1 = x * y
        print("Svar: " + str(res1))
    if välj == "/":
        res1 = x / y
        print("Svar: " + str(res1))
    else:
        print("Invalid Character")

välj = input("Välj räknesätt: +,-,x,/")
inp1 = input("tal 1: ")
inp2 = input("tal 2: ")
calc(välj,int(inp1),int(inp2))


    



