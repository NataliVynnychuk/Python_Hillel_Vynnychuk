import random
import string

# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ["qwe", "rty", "asd", "zxc"]

def do_task_1(my_list):
    new_list = []
    for index, value in enumerate(my_list):
        if not index % 2:
            new_list.append(value)
        if index % 2:
            new_list.append(value[::-1])
    return new_list

res1 = do_task_1(my_list)
print(res1)

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

my_list = ["qwe", "ray", "asd", "zxaac"]

def do_task_2(my_list):
    new_list = [value for value in my_list if value.startswith("a")]
    return new_list
res2 = do_task_2(my_list)
print(res2)

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["qaae", "rty", "wsd", "zaaac"]

def do_task_3(my_list):
    new_list = []
    for value in range(len(my_list)):
        if "a" in my_list[value]:
            new_list.append(my_list[value])
    return new_list

res3 = do_task_3(my_list)
print(res3)

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33, "qwe", 0]

def do_task_4(my_list):
    new_list = []
    for index in range(len(my_list)):
        if type (my_list[index]) == str:
            new_list.append(my_list[index])
    return new_list

res4 = do_task_4(my_list)
print(res4)

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "qwe123asdqwe"

def do_task_5(my_str):
    new_list = []
    for symbol in set(my_str):
        if my_str.count(symbol) == 1:
            new_list.append(symbol)
    return new_list

res5 = do_task_5(my_str)
print(res5)

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "qwerty123"
my_str_2 = "qwertyasdfgh"

def do_task_6(my_str_1, my_str_2):
    my_list = []
    my_set_1 = set(my_str_1)
    my_set_2 = set(my_str_2)
    intersection = my_set_1.intersection(my_set_2)
    my_list = list(intersection)
    return my_list
res6 = do_task_6(my_str_1, my_str_2)
print(res6)

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = "Моя первая строка"
my_str_2 = "Моя вторая строка"

def do_task_7(my_str_1, my_str_2):
    new_list = []
    for symbol in set(my_str_1).intersection(set(my_str_2)):
        if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
            new_list.append(symbol)
    return new_list

res7 = do_task_7(my_str_1, my_str_2)
print(res7)

 # 8. Даны списки names и domains.txt (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
names = ["petr", "lola", "viktor"]
domains = ["net", "com", "ua"]

def create_email(names, domains):
    random_name = random.choice(names)
    random_value = random.randint(100, 999)
    random_domains = random.choice(domains)
    str_letters = string.ascii_lowercase
    my_str_letters = ''.join(random.choice(str_letters) for letter in range(random.randrange(5, 8)))
    random_email = f"{random_name}.{random_value}@{my_str_letters}.{random_domains}"
    return random_email

e_mail = create_email(names, domains)
print(e_mail)


