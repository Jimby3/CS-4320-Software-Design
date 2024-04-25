# This class is used for holding the data of each restaurant
class Restaurant:
    def __init__(self, name, description, phone_num, price_level, rating, address, website):

        # this function is used to convert price level from 1 to 4, to $ to $$$$
        def price_level_to_dollars(price_level):
            if price_level == 1:
                return '$'
            elif price_level == 2:
                return '$$'
            elif price_level == 3:
                return '$$$'
            elif price_level == 4:
                return '$$$$'
            else:
                return 'N/A'

        self.name = str(name)
        self.description = str(description)
        self.phone_num = str(phone_num)
        self.price_level = price_level_to_dollars(price_level)
        self.rating = str(rating)
        self.address = str(address)
        self.website = str(website)

    # Getter methods
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_phone_num(self):
        return self.phone_num

    def get_price_level(self):
        return str(self.price_level)

    def get_rating(self):
        return self.rating

    def get_address(self):
        return self.address

    def get_website(self):
        return self.website

    def display_restaurant_details(self):
        try:
            print(
                "Name: " + self.name + "\nDescription: " + self.description + "\nPhone: " + self.phone_num +
                "\nAffordability: " + self.price_level + " out of $$$$\nRating: " + self.rating + " Stars\nAddress: " +
                self.address + "\nWebsite: " + self.website + "\n")
        except TypeError as e:
            print("An error occurred while displaying restaurant details:", e)


    def display_restaurant_simple(self):
        try:
            print(
                "Name: " + self.name + "\nAffordability: " + self.price_level + " out of $$$$\nRating: "
                + self.rating + " Stars")
        except TypeError as e:
            print("An error occurred while displaying restaurant details:", e)

    # Search restaurants by name through restaurant array and delete any of the same
