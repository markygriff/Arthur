import urllib2
import json
import googlemaps

# pip install -U googlemaps
# Google Maps API: AIzaSyB8geswrT0dfu10cSPnk8n51epy5-t9we0


def get_latlon(loc):
    gmaps = googlemaps.Client(key='AIzaSyB8geswrT0dfu10cSPnk8n51epy5-t9we0')
    geocode_result = gmaps.geocode(loc)

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    latlon = [lat, lon]
    return latlon

if __name__ == '__main__':
    get_latlon("1600 Amphitheatre Parkway, Mountain View, CA")
