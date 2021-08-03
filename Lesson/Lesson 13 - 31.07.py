#Модуль requests
import requests
import random

def get_raw_quote(lang="ru"):
    url = "https://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "lang": lang,
              "key": random.randint(1,999999)}
    response = requests.get(url, params=params)
    return response.json()

def get_quote(raw_qoute):
    return raw_qoute['quoteText']

def get_autor(raw_qoute):
    return raw_qoute['quoteAutor']

for request_number in range(10):
    raw_quote = get_raw_quote()
    quote = get_quote(raw_quote)
    print(raw_quote)






