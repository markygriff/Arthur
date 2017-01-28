# Uber Ride Request
#  pip install uber-rides
# http://stackoverflow.com/questions/11960602/how-to-add-something-to-pythonpath

# Startup Edmonton Lat/Lon = 53.545830, -113.499032
# Butterdome Lat/Lon = 53.523279, -113.527407

from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import json


def get_products(client):
    result = [];
    response = client.get_products(37.77, -122.41)
    products = response.json.get('products')


    for i in range(len(products)):
        result.append(products[i]["description"])

    return result


def get_prices(client):
    result = [];
    response = client.get_price_estimates(
        start_latitude=53.545830,
        start_longitude=-113.499032,
        end_latitude=53.523279,
        end_longitude=-113.527407,
    )

    estimation = response.json.get('prices')

    for i in range(len(estimation)):
         result.append(estimation[i]["display_name"] + ": " + estimation[i]["estimate"])

    return result


def main():
    uber_fn_dict = {"Prices": get_prices, "Products": get_products}

    session = Session(server_token='2L2ejAw48Rafdg9S9gGnm1yL9AfpcPUSak3YONWF')
    client = UberRidesClient(session)

    uinput = raw_input("How can uber help you today? ")

    run_fn = uber_fn_dict[uinput]
    result = run_fn(client)

    for i in range(len(result)):
        print result[i];


if __name__ == "__main__":
    main()
