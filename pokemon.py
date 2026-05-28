#Natalia
#Pokemon
#Pokemon Game

#Init
import random
name = ("Caterpie")
level = 1
day = 1


#Functions

def main():
    print ("Welcome to Pokemon! When you train you level up 1 level, when you battle you level up 5 levels.")
    while True:
        global level
        global day
        welcome = input(f"It is Day {day} what would you like to do? Train, Battle, or View Stats, or Quit: ")
        day = day + 1
        if welcome == "train":
            train()
        elif welcome == "battle":
            battle()
        elif welcome == "view stats":
            info()
        elif welcome == "quit":
            break



def train():
    global level
    print(f"{name} did 15 pushups!")
    print("You have leveled up!")
    level = level + 1
    evolve()
    choice = input("Would you like to continue training, return to menu: ")
    if choice == "menu":
            main()
    elif choice == "train":
            train()


def battle():
    global level
    boss = input("Are you ready to battle the boss?: ")
    if boss == "no":
        battle = input("Who would you like to battle? : ")
        outcome = random.randint(1,2)
        if outcome == 1:
            print(f"You have beaten {battle}, and have leveled up!" )
            level = level + 5
            evolve()
        elif outcome== 2:
            print(f"You lost agasint {battle}. Better luck next time!")
    elif boss == "yes":
        global level
        bosses = random.randint(1,15)
        if bosses < level:
              print("You have beaten the final boss!")
              level = level + 10
              evolve()
        else:
            print("You have lost.....")
            level = level - 5
            evolve()


def info():
    global level
    global name
    global day
    print(f"You are currently at level {level}, day {day}, and you have grown to be {name}")
    if name == "Caterpie":
        print((r"              ,`.\n"))
        print((r"              L  \\\n"))
        print((r"             ,    \\\n"))
        print((r"            j      \\\n"))
        print((r"            ,       \\\n"))
        print((r"           j         `\n"))
        print((r"           ,          .__\n"))
        print((r"        ,-'Y          `  `-.\n"))
        print((r"     .-'    `..___..-'      `-.\n"))
        print((r"    /__           ,-.          \\\n"))
        print((r"   /(__)         `   '          `.\n"))
        print((r"  |               `\"'             L\n"))
        print((r"  `.------._                      |\n"))
        print((r",'          `                     |\n"))
        print(("F             |                    |\n"))
        print(("|             |                    |\n"))
        print(("`._         ,'                     j\n"))
        print((r"  `+------'                      /\n"))
        print((r"    \\                           /                         |`._\n"))
        print((r"     `.                       ,'                          |   \\\n"))
        print((r"       `._                _,-'                            |    \\\n"))
        print((r"          `-,.________,.-'   `.                           |     L\n"))
        print((r"           /                   '                          |     |\n"))
        print((r"          /             _,._   |                          ,`---,'\n"))
        print((r"        ,'|            /    .  j                        .'      `.\n"))
        print((r"        . L            '    | ,                      ,-'\"'`-..   |\n"))
        print((r"         .,\\            `--' / `.               ___./       ,.' ,'\n"))
        print((r"            \\              ,'    \\__         ,-'     \"-.    | |'\n"))
        print((r"             `-._______,.-'  __   | `'-._.,- ._        _`   `\"Y\n"))
        print((r"               |           .\"  \\  |     \\      `.    ,'  \\   ,'\n"))
        print((r"               |           '    | ;      .       .   `._./.-'\n"))
        print((r"               7.           `'\"' / `.--. |   _.. |      j\n"))
        print((r"               `.__       `   _-'   |   |j  /   ||     .'\n"))
        print((r"                   `-...,_..-'      `--'/   `._, ^----'\n"))
        print((r"                        .\\            _'       ,'\n"))
        print((r"              `         `._-.______,.'`.___,.-'mh\n"))
        print(("\n"))
    elif name == "Metapod":
        print((r"          _,--'\"\"\"\"\"\"---.._\n"))
        print((r"        ,'                 `._\n"))
        print((r"      ,'                      `.\n"))
        print((r"    ,'                          \\\n"))
        print((r"   .                             \\\n"))
        print((r" ,'.                  ,-`.        \\\n"))
        print((r"/   \\               ,'    ,        \\\n"))
        print(("|`.  |\\            ,`      |         |\n"))
        print(("L  `.| |         .''     _,'        _'\n"))
        print((r"\\    \"'        ,`'_..-''        _,'\n"))
        print((r" `.            '\"\"          _,.' `.\n"))
        print((r"   /._                 _..-\"       \\\n"))
        print((r"  /   `.          _,.-'             \\\n"))
        print((r" /      \\-.___.--'/                  \\\n"))
        print((r"|      ,/.     .-^+.._               F\n"))
        print((r" L..-''.' \\  .'   |   `'--.....___   .\n"))
        print((r" /     /   `/     |               `\"-;\n"))
        print((r"/     j    j      '                ,'\n"))
        print((r"`.    |    |       L          _.-'Y\n"))
        print((r" ,`._/     |        .    _,.-'     .\n"))
        print((r" `.  '|    |         \\\"\"\"|         |\n"))
        print((r"  |   |    |         |   |         |\n"))
        print((r"  |   |    |        ,'   |         |\n"))
        print((r"  |   L    +      ,'     |         |\n"))
        print((r"  |    \\    L    ,\\      j         |\n"))
        print((r"  L     \\   |   /  `.   /          j\n"))
        print((r"   \\    j\\  |  /    `. /          .\n"))
        print((r"    L  .  ` | /       \\          /\n"))
        print((r"    +  |   `|/                  /\n"))
        print((r"     \\ | _,..._         \\      /\n"))
        print((r"      ./'      `-._      \\   ,'\n"))
        print((r"       l           `.     ^_/\n"))
        print((r"       +             `   /\n"))
        print((r"        L-\"\"--.       .,'\n"))
        print((r"        |      `.     ,\n"))
        print((r"        .        \\  ,'\n"))
        print((r"         `       _.'\n"))
        print((r"          `....-' mh\n"))
    elif name == "Butterfree":
        print((r"                    ,--\"\"+--.\n"))
        print((r"                   /     j   /`.\n"))
        print((r"                  |     /   |   `.\n"))
        print((r"                  |   ,'    '     \\\n"))
        print((r"                  j,-'     '`..    \\\n"))
        print((r"                 +      _ /    `._/ \\\n"))
        print((r"                 |     / '-.     |   .\n"))
        print((r"                 |    /     |   /    |\n"))
        print((r"                 |   /     j   j     |\n"))
        print((r"                 |  j      |   |     |._\n"))
        print((r"                 | .'     7    |     |  `.\n"))
        print((r" ___      _.._   | j      |    +     '    `.\n"))
        print((r"|.---=-.,'+-. `. |/       F     L  ,'    ,'`.\n"))
        print((r"||,==--'|_' |  j  \\      /      |,'   ,`'    L\n"))
        print((r"'Y'   | |  '/ ',.-.\\    j     ,,^  _,' \\     |\n"))
        print(("`.||   |  `.'  '    `.   / _,-'   `'     L   F\n"))
        print((r" ||   `     .  ,-.   `,--'              |   |\n"))
        print((r" `'    `.  /_,' ,'     `--------------\"\"\"\"'Y\n"))
        print((r"        _:\"'_.-'       /_>:-.__           /\n"))
        print((r"     `-\".`\"'__,`-.,-._/      `.\"\"`------\"'\n"))
        print((r"     `.| `\"'      | | _.--'\"\"'--\\\n"))
        print((r"      || /        | '\"  ___,.._  \\\n"))
        print((r"     _|||__      / /,.-'       `- .\n"))
        print((r"   ,'   `. .    /,'/'  _.,-\"\"\"--._F\n"))
        print((r"   7     | |  .',L'|_-'           |\n"))
        print((r"   +     | | / / ',\"'  ,.-'\"\"'`-._|\n"))
        print((r"    L    ' |. /  .-.`\"'           |\n"))
        print((r"    |   j j   \\  `-.'\\           j\n"))
        print((r"    +   | | \\  `.   ` `.  _.... ,\n"))
        print((r"     L  | |  \\   .   `  \\\"     /\n"))
        print((r"     | ,' |   L  ,'    \\ `    .\n"))
        print((r"     | || |   '  |      L `   |\n"))
        print((r"     `./|j     `. .     `. \\ j\n"))
        print((r"      |  '       ` .     | '\\`\n"))
        print((r"                  \\ '.   | \\\n"))
        print((r"                   | |  /,-'\n"))
        print((r"                   j l  \"\n"))
        print((r"                 _/_,'\n"))
        print((r"                ',' mh\n"))


def evolve():
     global level
     global name
     if level >= 5:
          name = "Metapod"
     elif level >= 15:
          name = "Butterfree"



#Main
main()

