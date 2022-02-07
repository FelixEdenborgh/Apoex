import requests
import json

session = requests.session()


def jprint(obj):
    # create a formatted string of the Python Json Object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
#jprint(response.json())

# All beer names
def name():
    r = requests.get("https://api.punkapi.com/v2/beers")
    data = r.json()
    items = []
    for item in data:
        items.append(item['name'])
    print("beers you can choice: ", items)


# the choise of the user
def User_choice(x):
    response = requests.get("https://api.punkapi.com/v2/beers")
    beer = response.json()
    # printing out best food to your choice
    for s in range(len(beer)):
        if beer[s]["name"] == x:
            print("\nBeer of yourchoice are: {}\nDescription of the beer {}\n{} \n{} \nSome lovely food to eat with {} are: {} ".format(beer[s]["name"], beer[s]["name"], beer[s]["description"],
                                                                                                       beer[s][
                                                                                                           "tagline"],
                                                                                                       beer[s]["name"],
                                                                                                       beer[s][
                                                                                                           "food_pairing"]))
# Find all of an element the user is looking for
def Find_All_Off_Type(x_choice):
    PARAMS = {'?beer_name=': x_choice}
    # Searching for alternatives within API
    r = requests.get(url="https://api.punkapi.com/v2/beers", params=PARAMS)
    data = r.json()
    if(r.status_code == 200):
        for s in range(len(data[:10])):
            print("\n {} \n Alcohol content {} ".format(data[s]["name"], data[s]["abv"]))

    else:
        print("Something went wrong!")




def Secound_Ten(x_choice):
    PARAMS = {'?beer_name=': x_choice}
    # Searching for alternatives within API
    r = requests.get(url="https://api.punkapi.com/v2/beers", params=PARAMS)
    data = r.json()
    if (r.status_code == 200):
        for s in range(len(data[10:20])):
            print("\n {} \n Alcohol content {} ".format(data[s]["name"], data[s]["abv"]))

    else:
        print("Something went wrong!")



play = True

while(play == True):
    print("\n")
    print("Welcome to PUNK API beer choice!!!")
    print("1: Search for a beer type: ")
    print("2: Choice a beer: ")
    print("3: Exit")

    search = input(": ")

    if(search == "1"):
        enter_a_beer_type = input("enter a type of beer: ")
        Find_All_Off_Type(enter_a_beer_type)
        print("\n")
        print("1: Next Page")
        print("2: Check a beer")
        print("3: Exit")

        choice = input()
        if(choice == "1"):
            # if next page
            Secound_Ten(enter_a_beer_type)
            continue
        elif(choice == "2"):
            name()
            to_find = input("Enter the name of the beer: ")
            User_choice(to_find)
            continue
        else:
            print("Shop will now close Have a lovely day!")
            play = False
            break

    elif(search == "2"):
        name()
        to_find = input("Enter the name of the beer: ")
        User_choice(to_find)
        continue

    else:
        print("Shop will now close have a nice day!")
        play = False
        break



