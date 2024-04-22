import random


# this function will hold the logic for randomly choosing a restaurant from an array
def random_decision_logic(user):
    # Check if the array is empty
    restaurant_array = user.get_not_sorted().get_not_sorted()
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


def choice_decision_logic(user):
    while True:
        restaurant_array = user.get_not_sorted().get_not_sorted() or user.get_restaurant_likes()

        if len(restaurant_array) <= 1:
            if len(restaurant_array) == 1:
                user.like_restaurant(restaurant_array[0])
                try:
                    user.get_not_sorted().remove_from_array(restaurant_array[0])
                except ValueError:
                    return restaurant_array[0]
            else:
                return
        else:

            rest1 = random.choice(restaurant_array)
            restaurant_array.remove(rest1)
            rest2 = random.choice(restaurant_array)
            restaurant_array.remove(rest2)

            displayBothRestaurantsSimple(rest1, rest2)


            decision = promptSimpleOptions()

            if decision == 1:
                user.like_restaurant(rest1)
            elif decision == 2:
                user.like_restaurant(rest2)
            else:
                displayBothRestaurantsMoreDetails(rest1, rest2)
                decision = promptComplexOptions()
                if decision == 1:
                    user.like_restaurant(rest1)

                elif decision == 2:
                    user.like_restaurant(rest2)

                elif decision == 3:
                    user.dislike_restaurant(rest1)
                    user.not_sorted_restaurants.add_to_array(rest2)

                elif decision == 4:
                    user.dislike_restaurant(rest2)
                    user.not_sorted_restaurants.add_to_array(rest1)

                elif decision == 5:
                    user.dislike_restaurant(rest1)
                    user.dislike_restaurant(rest2)

                elif decision == 6:
                    num = random.randint(1,2)
                    if num == 1:
                        user.like_restaurant(rest1)
                    else:
                        user.like_restaurant(rest2)





# this function displays both restaurants formatted better
def displayBothRestaurantsSimple(rest1, rest2):
    # Displaying restaurant information for user to choose
    print("\t\t---------------------------------------------------------------------------")
    print("\n\n\t\tRestaurant 1:\t\t\t\t\t\t\t\t\t\tRestaurant 2\t\t")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    print("\t\t{: <40}\t\t\t{: <40}".format(rest1.get_name(), rest2.get_name()))
    print("\t\t{: <4} out of $$$$\t\t\t\t\t\t\t\t\t{: <4} out of $$$$".format(rest1.get_price_level(),
                                                                              rest2.get_price_level()))
    print("\t\t{: <3} out of 5 Stars\t\t\t\t\t\t\t\t\t{: <3} out of 5 Stars\n".format(rest1.get_rating(),
                                                                                    rest2.get_rating()))
    print("\nWhich Restaurant would you rather eat at?")


def displayBothRestaurantsMoreDetails(rest1, rest2):


    print("\t\t---------------------------------------------------------------------------")
    print("\n\n\t\tRestaurant 1:\t\t\t\t\t\t\t\t\t\tRestaurant 2\t\t\n")
    print("\t\t{: <40}\t\t\t{: <40}".format(rest1.get_name(), rest2.get_name()))
    print_long_items(rest1.get_description(), rest2.get_description())
    print("\t\t{: <4} out of $$$$\t\t\t\t\t\t\t\t\t{: <4} out of $$$$".format(rest1.get_price_level(),
                                                                              rest2.get_price_level()))
    print("\t\t{: <3} out of 5 Stars\t\t\t\t\t\t\t\t\t{: <3} out of 5 Stars\n".format(rest1.get_rating(),
                                                                                    rest2.get_rating()))
    print("\t\t{: <40}\t\t\t{: <40}".format(rest1.get_phone_num(), rest2.get_phone_num()))
    print_long_items(rest1.get_address(), rest2.get_address())

    print_long_items(rest1.get_website(), rest2.get_website())



def promptSimpleOptions():
    while True:
        selection = input("\n1) Choose Restaurant 1\n2) Choose Restaurant 2\n"
                          "3) More Options and Details\nEnter Choice:")

        if selection == "1":
            return 1
        elif selection == "2":
            return 2
        elif selection == "3":
            return 3
        else:
            print("Invalid selection. Try again. \n")


# 2 choose, 2 hate, 1 hate both, 1 idc
def promptComplexOptions():
    while True:
        selection = input("\n1) Choose Restaurant 1\n2) Choose Restaurant 2\n"
                          "3) Never Recommend Restaurant 1 Again\n4) Never Recommend Restaurant 2 Again\n"
                          "5) Never Recommend Both Restaurants again\n6) I can't choose\nEnter Choice:")

        if selection == "1":
            return 1
        elif selection == "2":
            return 2
        elif selection == "3":
            return 3
        if selection == "4":
            return 4
        elif selection == "5":
            return 5
        elif selection == "6":
            return 6
        else:
            print("Invalid selection. Try again. \n")

# this function allows for users to print two strings that are long into multiple lines next to eachother for
# better formatting
def print_long_items(item1, item2):

    # Check if website URLs are longer than 51 characters
    if len(item1) > 51 or len(item2) > 51:
        # Split website URLs into chunks of 51 characters
        chunks1 = [item1[i:i + 51] for i in range(0, len(item1), 51)]
        chunks2 = [item2[i:i + 51] for i in range(0, len(item2), 51)]

        # Pad the chunks with empty strings to ensure consistent alignment
        chunks1 += [''] * (3 - len(chunks1))
        chunks2 += [''] * (3 - len(chunks2))

        # Print website URLs side by side
        for chunk1, chunk2 in zip(chunks1, chunks2):
            print("\t\t{: <51} {: <51}".format(chunk1, chunk2))
    else:
        print("\t\t{: <40}\t\t\t{: <40}\n".format(item1, item2))