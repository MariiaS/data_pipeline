import json

import numpy as np
import requests
from geopy.geocoders import Nominatim


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
        country = np.NaN
    else:
        country = data.address.rsplit(', ', 1)[1]
    return country