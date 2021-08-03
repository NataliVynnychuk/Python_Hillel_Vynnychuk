# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

import json
import re

def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data

filename = "data.json"
data = read_json(filename)
print(data)

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_by_name(filename):
    name = filename["name"].split(" ")[-1]
    return name

sorted_name = sorted(data, key=sort_by_name)
print(sorted_name)

#3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def sort_by_date_of_death(filename):
    year = filename["years"]
    date_of_death = re.findall(r'\d+', year)
    if "BC" in date_of_death:
        return int(date_of_death[-1] + [-2])
    else:
        return int(date_of_death[-1])

sorted_by_date_of_death = sorted(data, key=sort_by_date_of_death)
print(sorted_by_date_of_death)

# 4. Написать функцию сортировки по количеству слов в поле "text"

def sort_by_word_count(filename):
    word_count = filename["text"]
    words = word_count.split(" ")
    len_text = len(words)
    return len_text

sorted_by_word_count = sorted(data, key=sort_by_word_count)
print(sorted_by_word_count)
