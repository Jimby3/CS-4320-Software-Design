import User
from DecisionLogic import random_decision_logic, choice_decision_logic
from MethodSelection import select_restaurant_type, select_decision_type
import GoogleApiEngine


# This class is used for...
class BiteMatchEngine:

    def __init__(self):
        print()

    def start_engine(self):

        user = User

        restaurant_type = select_restaurant_type()

        decision_type = select_decision_type()

        # need to get this from user
        zipcode = 60140

        # need to get this from decisions above
        restaurant_type = 'fast food'

        # calling API to get 20 restaurants based on the zipcode and type
        api_engine = GoogleApiEngine.GoogleApiEngine(zipcode, restaurant_type)

        # returns unsorted list of restaurants from NotSortedRestaurants class
        restaurant_list = api_engine.makeAPIRequest()

        if decision_type == 1:
            do_over = True
            while do_over:
                chosen, remaining_restaurants = random_decision_logic(restaurant_list.not_sorted_restaurants, user)

                if chosen != -1:

                    print('\n')
                    chosen.display_restaurant_details()

                    valid = False
                    while not valid:
                        redo = input("\nDo you want to swap the restaurant you got?"
                                     "\nEnter YES or NO: ")
                        if redo.upper() == "YES" or redo.upper() == "NO":
                            valid = True
                        else:
                            print("\n\nInvalid input. Please try again.")
                    if redo.upper() == "NO":
                        do_over = False
                        print("\nEnjoy your food!")

                else:
                    print("\nNo Restaurants Remaining! STOP BEING SO PICKY")
                    do_over = False





        elif decision_type == 2:

            chosen = choice_decision_logic(restaurant_list.not_sorted_restaurants, user)

        else:
            print("Error, Decision type not valid")
            quit()

    def stop_engine(self):
        print()
