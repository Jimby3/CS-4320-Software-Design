from googleplaces import GooglePlaces, types

from RestaurantLists.NotSortedRestaurants import NotSortedRestaurants
from Restaurant import Restaurant

api_key = 'AIzaSyDbQ9LeTfjQjIwnEdkw4Q2gDihco9gUj0U'
google_places = GooglePlaces(api_key)


class GoogleApiEngine:
    def __init__(self, zipcode, restaurant_type):
        self.zipcode = zipcode
        self.restaurant_type = restaurant_type

    def makeAPIRequest(self):
        query_result = google_places.nearby_search(
            location=self.zipcode, keyword=self.restaurant_type,
            radius=3200, types=[types.TYPE_FOOD])

        restaurant_list = NotSortedRestaurants()

        for place in query_result.places:
            place.get_details()

            restaurant = Restaurant(place.name, place.details.get('editorial_summary', {}).get('overview'),
                                    place.details.get('formatted_phone_number'), place.details.get('price_level'),
                                    place.details.get('rating'), place.formatted_address, place.details.get('website'))

            restaurant_list.add_to_array(restaurant)

        return restaurant_list

        # # Access details directly as a dictionary
        # print(place.name)
        # print(place.details.get('editorial_summary', {}).get('overview'))
        # print(place.details.get('formatted_phone_number'))
        # print(place.details.get('price_level'))
        # print(place.details.get('rating'))
        # print(place.details.get('website'))
        # print(place.formatted_address)

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
#         location -- A human readable location, e.g 'London, England' (default None)
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
#         sensor   -- Indicates whether or not the Place request came from a device
#                     using a location sensor (default False)
#
#         type     -- An optional type used for restricting the results to Places (default None)
#
#         types    -- An optional list of types, restricting the results to Places (default []).
#                     This kwarg has been deprecated in favour of the 'type' kwarg.
