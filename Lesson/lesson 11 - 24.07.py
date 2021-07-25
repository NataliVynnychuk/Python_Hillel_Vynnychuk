# json, csv (формат табличных данных, хранит только данные)
# импорт из файла
# assert

import json


def write_json(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data

data_list = [1, 2, 3, 4, 5]
data_dict = {"name": "John",
             "age": 13,
             "job": {"title": "Data Ingener",
                     "price": "1000$"}}

# data_dumps = json.dumps(data_list)
# print(data_dumps, type(data_dumps))
#
# with open("data.json", "w") as json_file:
#     json.dump(data_list, json_file)
#
# with open("data.json", "r") as json_file:
#     new_data = json.load(json_file)
# print(new_data[2], type(new_data))

filename = "data_dict.json"
write_json(filename, data_dict)
data = read_json(filename)
print(data)


