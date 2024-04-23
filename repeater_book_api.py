import requests

class RepeaterBookAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_repeaters_by_location(self, location):
        url = f'https://api.repeaterbook.com/v1/repeaters/{location}'
        headers = {'x-api-key': self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to retrieve repeaters. Status code: {response.status_code}")
