from dateutil.parser import parse
from datetime import datetime


def parse_date(date_string):
    return date_string.strftime("%Y-%m-%d")
