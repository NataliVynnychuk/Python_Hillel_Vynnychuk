# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
import os
import string

def get_data(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
        return data

# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
#  и возвращает их в виде списка строк (названия возвращать без точки).

def get_domains(filename):
    list_domains = [value.replace(".", "").replace("\n", "") for value in get_data("domains.txt")]
    return list_domains

print(get_domains("domains.txt"))

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

def get_names(filename):
    list_names = [value.split("\t")[1] for value in get_data("names.txt")]
    return list_names

print(get_names("names.txt"))

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]

months_dict = {"January" : "01",
               "February": "02",
               "March": "03",
               "April": "04",
               "May": "05",
               "June": "06",
               "July": "07",
               "August": "08",
               "September": "09",
               "October": "10",
               "November": "11",
               "December": "12"}


def get_list_date(filename):
    original_date = [date.split(" -")[0] for date in get_data(filename) if date[0].isdigit() and date.split(" -")[0][-1].isdigit()]
    return original_date


def get_day(filename):
    list_day = [date.split(" ")[0].rstrip("nsthrd") for date in get_list_date(filename)]
    day_modified_list = []
    for day in list_day:
        if len(day) == 1:
            day_modified_list.append("0" + day)
        else:
            day_modified_list.append(day)
    return day_modified_list


def get_months(filename):
    list_months = [date.split(" ")[1] for date in get_list_date(filename)]
    months_modified_list = [months_dict[months] for months in list_months]
    return months_modified_list


def get_years(filename):
    list_years = [date.split(" ")[2] for date in get_list_date(filename)]
    return list_years


def get_dicts(filename):
    date_original = [{"date_original": date} for date in get_list_date(filename)]
    date_modified = ["/".join(data) for data in list(zip(get_day(filename), get_months(filename), get_years(filename)))]
    for index, date in enumerate(date_original):
        date["date_modified"] = date_modified[index]
    return date_original


print(get_dicts("authors.txt"))

