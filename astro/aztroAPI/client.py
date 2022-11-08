import requests

class AztroHoroscope:
    def __init__(self, data):
        self.data = data
        # Example Response
        #  {"current_date": "June 23, 2017", "compatibility": " Cancer", "lucky_time": " 7am", "lucky_number": " 64", "color": " Spring Green", "date_range": "Mar 21 - Apr 20", "mood": " Relaxed", "description": "It's finally time for you to think about just one thing: what makes you happy. Fortunately, that happens to be a person who feels the same way. Give yourself the evening off. Refuse to be put in charge of anything."}

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


