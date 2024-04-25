# this class is where the restaurants will first live after pulling them down from the API, with methods to remove
# duplicates and blacklists
class NotSortedRestaurants:
    def __init__(self):
        self.not_sorted_restaurants = []

    # getting the array
    def get_not_sorted(self):
        return self.not_sorted_restaurants

    # appending to the array
    def add_to_array(self, restaurant):
        self.not_sorted_restaurants.append(restaurant)

    # removing from array by name
    def remove_from_array(self, restaurant):
        self.not_sorted_restaurants.remove(restaurant)

    # removing duplicate names from array
    def remove_duplicates(self):
        checked_restaurants = set()
        unique_restaurants = []
        for restaurant in self.not_sorted_restaurants:
            if restaurant.name not in checked_restaurants:
                checked_restaurants.add(restaurant.name)
                unique_restaurants.append(restaurant)
        self.not_sorted_restaurants = unique_restaurants

    # read in info from file that has blacklisted restaurants and remove them
    def remove_DNR_restaurants(self, user):
        # Create a set of restaurant names to remove for faster lookup
        DNR_names = set(user.doNotRecommendRestaurants)
        # Create a new list to hold the restaurants that are not in DNR list
        remaining_restaurants = []

        # Iterate over restaurants and add them to remaining_restaurants if they're not in DNR list
        for restaurant in self.not_sorted_restaurants:
            if restaurant.name not in DNR_names:
                remaining_restaurants.append(restaurant)

        # Replace the original list with the new list
        self.not_sorted_restaurants = remaining_restaurants

    def  print_not_sorted(self):
        for restaurant in self.not_sorted_restaurants: print(restaurant.name)