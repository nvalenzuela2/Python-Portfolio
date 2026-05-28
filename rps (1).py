#Natalia
#A simulation of the rock paper scissors game where the players play against a computer
#Rock Paper or Scissors

#init
import random
print("Welcome to Rock, Paper, Or Scissors!")
#functions
def rps():
    wins = 0
    losses = 0
    draw = 0
    while True:
        game = int(input("Rock, Paper, or Scissors - Pick 1, 2 or 3(1 is Rock, 2 is Paper, and 3 is Scissors) type 4 when you're done playing: "))
        comp = random.randint(1,3)
        if game == comp:
            print("Tie!")
            draw = draw + 1
        elif game == 1 and comp == 2:
            print("You lost! Computer choose Paper")
            losses = losses + 1
        elif game == 1 and comp == 3:
            print("You won! Computer chose Scissors")
            wins = wins + 1
        elif game == 2 and comp == 1:
            print("You won! Computer chose Rock")
            wins = wins + 1
        elif game == 2 and comp == 3:
            print("You lost! Computer chose Scissors")
            losses = losses +  1
        elif game == 3 and comp == 1:
            print("You lost! Computer chose Rock")
            losses = losses + 1
        elif game == 3 and comp == 2:
            print("You won! Computer choose Paper")
            wins = wins + 1
        else:
            break
        print(f"Wins:{wins} Losses:{losses} Draws:{draw}")
        continue



#main
rps()
