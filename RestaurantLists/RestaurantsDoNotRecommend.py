# this class will hold an array of restaurant objects that should never be recommended again.
class RestaurantDoNotRecommend():
    def __init__(self):
        self.not_rec_restaurants = []

    def add_restaurant(self, restaurant):
        self.not_rec_restaurants.append(restaurant)