import json

import pandas as pd
import requests
from geopy.geocoders import Nominatim

df = pd.read_csv("../data/hb/2021/04/28/hb.csv")


def get_address_from_ip(ip_address):
    url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(url)
    data = response.content.decode()
    data = data.split("(")[1].strip(")")
    initial_string = json.dumps(data)
    return json.loads(initial_string)


def get_country_from_city_state(street, city, postcode):
    locator = Nominatim(user_agent="geoapi")
    data = locator.geocode(city + " " + street)
    if data is None:
        data = locator.geocode(postcode)
    if data is None:
        country = ""
    else:
        country = data.address.rsplit(', ', 1)[1]
    return country


if __name__ == '__main__':
    print(df.head())
    print(get_address_from_ip('0.0.0.0'))
    print(get_country_from_city_state('', 'westminster', ''))
