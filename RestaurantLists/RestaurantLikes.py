# This class contains an array of restaurant objects that the user chose over the ones in RestaurantDoNotLike
class RestaurantLikes:
    def __init__(self):
        self.liked_restaurants = []

    def add_restaurant(self, restaurant):
        self.liked_restaurants.append(restaurant)