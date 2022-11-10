"""
PyApod
~~~~~~~

PyApod is a Python Wrapper for apod - Nasa's Astronomy Picture of the Day API

"""

import requests


class Apod(object):
    BASE_URL = "https://api.nasa.gov/planetary/apod?"

    def __init__(
        self,
        date=None,
        start_date=None,
        end_date=None,
        count: int = None,
        thumbs: bool = False,
        api_key: str = "DEMO_KEY",
    ):
        self.date = date
        self.start_date = start_date
        self.end_date = end_date
        self.count = count
        self.thumbs = thumbs
        self.api_key = "api_key=" + api_key
        self.base_url = self.BASE_URL + self.api_key

    def data(self):
        try:
            r = requests.get(url=self.base_url)
            if r.status_code == 200:
                data = r.json()
                return data
        except Exception as e:
            return e
