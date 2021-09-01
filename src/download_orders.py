import requests
import pprint
import json

from secrets import BASELINKER_TOKEN


def download_orders():
    url = "https://api.baselinker.com/connector.php"

    params = {"status_id": 238258}  # Nowe Allegro
    data = {
        "token": BASELINKER_TOKEN,
        "method": "getOrders",
        "parameters": json.dumps(params)
    }

    response = requests.post(url, data=data)

    return response.json()
