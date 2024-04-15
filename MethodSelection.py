# This class is used for managing the decisions the user makes in their choice
def select_restaurant_type():
    selection = 0
    valid = False
    while not valid:
        selection = input("Would you like to eat at a Fast Food or a Sit Down restaurant?\n"
                              "1: Fast Food\n2: Sit Down\nEnter Choice: ")
        if selection != '1' and selection != '2':
            print("\n\n\nInvalid Selection, Please try again:\n\n")
        else:
            valid = True

    restaurant_type = ""
    if selection == '1':
        restaurant_type = "Fast Food"
    elif selection == '2':
        restaurant_type = "Sit Down"
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
