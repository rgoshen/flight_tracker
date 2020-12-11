from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        print(f"{row['id']} has no iata code")
