# область видимости в классах


################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
from string import ascii_lowercase as alphabet


class WorkWithFiles:
    def __init__(self, dirname="alphabet"):
        self._dirname = dirname
        self._create_dir()

    def _create_dir(self):
        os.makedirs(self._dirname, exist_ok=True)

    def _create_file(self, symbol):
        filename = f"{self._dirname}/{symbol}.txt"
        with open(filename, 'w') as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def create_files_in_dir(self):
        for letter in alphabet:
            self._create_file(letter)

    def get_tanos_click(self):
        files = os.listdir(self._dirname)
        files = list(set(files))[:len(files) // 2]
        for file in files:
            os.remove(os.path.join(self._dirname, file))


file_worker = WorkWithFiles("qwe")
# file_worker.create_files_in_dir()
# file_worker.get_tanos_click()




# import csv
#
#
# class ReadCSV:
#     def __init__(self, filename, mode="reader"):
#         self.filename = filename
#         if mode == "dict_reader":
#             self._csv_mode = csv.DictReader
#         else:
#             self._csv_mode = csv.reader
#
#     def read_from_csv(self):
#         with open(self.filename, 'r') as csv_file:
#             reader = self._csv_mode(csv_file, delimiter=",")
#             data = []
#             for row in reader:
#                 data.append(row)
#             return data
#
#
#
# csv_reader = ReadCSV("new_data.csv", mode="dict_reader")
# data = csv_reader.read_from_csv()
# print(data)



# наследование в классах
import json


class JsonReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_json()

    def read_json(self):
        with open(self.filename, "r") as json_file:
            data = json.load(json_file)
            return data

    def __repr__(self):
        return f"{self.filename}"


class JsonWorkerList(JsonReader):
    def __init__(self, filename, limit):
        super().__init__(filename)
        self.data = self.data[:limit]

    def sort(self):
        self.data.sort()


class JsonWorkerDict(JsonReader):
    def sort(self):
        keys = sorted(self.data.keys())
        self.data = {key: self.data[key] for key in keys}

    def __repr__(self):
        return f"Dict filename: {super().__repr__()}"


json_worker_list = JsonWorkerList("data_list.json", 3)
json_worker_dict = JsonWorkerDict("data_dict.json")
print(json_worker_list)
print(json_worker_dict)
json_worker_list.sort()
json_worker_dict.sort()
print(json_worker_list.data)
print(json_worker_dict.data)

json_worker = JsonReader("data_dict.json")
print(json_worker)