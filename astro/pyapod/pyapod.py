"""
PyApod
~~~~~~~

PyApod is a Python Wrapper for apod - Nasa's Astronomy Picture of the Day API

"""

import requests
import datetime




class Apod(object):
    BASE_URL = 'https://api.nasa.gov/planetary/apod?'
    def __init__(self, date=None, start_date=None, end_date=None, count: int = None, thumbs: bool = False, api_key: string = "DEMO_KEY"):
        self.date = date
        self.start_date = start_date
        self.end_date = end_date
        self.count = count
        self.thumbs = thumbs
        self.api_key = 'api_key='+api_key
        self.base_url = self.BASE_URL + self.api_key
        try:
            r = requests.post(url=base_url, params=params)
            if r.status_code is 200:
                data = r.json()
            else:
                print("could not get a response")
