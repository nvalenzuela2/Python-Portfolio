import random
import pandas as pd
data = pd.read_csv('netflix.csv')

id = data['id'].tolist()
type = data['Type'].tolist()
title = data['Title'].tolist()
country = data['Country'].tolist()
data_added = data['Data Added'].tolist()
release = data['Release Year'].tolist()
rating = data['Rating'].tolist()
genre = data['Genre'].tolist()
filter = []
non = []

#Menu - put it all together

def main():
    print("Welcome to our Netflix Search! We are here to help you find your ideal movie/s! Let's get started!")
    while True:
        do = input("What would you like to do, would you like to find content based on location, classification, or genre?: ")
        if do == "location" or do == "Location":
            abc = input("What country would you like your show from?: ")
            location(abc)
            hgf = input("Would you like to try again or are you satisfied?: ")
            if hgf == "try again" or hgf == "Try Again" or hgf == "Try again":
                continue
            if hgf == "satisfied" or hgf == "Satisfied":
                break

        if do == "classification" or do == "Classification":
            fed = input("What rating would you prefer?: ")
            classification(fed)
            klj = input("Would you like to try again or are you satisfied?: ")
            if klj == "try again" or klj == "Try Again" or klj == "Try again":
                continue
            if klj == "satisfied" or klj == "Satisfied":
                break
            else:
                break
        if do == "genre" or do == "Genre":
            xyz = input("What is a preferred genre?: ")
            search_genre(xyz)
            omt = input("Would you like to try again or are you satisfied?: ")
            if omt == "try again" or omt == "Try Again" or omt == "Try again":
                continue
            if omt == "satisfied" or omt == "Satisfied":
                break
            else:
                break
        else:
            print("That's not an option. Let's try again!")
            continue


#Functions

#Ask what country
def location(where):
    while True:
        for i in range(len(id)):
            if where == country[i]:
                filter.append(title[i])
                non.append(country[i])
        if where in non:
            selected_item = random.choice(filter)
            print(f"We have selected {selected_item} as something that would appeal to your interests, this content was made in {where}. Hope you enjoy!")
            break
        else:
            print("Sorry that is not an option.")
            break


#Ask for rating
def classification(type):
    while True:
        for i in range(len(id)):
            if type == rating[i]:
                filter.append(title[i])
                non.append(rating[i])
        if type in non:
            selected_item = random.choice(filter)
            print(f"We have selected {selected_item} as something that would appeal to your interests, this content is of classification {type}. Hope you enjoy!")
            break
        else:
            print("Sorry that is not an option.")
            break



#Ask for genre of movie
def search_genre(search):
    while True:
        for i in range(len(id)):
            if search in genre[i]:
                filter.append(title[i])
                non.append(genre[i])
        if search in non:
            selected_item = random.choice(filter)
            print(f"We have selected {selected_item} as something that would appeal to your interests, this content's genre is {search}. Hope you enjoy!")
            break
        else:
            print("Sorry that is not an option.")
            break


main()


#Sources
#Netflix Content
#Website name: code.org
#Url: https://docs.google.com/spreadsheets/d/1GzPPziG7pEvL1XrqO5DewWLU1s12NNbAQ2nqJ5CjUJw/edit?gid=0#gid=0


