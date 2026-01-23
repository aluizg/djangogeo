import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2

YEALP_SEARCH_ENDPOINT = "https://api.yelp.com/v3/businesses/search"

def yelp_search(keyword=None, location=None):
    if not keyword:
        keyword = 'Pizzaria'

    if not location:
        location = 'Rio de Janeiro'

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + settings.YELP_API_KEY
    }
    params = {
        "term": keyword,
        "location": location,
        "limit": 10,
        "sort_by": "best_match"
    }
    response = requests.get(YEALP_SEARCH_ENDPOINT, headers=headers, params=params)

    return response.json()

def get_client_data():
    geo = GeoIP2()
    ip = get_random_ip()
    try:
        city_data = geo.city(ip)
        return city_data
    except geoip2.errors.AddressNotFoundError:
        return None

def get_random_ip():
    return ".".join(str(randint(0, 255)) for _ in range(4))