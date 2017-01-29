# Dependencies:
#   pip install python-google-places

from googleplaces import GooglePlaces, types, lang

API_key = 'AIzaSyA4fllD-4FhUKiUYUdoJwRzCfn-riQMsU8'
google_places = GooglePlaces(API_key)
LOCATION = 'Edmonton'

def get_places_restaurant(k=None):

    query_result = google_places.nearby_search(
        location=LOCATION,
        keyword=k,
        radius=1000,
        types=[types.TYPE_RESTAURANT,types.TYPE_FOOD])

    # if query_result.has_attributions:
    #     print query_result.html_attributions

    for place in query_result.places:
        place.get_details()
        print place.name
        print place.geo_location
        # print place.place_id
        #
        # # The following method has to make a further API call.
        # place.get_details()
        # # Referencing any of the attributes below, prior to making a call to
        # # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        # print place.details # A dict matching the JSON response from Google.
        # print place.local_phone_number
        # print place.international_phone_number
        # print place.website
        # print place.url

def get_places_health(k=None):

    query_result = google_places.nearby_search(
        location=LOCATION,
        keyword=k,
        radius=1000,
        types=[types.TYPE_DOCTOR,types.TYPE_HEALTH,types.TYPE_DENTIST,types.TYPE_PHARMACY])

    # if query_result.has_attributions:
    #     print query_result.html_attributions

    for place in query_result.places:
        place.get_details()
        print place.name
        print place.geo_location

if __name__ == '__main__':
    # get_places_restaurants('Asian')
    get_places_health()
