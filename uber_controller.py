# Uber Ride Request
#  pip install uber-rides
# http://stackoverflow.com/questions/11960602/how-to-add-something-to-pythonpath
# https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python

# Startup Edmonton Lat/Lon = 53.545830, -113.499032
# Butterdome Lat/Lon = 53.523279, -113.527407

from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import json
import google_geocode


def get_prices(start, end):
    start_latlon = google_geocode.get_latlon(start)
    end_latlon = google_geocode.getlatlon(end)
    session = Session(server_token='2L2ejAw48Rafdg9S9gGnm1yL9AfpcPUSak3YONWF')
    client = UberRidesClient(session)

    result = [];
    response = client.get_price_estimates(
        # start_latitude=53.545830,
        # start_longitude=-113.499032,
        # end_latitude=53.523279,
        # end_longitude=-113.527407,
        start_latitude = start_latlon[0]
        start_longitude = start_latlon[1]
        end_latitude = end_latlon[0]
        end_longitude = end_latlon[0]
    )

    estimation = response.json.get('prices')

    for i in range(len(estimation)):
         result.append(estimation[i]["display_name"] + ": " + estimation[i]["estimate"])

    return result


if __name__ == "__main__":
    main()
