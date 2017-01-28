# Dependencies:
# pip install pyowm

import sys
import pyowm

API_key = '276f7913122c3e77188086d23a78d00b'
owm = pyowm.OWM(API_key)
LOCAL = 'London,uk'
WEATHER = None
FORECAST = None
CONDITIONS = ['temperature','clouds','rain','snow','wind','humidity',]
DETAILS = {
"temperature":None
"clouds":None,
"rain":None,
"snow":None,
"wind":None,
"humidity":None
}

def get_API_key():
    return '276f7913122c3e77188086d23a78d00b'

def get_temperature():
    return DETAILS['temperature']

def get_clouds():
    return DETAILS['clouds']

def get_rain():
    return DETAILS['rain']

def get_snow():
    return DETAILS['snow']

def get_wind():
    return DETAILS['wind']

def get_humidity():
    return DETAILS['humidity']

def set_weather_details():
    DETAILS = {"temperature":WEATHER.get_temperature('celsius')
    "clouds":WEATHEREATHER.get_clouds(),
    "rain":WEATHER.get_rain(),
    "snow":WEATHER.get_snow(),
    "wind":WEATHER.get_wind(),
    "humidity":WEATHER.get_humidity()
    }
    return details

def set_local(l):
    LOCAL = l

def set_forecast(num_days):
    '''
    sets global forecast for specified number of days
    '''
    FORECAST = owm.daily_forecast(LOCAL, limit=num_days)

def main():
    '''
    Theoretically, what we want is an interaction like:
        Arthur: Hello, I know shit about weather
        User: What's the weather in Edmonton, Alberta right now?
        Arthur: (retrieves info about current weather in Edmonton)
        Arthur: Here's the weather in Edmonton Alberta....
    '''
    # gonna need to do some str parsing
    LOCAL = raw_input("Enter a location... ")

    # if len(owm.city_id_registry().ids_for(LOCAL)) > 1:
    #     print("Which", LOCAL, "would you like?")
    #     for i in owm.city_id_registry().ids_for(LOCAL):
    #         print i,
    #     chocie = raw_input("Choose by index: ")
    #     LOCAL = owm.city_id_registry().ids_for(LOCAL)[choice][1]

    w = get_weather() # get a weather object for LOCAL
    print "Details about the weather in", LOCAL, "..."
    set_weather_details()
    for cond in CONDITIONS: print cond, DETAILS[cond]

if __name__ == '__main__':
    main()
