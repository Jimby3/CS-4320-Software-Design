from RestaurantLists.NotSortedRestaurants import NotSortedRestaurants


class User:
    def __init__(self):
        self.likedRestaurants = []
        self.doNotRecommendRestaurants = []
        self.not_sorted_restaurants = NotSortedRestaurants()

        try:
            with open("Database/DNR_temp_db.txt", "r") as file:
                data = file.read()
                restaurant_names = data.split(',')

                # Remove leading and trailing whitespace from each name and filter out blank names
                self.doNotRecommendRestaurants = [name.strip() for name in restaurant_names if name.strip()]

                # Print each non-blank name
                for name in self.doNotRecommendRestaurants:
                    print(name)

        except FileNotFoundError:
            print("File not found.")

        try:
            with open("Database/User_Location_Temp_db.txt", "r") as file:
                self.location = file.readline()
        except FileNotFoundError:
            self.location = ""

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_not_sorted(self):
        return self.not_sorted_restaurants

    def set_not_sorted(self, restaurant_array):
        self.not_sorted_restaurants = restaurant_array

    def get_restaurant_likes(self):
        return self.likedRestaurants

    def get_DNR_restaurants(self):
        return self.doNotRecommendRestaurants

    def like_restaurant(self, restaurant):
        self.likedRestaurants.append(restaurant)

    def dislike_restaurant(self, restaurant):
        self.doNotRecommendRestaurants.append(restaurant.name)

    def print_restaurant_likes(self):
        for restaurant in self.likedRestaurants: print(restaurant.name)
