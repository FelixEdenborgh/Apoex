import requests
import json


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
    print("The status code is: ", response.status_code)
    print("halloj")
    if (response.status_code == 200):
        for s in range(len(beer)):
            if beer[s]["name"] == x:
                print("\nBeer of your choice are: {} {}%\nDescription of the beer {}\n{} \n{} \nSome lovely food to eat with {} are: {} ".format(beer[s]["name"],beer[s]["abv"], beer[s]["name"], beer[s]["description"],
                                                                                                           beer[s][
                                                                                                               "tagline"],
                                                                                                           beer[s]["name"],
                                                                                                           beer[s][
                                                                                                               "food_pairing"]))
# Find all of an element the user is looking for
def Find_All_Off_Type(x_choice):
    user_choise = str(x_choice)
    Base_url = "https://api.punkapi.com/v2/beers?beer_name={}".format(user_choise)

    print(Base_url)
    # Searching for alternatives within API
    # problemet är att den inte lägger till min parameter efter url:en
    r = requests.get(Base_url)
    data = r.json()
    print("The status code is: ", r.status_code)
    # hitta något sätt att lära ut datan från din dict samt att den också ska gå efter user choice. Dvs väljer du "ada" så ska den skriva ut allt med ada inuti.
    state = 0
    Beer_Data = json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    Beer_Data_Test = json.loads(Beer_Data) # json.loads take a string as input and returns a dictionary as output.
    if (r.status_code == 200):
        for user_choise in Beer_Data_Test[:10]:
            if (user_choise in Beer_Data_Test):
                print(user_choise['name'], user_choise['abv'])
                state = state + 1
                if(state == 10):
                    break

            else:
                print("Nothing here")

        else:
            print("Nothing here")

    else:
        print("Something went wrong!")


def Secound_Ten(x_choice):
    user_choise = str(x_choice)
    Base_url = "https://api.punkapi.com/v2/beers?beer_name={}".format(user_choise)

    print(Base_url)
    # Searching for alternatives within API
    # problemet är att den inte lägger till min parameter efter url:en
    r = requests.get(Base_url)
    data = r.json()
    print("The status code is: ", r.status_code)
    # hitta något sätt att lära ut datan från din dict samt att den också ska gå efter user choice. Dvs väljer du "ada" så ska den skriva ut allt med ada inuti.
    state = 0
    Beer_Data = json.dumps(data)  # json.dumps take a dictionary as input and returns a string as output.
    Beer_Data_Test = json.loads(Beer_Data)  # json.loads take a string as input and returns a dictionary as output.
    if (r.status_code == 200):
        for user_choise in Beer_Data_Test[10:20]:
            if (user_choise in Beer_Data_Test):
                print(user_choise['name'], user_choise['abv'])
                state = state + 1
                if (state == 10):
                    break


            else:
                print("Nothing here")

        else:
            print("Nothing here")

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
        print("2: Search again for a beer type: ")
        print("3: Check a beer")
        print("4: Exit")

        choice = input()
        if(choice == "1"):
            # if next page
            Secound_Ten(enter_a_beer_type)
            continue
        elif (choice == "2"):
            enter_a_beer_type = input("enter a type of beer: ")
            Find_All_Off_Type(enter_a_beer_type)
            continue
        elif(choice == "3"):
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

