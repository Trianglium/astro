import requests

class AztroHoroscope:
    def __init__(self, data, sign):
        self.data = data
        self._sign = ""

    @property
    def sign(self):
        return self._sign
    
    @sign.setter
    def sign(self, new_sign: str):
        self._sign = new_sign

    @property
    def current_date(self):
        return self.data["current_date"]
    
    @property
    def compatibility(self):
        return self.data["compatibility"]
    
    @property
    def lucky_time(self):
        return self.data["lucky_time"]

    @property
    def lucky_number(self):
        return self.data["lucky_number"]

    @property
    def color(self):
        return self.data["color"]

    @property
    def date_range(self):
        return self.data[ "date_range"]

    @property
    def mood(self):
        return self.data["mood"]

    @property
    def description(self):
        return self.data["description"]
    

    def __str__(self):
        if self.current_date:
            return f'{self.sign} ({self.current_date})'
        
        return self.sign


class AztroClient:
    AZTRO_API_URL = "https://aztro.sameerkumar.website/"

    def __init__(self, zodiac_sign: str):
        self._zodiac_sign = zodiac_sign
    
    @property
    def zodiac_sign(self):
        return self._zodiac_sign
    
    @zodiac_sign.setter
    def zodiac_sign(self, new_zodiac_sign):
        self._zodiac_sign = new_zodiac_sign
    
    def make_request(self):
        params["sign"] = self.zodiac_sign
        params["day"] = "today"

        resp = requests.get(self.AZTRO_API_URL, params=params)

        resp.raise_for_status()
        return resp
    
    def set_horoscope(self):
        AztroHoroscope()

