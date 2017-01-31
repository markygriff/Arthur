# Dependencies:
#   pip install python-google-places

from googleplaces import GooglePlaces, types, lang

API_key = 'AIzaSyA4fllD-4FhUKiUYUdoJwRzCfn-riQMsU8'
google_places = GooglePlaces(API_key)
LOCATION = 'Edmonton'

def get_places_dine(k=None):
    query_result = google_places.nearby_search(
        location=LOCATION,
        keyword=k,
        radius=1000,
        types=[types.TYPE_RESTAURANT,types.TYPE_FOOD])

    # if query_result.has_attributions:
    #     print query_result.html_attributions
    places = []
    for place in query_result.places:
        place.get_details()
        #print place.name
        #print place.geo_location
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
        places.append(str(place.name))
    return places

def get_places_bar(k=None):
    query_result = google_places.nearby_search(
        location=LOCATION,
        keyword=k,
        radius=1000,
        types=[types.TYPE_BAR])

    # if query_result.has_attributions:
    #     print query_result.html_attributions
    places = []
    for place in query_result.places:
        place.get_details()
        #print place.name
        #print place.geo_location
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
        places.append(str(place.name))
    return places

def get_places_health(k=None):
    query_result = google_places.nearby_search(
        location=LOCATION,
        keyword=k,
        radius=1000,
        types=[types.TYPE_DOCTOR,types.TYPE_HEALTH,types.TYPE_DENTIST,types.TYPE_PHARMACY])

    # if query_result.has_attributions:
    #     print query_result.html_attributions
    places = []
    for place in query_result.places:
        place.get_details()
        print place.name
        print place.geo_location['lat']
        print place.website
        places.append(place)
    return places

if __name__ == '__main__':
    # get_places_restaurants('Asian')
    get_places_health()


# """
# Valid types to be optionally used in Google Place query api calls.
#
# @author: sam@slimkrazy.com
# """
#
# TYPE_ACCOUNTING = 'accounting'
# TYPE_AIRPORT = 'airport'
# TYPE_AMUSEMENT_PARK = 'amusement_park'
# TYPE_AQUARIUM = 'aquarium'
# TYPE_ART_GALLERY = 'art_gallery'
# TYPE_ATM = 'atm'
# TYPE_BAKERY = 'bakery'
# TYPE_BANK = 'bank'
# TYPE_BAR = 'bar'
# TYPE_BEAUTY_SALON = 'beauty_salon'
# TYPE_BICYCLE_STORE = 'bicycle_store'
# TYPE_BOOK_STORE = 'book_store'
# TYPE_BOWLING_ALLEY = 'bowling_alley'
# TYPE_BUS_STATION = 'bus_station'
# TYPE_CAFE = 'cafe'
# TYPE_CAMPGROUND = 'campground'
# TYPE_CAR_DEALER = 'car_dealer'
# TYPE_CAR_RENTAL = 'car_rental'
# TYPE_CAR_REPAIR = 'car_repair'
# TYPE_CAR_WASH = 'car_wash'
# TYPE_CASINO = 'casino'
# TYPE_CEMETERY = 'cemetery'
# TYPE_CHURCH = 'church'
# TYPE_CITY_HALL = 'city_hall'
# TYPE_CLOTHING_STORE = 'clothing_store'
# TYPE_CONVENIENCE_STORE = 'convenience_store'
# TYPE_COURTHOUSE = 'courthouse'
# TYPE_DENTIST = 'dentist'
# TYPE_DEPARTMENT_STORE = 'department_store'
# TYPE_DOCTOR = 'doctor'
# TYPE_ELECTRICIAN = 'electrician'
# TYPE_ELECTRONICS_STORE = 'electronics_store'
# TYPE_EMBASSY = 'embassy'
# TYPE_ESTABLISHMENT = 'establishment'
# TYPE_FINANCE = 'finance'
# TYPE_FIRE_STATION = 'fire_station'
# TYPE_FLORIST = 'florist'
# TYPE_FOOD = 'food'
# TYPE_FUNERAL_HOME = 'funeral_home'
# TYPE_FURNITURE_STORE = 'furniture_store'
# TYPE_GAS_STATION = 'gas_station'
# TYPE_GENERAL_CONTRACTOR = 'general_contractor'
# TYPE_GEOCODE = 'geocode'
# TYPE_GROCERY_OR_SUPERMARKET = 'grocery_or_supermarket'
# TYPE_GYM = 'gym'
# TYPE_HAIR_CARE = 'hair_care'
# TYPE_HARDWARE_STORE = 'hardware_store'
# TYPE_HEALTH = 'health'
# TYPE_HINDU_TEMPLE = 'hindu_temple'
# TYPE_HOME_GOODS_STORE = 'home_goods_store'
# TYPE_HOSPITAL = 'hospital'
# TYPE_INSURANCE_AGENCY = 'insurance_agency'
# TYPE_JEWELRY_STORE = 'jewelry_store'
# TYPE_LAUNDRY = 'laundry'
# TYPE_LAWYER = 'lawyer'
# TYPE_LIBRARY = 'library'
# TYPE_LIQUOR_STORE = 'liquor_store'
# TYPE_LOCAL_GOVERNMENT_OFFICE = 'local_government_office'
# TYPE_LOCKSMITH = 'locksmith'
# TYPE_LODGING = 'lodging'
# TYPE_MEAL_DELIVERY = 'meal_delivery'
# TYPE_MEAL_TAKEAWAY = 'meal_takeaway'
# TYPE_MOSQUE = 'mosque'
# TYPE_MOVIE_RENTAL = 'movie_rental'
# TYPE_MOVIE_THEATER = 'movie_theater'
# TYPE_MOVING_COMPANY = 'moving_company'
# TYPE_MUSEUM = 'museum'
# TYPE_NIGHT_CLUB = 'night_club'
# TYPE_PAINTER = 'painter'
# TYPE_PARK = 'park'
# TYPE_PARKING = 'parking'
# TYPE_PET_STORE = 'pet_store'
# TYPE_PHARMACY = 'pharmacy'
# TYPE_PHYSIOTHERAPIST = 'physiotherapist'
# TYPE_PLACE_OF_WORSHIP = 'place_of_worship'
# TYPE_PLUMBER = 'plumber'
# TYPE_POLICE = 'police'
# TYPE_POST_OFFICE = 'post_office'
# TYPE_REAL_ESTATE_AGENCY = 'real_estate_agency'
# TYPE_RESTAURANT = 'restaurant'
# TYPE_ROOFING_CONTRACTOR = 'roofing_contractor'
# TYPE_RV_PARK = 'rv_park'
# TYPE_SCHOOL = 'school'
# TYPE_SHOE_STORE = 'shoe_store'
# TYPE_SHOPPING_MALL = 'shopping_mall'
# TYPE_SPA = 'spa'
# TYPE_STADIUM = 'stadium'
# TYPE_STORAGE = 'storage'
# TYPE_STORE = 'store'
# TYPE_SUBWAY_STATION = 'subway_station'
# TYPE_SYNAGOGUE = 'synagogue'
# TYPE_TAXI_STAND = 'taxi_stand'
# TYPE_TRAIN_STATION = 'train_station'
# TYPE_TRAVEL_AGENCY = 'travel_agency'
# TYPE_UNIVERSITY = 'university'
# TYPE_VETERINARY_CARE = 'veterinary_care'
# TYPE_ZOO = 'zoo'
#
# # The following types supported by the Places API when sending
# # Place Search requests. These types cannot be used when adding a new Place.
#
# TYPE_ADMINISTRATIVE_AREA_LEVEL_1 = 'administrative_area_level_1'
# TYPE_ADMINISTRATIVE_AREA_LEVEL_2 = 'administrative_area_level_2'
# TYPE_ADMINISTRATIVE_AREA_LEVEL_3 = 'administrative_area_level_3'
# TYPE_COLLOQUIAL_AREA = 'colloquial_area'
# TYPE_COUNTRY = 'country'
# TYPE_FLOOR = 'floor'
# TYPE_INTERSECTION = 'intersection'
# TYPE_LOCALITY = 'locality'
# TYPE_NATURAL_FEATURE = 'natural_feature'
# TYPE_NEIGHBORHOOD = 'neighborhood'
# TYPE_POLITICAL = 'political'
# TYPE_POINT_OF_INTEREST = 'point_of_interest'
# TYPE_POST_BOX = 'post_box'
# TYPE_POSTAL_CODE = 'postal_code'
# TYPE_POSTAL_CODE_PREFIX = 'postal_code_prefix'
# TYPE_POSTAL_TOWN = 'postal_town'
# TYPE_PREMISE = 'premise'
# TYPE_ROOM = 'room'
# TYPE_ROUTE = 'route'
# TYPE_STREET_ADDRESS = 'street_address'
# TYPE_STREET_NUMBER = 'street_number'
# TYPE_SUBLOCALITY = 'sublocality'
# TYPE_SUBLOCALITY_LEVEL_4 = 'sublocality_level_4'
# TYPE_SUBLOCALITY_LEVEL_5 = 'sublocality_level_5'
# TYPE_SUBLOCALITY_LEVEL_3 = 'sublocality_level_3'
# TYPE_SUBLOCALITY_LEVEL_2 = 'sublocality_level_2'
# TYPE_SUBLOCALITY_LEVEL_1 = 'sublocality_level_1'
# TYPE_SUBPREMISE = 'subpremise'
# TYPE_TRANSIT_STATION = 'transit_station'
#
#
# # autocomplete types
# AC_TYPE_GEOCODE = 'geocode'
# AC_TYPE_ADDDRESS = 'address'
# AC_TYPE_ESTABLISHMENT = 'establishment'
# AC_TYPE_REGIONS = '(regions)'
# AC_TYPE_CITIES = '(cities)'
