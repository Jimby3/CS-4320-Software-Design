# This file is used for managing the decisions the user makes on how they want their food

def select_restaurant_type():
    selection = 0
    valid = False
    while not valid:
        selection = input("Would you like to eat at a Fast Food, Sit Down restaurant, or choose your own category?\n"
                              "1: Fast Food\n2: Sit Down\n3: Own Choice\nEnter Choice: ")
        if selection != '1' and selection != '2' and selection != '3':
            print("\n\n\nInvalid Selection, Please try again:\n\n")
        else:
            valid = True

    restaurant_type = ""
    if selection == '1':
        restaurant_type = "Fast Food"
    elif selection == '2':
        restaurant_type = "Sit Down"
    elif selection == '3':
        restaurant_type = input("Enter the type of restaurant you would like to eat at: ")
    return restaurant_type


def select_decision_type():
    selection = 0
    valid = False
    while not valid:
        selection = input("\nWould you like to get a random restaurant decision or choose from different options?\n"
                              "1: Random\n2: Options\nEnter Choice: ")
        if selection != '1' and selection != '2':
            print("\n\n\nInvalid Selection, Please try again:\n\n")
        else:
            valid = True
    selection = int(selection)
    return selection

