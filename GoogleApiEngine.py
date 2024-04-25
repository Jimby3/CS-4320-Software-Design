from googleplaces import GooglePlaces, types

from RestaurantLists.NotSortedRestaurants import NotSortedRestaurants
from Restaurant import Restaurant


api_key = 'PUT_YOUR_API_KEY_HERE'
google_places = GooglePlaces(api_key)

# this class handles the API calling for out app.
class GoogleApiEngine:
    def __init__(self, location, restaurant_type):
        self.location = location
        self.restaurant_type = restaurant_type

    def makeAPIRequest(self):
        try:
            # Attempt to make a nearby search API request using Google Places API.
            query_result = google_places.nearby_search(
                location=self.location, keyword=self.restaurant_type,
                radius=3200, types=[types.TYPE_FOOD])
        except ValueError or TypeError:
            # If an error occurs (ValueError or TypeError), print a message and quit the application.
            print("Unable to find location, quitting app...")
            quit()

        # Create an empty list to store restaurant objects.
        restaurant_list = NotSortedRestaurants()

        # Iterate through each place returned by the API query result.
        for place in query_result.places:
            # Retrieve detailed information about the place.
            place.get_details()

            # Create a Restaurant object using retrieved details.
            restaurant = Restaurant(
                place.name,
                place.details.get('editorial_summary', {}).get('overview'),
                place.details.get('formatted_phone_number'),
                place.details.get('price_level'),
                place.details.get('rating'),
                place.formatted_address,
                place.details.get('website')
            )

            # Add the created restaurant object to the list.
            restaurant_list.add_to_array(restaurant)

        # Remove any duplicate restaurants from the list.
        restaurant_list.remove_duplicates()

        # Return the list of restaurants.
        return restaurant_list

# API Legend

# googleplaces.GooglePlaces
#   nearby_search(**kwargs)
#     Returns googleplaces.GooglePlacesSearchResult
#       kwargs:
#         keyword  -- A term to be matched against all available fields, including but
#                     not limited to name, type, and address (default None)
#
#         language -- The language code, indicating in which language the results
#                     should be returned, if possble. (default en)
#
#         lat_lng  -- A dict containing the following keys: lat, lng (default None)
#
#         location -- A human-readable location, e.g 'London, England' (default None)
#
#         name     -- A term to be matched against the names of the Places.
#                     Results will be restricted to those containing the passed name value. (default None)
#
#         pagetoken-- Optional parameter to force the search result to return the next
#                     20 results from a previously run search. Setting this parameter
#                     will execute a search with the same parameters used previously. (default None)
#
#         radius   -- The radius (in meters) around the location/lat_lng to restrict
#                     the search to. The maximum is 50000 meters (default 3200)
#
#         rankby   -- Specifies the order in which results are listed:
#                     'prominence' (default) or 'distance' (imply no radius argument)
#
#         sensor   -- Indicates whether the Place request came from a device
#                     using a location sensor (default False)
#
#         type     -- An optional type used for restricting the results to Places (default None)
#
#         types    -- An optional list of types, restricting the results to Places (default []).
#                     This kwarg has been deprecated in favour of the 'type' kwarg.
