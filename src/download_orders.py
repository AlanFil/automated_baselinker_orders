import requests
import pprint
import json


def download_orders():
    pp = pprint.PrettyPrinter()
    url = "https://api.baselinker.com/connector.php"

    params = {"status_id": 238258}
    data = {
        "token": "5352-12216-TJ6JJ5UPWXCUSJ6TYH6AABNHOZZDXR03D69MNHZ8342NOCFYJJNOU1HZ3GYSH8H3",
        "method": "getOrders",
        "parameters": json.dumps(params)
    }

    response = requests.post(url, data=data)
    pp.pprint(response.json())

    return response.json()
