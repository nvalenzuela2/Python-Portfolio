#Natalia
#Dog Breed
#The purpose of my prgram is to help users choose a dog breed that meets their needs
#Init
import webbrowser
import pandas as pd
data = pd.read_csv('dog.csv')

id = data['id'].tolist()
name = data['Name'].tolist()
breed_group = data['Breed Group'].tolist()
bredfor = data['BredFor'].tolist()
min_life = data['Minimum Life Span'].tolist()
max_life = data['Maximum Life Span'].tolist()
min_height = data['Minimum Height'].tolist()
max_height = data['Maximum Height'].tolist()
min_weight = data['Minimum Height'].tolist()
max_weight = data['Maximum Height'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()
filter = []

#Functions

def weight_finder():
    weight = input("Would you like your dog tiny, small, medium, or large?: ")
    if weight == "tiny":
        for i in range(len(name)):
            if min_weight[i] <= 10:
                filter.append(name[i])
        print(f"Here is a list of tiny dogs that we recommend you get: {filter}")
        filter.clear()
    if weight == "small":
        for i in range(len(name)):
            if 25 >= min_weight[i] >= 11:
                filter.append(name[i])
        print(f"Here is a list of small dogs that we recommend you get: {filter}")
        filter.clear()
    if weight == "medium":
        for i in range(len(name)):
            if 60 >= min_weight[i] >= 26:
                filter.append(name[i])
        print(f"Here is a list of medium sized dogs that we recommend you get: {filter}")
        filter.clear()
    if weight == "large":
        for i in range(len(name)):
            if min_weight[i] >= 61:
                filter.append(name[i])
        print(f"Here is a list of large dogs that we recommend you get: {filter}")
        filter.clear()
    main()
def breed(dogs):
    for i in range(len(name)):
        if dogs == name[i]:
            filter.append(temperament[i])
            webbrowser.open(image[i])
        else:
            print("Dog not found in our system")
    print(f"Here is the temperament and image of the dog you have chosen: {filter}")
    filter.clear()
    main()

def preference(specific):
    for i in range(len(name)):
        if specific in bredfor[i]:
            filter.append(name[i])
    print(f"We would recommend you this/these dogs based on your preference: {filter}")
    filter.clear
    main()

def main():
    while True:
        ask = input("Welcome to Dog Finder! Do you have a specifc weight in mind and want a list of dogs based on weight, do you have a dog in mind and want to know their temperament, or do you want a list of dogs based on a certain purpose? (weight, temperament, or purpose)(type exit to leave): ")
        if ask == "weight":
            weight_finder()
        if ask == "temperament":
            temp = input("What type of dog are you looking for?: ")
            breed(temp)
        if ask == "purpose":
            purp = input("What purpose would you like to search for?: ")
            preference(purp)
        if ask == "exit":
            break

#Main
main()


#Sources
#Mr.J shared this data with us
#Dataset Source Information:
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
