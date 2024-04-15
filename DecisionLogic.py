import random
from Restaurant import Restaurant


# this function will hold the logic for randomly choosing a restaurant from an array
def random_decision_logic(restaurant_array, user):
    # Check if the array is empty
    if not restaurant_array:
        return -1, -1

    # Generate a random index within the range of the array length
    random_index = random.randint(0, len(restaurant_array) - 1)

    # Retrieve the element at the randomly generated index
    random_element = restaurant_array[random_index]

    # Remove the element at the randomly generated index from the array
    restaurant_array.pop(random_index)

    # Return the retrieved element
    return random_element, restaurant_array


def choice_decision_logic(restaurant_array, user):
    valid = True
    while valid:
        if len(restaurant_array) > 1:

            # selecting two random restaurants from the array + popping them from array
            random_index = random.randint(0, len(restaurant_array) - 1)
            rest1 = restaurant_array[random_index]
            restaurant_array.pop(random_index)
            random_index = random.randint(0, len(restaurant_array) - 1)
            rest2 = restaurant_array[random_index]
            restaurant_array.pop(random_index)

            # displaying restaurant information for user to choose
            print("\n====================\nRestaurant 1:")
            rest1.display_restaurant_simple()
            print("====================\n\nOr\n\n====================\nRestaurant 2:")
            rest2.display_restaurant_simple()
            print("====================")

            # managing restaurants based on decision
            answer = False
            while not answer:
                selection = input("\nWhich restaurant would you rather go to?"
                                  "\nEnter 1 or 2: ")
                if selection != "1" and selection != "2":
                    print("Invalid selection. Try again. \n")
                else:
                    answer = True

            # START HERE
            # WRITE LOGIC TO IMPLEMENT THE CHOSEN RESTAURANT GETS ADDED TO LIKES
            # BEGIN PROMPTING ACROSS APP IF USERS NEVER WANTS THAT RESTAURANT RECOMMENDED AGAIN





        else:
            valid = False
            user.restaurantLikes.add_restaurant(restaurant_array[0])

        choice = "hi"
        return choice
