# this class will hold an array of restaurants that weren't picked over the ones in RestaurantLikes
class RestaurantDislikes:
    def __init__(self):
        self.disliked_restaurants = []

    def add_restaurant(self, restaurant):
        self.disliked_restaurants.append(restaurant)
