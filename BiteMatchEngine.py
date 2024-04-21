import User
from DecisionLogic import random_decision_logic, choice_decision_logic
from MethodSelection import select_restaurant_type, select_decision_type
import GoogleApiEngine


# This class is used for...
class BiteMatchEngine:

    def __init__(self):
        print()

    def start_engine(self):

        user = User.User()

        if user.location == "":
            user.set_location(input("Please Enter Your Location (Address, Zipcode, or City):\n"))

        else:

            valid = False
            while not valid:
                print("Your Location is: " + user.get_location())
                selection = input("Would you like to change your location? y/n\n")
                if selection != 'y' and selection != 'n':
                    print("\n\n\nInvalid Selection, Please try again:\n\n")
                else:
                    valid = True

            if selection == 'y':
                user.set_location(input("Please Enter Your Location:\n"))

        restaurant_type = select_restaurant_type()

        decision_type = select_decision_type()

        # calling API to get 20 restaurants based on the zipcode and type
        api_engine = GoogleApiEngine.GoogleApiEngine(user.get_location(), restaurant_type)

        # returns unsorted list of restaurants from NotSortedRestaurants class, with no duplicates
        user.set_not_sorted(api_engine.makeAPIRequest())
        user.get_not_sorted().remove_DNR_restaurants(user)

        if len(user.get_not_sorted().get_not_sorted()) == 0:
            print("No Restaurants Found.")
            self.stop_engine(user)

        if decision_type == 1:
            do_over = True
            while do_over:
                chosen, remaining_restaurants = random_decision_logic(user)

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
                    print("\nNo Restaurants Remaining!")
                    do_over = False


        elif decision_type == 2:

            chosen = choice_decision_logic(user)
            print("\n")
            chosen.display_restaurant_details()

        else:
            print("Error, Decision type not valid")
            self.stop_engine(user)

        self.stop_engine(user)

    def stop_engine(self, user):
        print("\n\nStopping app...")

        with open("Database/DNR_temp_db.txt", 'w') as file:
            for restaurant_name in user.get_DNR_restaurants():
                file.write(restaurant_name + ", ")

        with open("Database/User_Location_Temp_db.txt", 'w') as file:
            file.write(user.get_location())

        quit()