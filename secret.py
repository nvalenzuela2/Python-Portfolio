#Natalia
#Secret
#This game has the computer choose a random number and the user guess until it gets it right

import random
import sys

def game():
    y = input("Choose game(easy, medium, hard): ")
    if y == "easy":
        def secret1():
            random_integer = random.randint(1,10)
            for i in range(5):
                while True:
                    x = int(input("Enter your first guess: "))
                    if x == random_integer:
                        print("Congrats you guessed correctly!")
                        break
                    sys.exit()
                    else:
                        print("Try again")
                        if x == random_integer - 1 or x == random_integer + 1 or x == random_integer - 2 or x == random_integer + 2:
                            print("hot")
                        elif x == random_integer - 3 or x == random_integer + 3:
                            print("warm")
                        else:
                            print("cold")
                        break
                        sys.exit()
        secret1()

    elif y == "medium":
            def secret2():
                random_integer = random.randint(1,50)
                for i in range(5):
                    while True:
                        x = int(input("Enter your first guess: "))
                        if x == random_integer:
                            print("Congrats you guessed correctly!")
                            break
                        sys.exit()
                        else:
                            print("Try again")
                            if x == random_integer - 1 or x == random_integer + 1 or x == random_integer - 2 or x == random_integer + 2:
                                print("hot")
                            elif x == random_integer - 3 or x == random_integer + 3:
                                print("warm")
                            else:
                                print("cold")
                            break
                            sys.exit()
            secret2()
    else:
                def secret3():
                    random_integer = random.randint(1,100)
                    for i in range(5):
                        while True:
                            if x == random_integer:
                                print("Congrats you guessed correctly!")
                                break
                            sys.exit()
                            else:
                                print("Try again")
                                if x == random_integer - 1 or x == random_integer + 1 or x == random_integer - 2 or x == random_integer + 2:
                                    print("hot")
                                elif x == random_integer - 3 or x == random_integer + 3:
                                    print("warm")
                                else:
                                    print("cold")
                                break
                                sys.exit()
                secret3()




#main
game()
