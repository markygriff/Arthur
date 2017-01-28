from googleplaces import GooglePlaces, types, lang

API_key = 'AIzaSyA4fllD-4FhUKiUYUdoJwRzCfn-riQMsU8'
google_places = GooglePlaces(API_key)

query_result = google_places.nearby_search(
    location='London', keyword='Restaurants',
    radius=1000, types=[types.TYPE_RESTAURANT])

if query_result.has_attributions:
print query_result.html_attributions


for place in query_result.places:
    place.get_details()
    print place.rating

if __name__ == '__main__':
    pass
