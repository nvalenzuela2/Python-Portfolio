#Natalia
#Hogwarts
#Create a Python program that asks the user for their and assigns them to one of the from the series.

import time
import random
def main():
    print("Welcome to Hogwarts")
    name = input("What is your name?: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print(house(name))

def house(name):
    if name == "harry"  or name == "ron" or name == "hermione":
        return ("Gryffindor")
    elif name == "newt" or name == "nymphadora" or name == "pamona":
        return ("Hufflepuff")
    elif name == "luna" or name == "cho" or name == "filius":
        return ("Ravenclaw")
    elif name == "voldemort" or name == "draco" or name == "serverus":
        return ("Slytherin")
    else:
        num = random.randint(1,4)
        if num == 1:
            return ("Gryffindor")
        elif num == 2:
            return("Hufflepuff")
        elif num == 3:
            return("Ravenclaw")
        elif num == 4:
            return("Slytherin")

main()
