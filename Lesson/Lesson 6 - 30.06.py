# А)
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50]
# my_result = []
# for index in range(len(my_list_1)):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)

########################################

# Б)
# my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# my_list_2 = [10, 20, 30, 40]
# my_result = []
#
# min_len_lists = min(len(my_list_1), len(my_list_2))
#
# for index in range(min_len_lists):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
#
# last_values_list_1 = my_list_1[min_len_lists:]
# last_values_list_2 = my_list_2[min_len_lists:]
#
# my_result = my_result + last_values_list_1 + last_values_list_2
#
# print(my_result)

########################################
# id() - номер объекта в памяти
# my_list = [1, 2, 3]
# print(id(my_list))
# my_list = [2, 3, 4, 5]
# print(id(my_list))
# my_list.append(6)
# print(id(my_list))
########################################
# my_list = [1, 2, 3]
#
# result = []
# print(id(result))
#
# result = result + my_list
# print(id(result))
#
# result += my_list
# print(id(result))

########################################
# value = 10
# value += 2
# print(value)
#
# value = 10
# value = value + 2
# print(value)
########################################
########################################
########################################
###########ГЕНЕРАТОР СПИСКОВ:###########
# сгенерировали список:
# folders = []
# for digit in range(1, 21):
#     folder = f"/tmp/{digit}"
#     folders.append(folder)
# print(folders)

# короткий вариант:
# folders = []
# for digit in range(1, 21):
#     folders.append(f"/tmp/{digit}")
# print(folders)

# folders = [f"/tmp/{digit}" for digit in range(1, 21) if not digit % 3]  # [что? цикл условие]
# print(folders)
#
# symbols = [ord(symbol) for symbol in 'eyuioa']
# print(symbols)
#
# alphabet = [chr(ord_index) for ord_index in range(ord("a"), ord("z") + 1)]
# alphabet = "".join(alphabet)
# print(alphabet)

########################################
########################################
########################################
# МНОЖЕСТВА set - не сохраняет порядок, все элементы уникальные

# my_list = [3, 10, 10, 2, 2, "2", 3, 3, 3, 3, 3, 3]  # {1, 2, 3} - множества
# # my_list_unique = list(set(my_list)) - убирает дубли
# my_set = set(my_list)
# print(my_set)
# my_list_unique = list(my_set)
# print(my_list_unique)
#
# new_set = {1, 2, 3, 54, 54, 54}
# print(new_set)

# my_str = "bla BLA car"
# my_str = my_str.lower()
# res_len = len(set(my_str))
# print(res_len)

# количество букв в строке
# my_str = "qqqqqqqqqqqqqqqqqqqqwweeeeeeeeeeerty"
# for symbol in set(my_str):
#     print(symbol, my_str.count(symbol))

# my_str_1 = "qwerty1234567890"
# my_str_2 = "qweasd123456789"
#
# my_set_1 = set(my_str_1)
# my_set_2 = set(my_str_2)
#
# intersection = my_set_1.intersection(my_set_2)
# print(intersection)
# union = my_set_1.union(my_set_2)
# print(union)
# difference = my_set_1.difference(my_set_2)
# print(difference)
################################################
# СЛОВАРЬ - dict - не гарантирует порядок, все ключи уникальные, остаётся последнее значение
# ключи - любые неизменяемые объекты (число, строка, кортеж)
# значения - любые объекты

# triangle = [[1, 1], [2, 3], [4, -2]]
# print(triangle[1][1])

# triangle = {"A": {"x": 1, "y": 1},
#             "B": {"x": 2, "y": 3},
#             "C": {"x": 4, "y": -2}}
#
# print(triangle["B"]["y"])
# print(triangle)
# key = (1, 2, "qwe")
# test_dict = {11: "qwerty",
#              "11": 12,
#              (1, 2, "qwe"): 'test'}
# print(test_dict[key])  #создает пустой словать

