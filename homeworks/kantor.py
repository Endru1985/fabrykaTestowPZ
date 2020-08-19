import requests as r
from datetime import datetime


response = r.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json')

print(response.json())