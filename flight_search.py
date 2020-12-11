import requests
from requests.api import request
from pprint import pprint

TEQUILA_API_KEY = "EBR-IlNX4Arr1GUabbien9oJCgFoJcyt"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    
    def get_destination_code(self, city_name):
        """Method for sending query of city name and returns iata code."""
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {
            "term":city_name,
            "location_types": "city"
        }
        location_headers = {"apikey":TEQUILA_API_KEY}

        response = requests.get(url=location_endpoint, headers=location_headers, params=query)
        results = response.json()["locations"]
        iata_code = results[0]["code"]
        return iata_code
