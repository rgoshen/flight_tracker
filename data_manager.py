import requests
from pprint import pprint
import os

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/66b68d8e72da89ec872ba57ded11c330/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/66b68d8e72da89ec872ba57ded11c330/flightDeals/users"
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Method for getting spreadsheet data from prices sheet."""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_headers)
        self.destination_data = response.json()['prices']
        return self.destination_data


    def update_destination_codes(self):
        """Method for updating the iata code on price sheet."""
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
