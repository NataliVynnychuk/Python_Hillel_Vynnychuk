# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.

import requests
import random
import csv

url = "http://api.forismatic.com/api/1.0/"

def get_raw_quote(quotes, lang="en"):
    quote_list = []
    for request_number in range(quotes):
        params = {"method": "getQuote",
                  "format": "json",
                  "lang": lang,
                  "key": random.randint(1, 999999)}
        response = requests.get(url, params=params)
        quote_json = response.json()
        if not quote_json['quoteAuthor'] == '':
            list_quote = [quote_json['quoteAuthor'], quote_json['quoteText'], quote_json['quoteLink']]
            quote_list.append(list_quote)
    return quote_list

# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

def write_quote_csv(file_csv, data):
    with open(file_csv, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(["Author", "Quote", "URL"])
        writer.writerows(sorted(data, key=lambda x: x[0]))

filename = 'quotes.csv'
list_quotes_autors = get_raw_quote(10)
write_quote_csv(filename, list_quotes_autors)



