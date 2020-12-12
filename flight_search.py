import requests
from flight_data import FlightData
import os
from pprint import pprint

TEQUILA_API_KEY = os.environ.get("TEQULIA_FLIGHT_TRACKER")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
HEADERS = {"apikey":TEQUILA_API_KEY}

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_names):
        """Method for sending query of city name and returns iata code."""
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        for city in city_names:
            query = {"term":city, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=HEADERS, params=query)
            results = response.json()["locations"]
            iata_code = results[0]["code"]
            self.city_codes.append(iata_code)

        return self.city_codes


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Method to query API for flight information."""
        print(f"Check flights triggered for {destination_city_code}")
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=HEADERS,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code} {data['price']}")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=HEADERS,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
