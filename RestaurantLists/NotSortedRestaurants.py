import Restaurant

# this class is where the restaurants will first live after pulling them down from the API
class NotSortedRestaurants:
    def __init__(self):
        self.not_sorted_restaurants = []

    def add_to_array(self, restaurant):
        self.not_sorted_restaurants.append(restaurant)