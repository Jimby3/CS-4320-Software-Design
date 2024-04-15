# This class is used for...
from RestaurantLists import RestaurantsDoNotRecommend, RestaurantLikes, RestaurantDoNotLike


class User:
    def __init__(self, zipcode):
        self.restaurantLikes = RestaurantLikes
        self.restaurantDoNotLike = RestaurantDoNotLike
        self.restaurantDoNotRecommend = RestaurantsDoNotRecommend
        self.zipcode = zipcode

    def like_restaurant(self, restaurant_name):
        self.restaurantLikes.RestaurantLikes.add_restaurant(restaurant_name)