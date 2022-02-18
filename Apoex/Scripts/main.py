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
    if (response.status_code == 200):
        for s in range(len(beer)):
            if beer[s]["name"] == x:
                print("\nBeer of your choice are: {} {}%\nDescription of the beer {}\n{} \n{} \nSome lovely food to eat with {} are: {} ".format(beer[s]["name"],beer[s]["abv"], beer[s]["name"], beer[s]["description"],
                                                                                                           beer[s][
                                                                                                               "tagline"],
                                                                                                           beer[s]["name"],
                                                                                                   beer[s][
                                                                                                               "food_pairing"]))





def choice_A_Beer(x_choice, userC):
    user_choise = str(x_choice)
    Base_url = "https://api.punkapi.com/v2/beers?beer_name={}".format(user_choise)
    print(Base_url)
    r = requests.get(Base_url)
    data = r.json()
    # printing out best food to your choice
    print("The status code is: ", r.status_code)
    Beer_Data = json.dumps(data)  # json.dumps take a dictionary as input and returns a string as output.
    Beer_Data_Test = json.loads(Beer_Data)  # json.loads take a string as input and returns a dictionary as output.
    if (r.status_code == 200):
        print(userC)
        for user_choise in range(len(Beer_Data_Test)):
            if Beer_Data_Test[user_choise]["name"] == userC:
                print(
                    "\nBeer of your choice are: {} {}%\nDescription of the beer {}\n{} \n{} \nSome lovely food to eat with {} are: {} ".format(
                        Beer_Data_Test[user_choise]["name"],
                        Beer_Data_Test[user_choise]["abv"],
                        Beer_Data_Test[user_choise]["name"],
                        Beer_Data_Test[user_choise]["description"],
                        Beer_Data_Test[user_choise]["tagline"],
                        Beer_Data_Test[user_choise]["name"],
                        Beer_Data_Test[user_choise]["food_pairing"]))




# Find all of an element the user is looking for
def Find_All_Off_Type(x_choice):
    user_choise = str(x_choice)
    Base_url = "https://api.punkapi.com/v2/beers?beer_name={}".format(user_choise)

    print(Base_url)
    # Searching for alternatives within API
    r = requests.get(Base_url)
    data = r.json()
    print("The status code is: ", r.status_code)
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
                print("\n\n")
                print("Nothing here")
                print("\n\n")

        else:
            print("\n\n")
            print("Nothing here")
            print("\n\n")

    else:
        print("\n\n")
        print("Something went wrong!")
        print("\n\n")
    print("1: Next page")
    print("2: Choice a beer")
    print("3: Exit")
    user_input = input()
    if (user_input == "1"):
        Secound_Ten(enter_a_beer_type)
        return
    elif (user_input == "2"):
        print("Enter a beer: ")
        choice_of_beer_user_wants = input()
        choice_A_Beer(x_choice, choice_of_beer_user_wants)
    else:
        return

def Secound_Ten(x_choice):
    user_choise = str(x_choice)
    Base_url = "https://api.punkapi.com/v2/beers?beer_name={}".format(user_choise)

    print(Base_url)
    # Searching for alternatives within API
    r = requests.get(Base_url)
    data = r.json()
    print("The status code is: ", r.status_code)
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
                print("\n\n")
                print("Nothing here")
                print("\n\n")

        else:
            print("\n\n")
            print("Nothing here")
            print("\n\n")

    else:
        print("\n\n")
        print("Something went wrong!")
        print("\n\n")
    print("2: Choice a beer")
    print("3: Exit")
    user_input = input()
    if (user_input == "1"):
        Secound_Ten(enter_a_beer_type)
        return
    elif (user_input == "2"):
        print("Enter a beer: ")
        choice_of_beer_user_wants = input()
        choice_A_Beer(x_choice, choice_of_beer_user_wants)
    else:
        return


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
        print("1: Search again for a beer type: ")
        print("2: Check a beer")
        print("3: Exit")

        choice = input()
        if (choice == "1"):
            enter_a_beer_type = input("enter a type of beer: ")
            Find_All_Off_Type(enter_a_beer_type)
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

