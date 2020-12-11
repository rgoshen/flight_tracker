import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/66b68d8e72da89ec872ba57ded11c330/flightDeals/prices"

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        destination_data = response.json()['prices']
        # pprint(destination_data)
        return destination_data

#TODO: POST(add rows) sheet:prices data

#TODO: PUT(update rows) sheet:prices data

#TODO: DELETE sheet:prices data
