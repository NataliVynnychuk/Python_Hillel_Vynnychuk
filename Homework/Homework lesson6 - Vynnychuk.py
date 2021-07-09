# 1
my_list = ["qwe", "rty", "asd", "zxc"]
new_list = []
for index, symbol in enumerate(my_list):
    if not index % 2:
        new_list.append(symbol)
    if index % 2:
        new_list.append(symbol[::-1])
print(new_list)
#######################################
# 2
my_list = ["qwe", "ray", "asd", "zxaac"]
new_list = []
for symbol in my_list:
    if symbol.startswith("a"):
        new_list.append(symbol)
print(new_list)
#######################################
# 3
my_list = ["qaae", "rty", "wsd", "zaaac"]
new_list = []
for index in range(len(my_list)):
    if "a" in my_list[index]:
        new_list.append(my_list[index])
print(new_list)
#######################################
# 4
my_list = [1, 2, 3, "11", "22", 33, "qwe", 0]
new_list = []
for index in range(len(my_list)):
    if type (my_list[index]) == str:
        new_list.append(my_list[index])
print(new_list)
#######################################
# 5
my_str = "qwe123asd"
my_list = []
my_set = set(my_str)
my_list = list(my_set)
print(my_list)

# ИЛИ:

my_str = "qwe123asd"
new_list = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        new_list.append(symbol)
print(new_list)
#############################
# 6
my_str_1 = "qwerty123"
my_str_2 = "qwertyasdfgh"
my_list = []
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
intersection = my_set_1.intersection(my_set_2)
my_list = list(intersection)
print(my_list)
#############################
# 7
my_str_1 = "Моя первая строка"
my_str_2 = "Моя вторая строка"
new_list = []
for symbol in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        new_list.append(symbol)
print(new_list)
#############################
# 8
my_person = {"Фамилия": "Винничук",
             "Имя": "Наталия",
             "Возраст": "27",
             "Проживание": {"Страна": "Украина",
                            "Город": "Днепр",
                            "Улица": "Паникахи"},
             "Работа": {"Наличие": "Имеется",
                        "Должность": "Админ"}}
print(my_person)
##############################
# 9
recipe = {"Коржи": {"Мука": 500,
                    "Молоко": 200,
                    "Масло": 50,
                    "Яйцо": 100},
           "Крем": {"Сахар": 100,
                    "Масло": 50,
                    "Ванииль": 10,
                    "Сметана": 500},
        "Глазурь": {"Какао": 50,
                    "Сахар": 100,
                    "Масло": 100}}
print(recipe)
##############################
