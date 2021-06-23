# value = input("Введи число")

# my_list = [1, 2, 3]
# new_list = [my_list.copy(), my_list.copy(), my_list.copy()]
# print(new_list)
# new_list[0].append(4)
# print(my_list)
# print(new_list)

# tmp_value = 5
#
# go_game = True
# text_message = "Введи число от 1 до 10"
#
# while go_game:
#     try:
#         value = int(input(text_message))
#         if tmp_value > value:
#             text_message = "Попробуй больше"
#         elif tmp_value < value:
#             text_message = ("Попробуй меньше")
#         else:
#             go_game = False
#             print("Ура, угадал!")
#     except ValueError:
#         text_message = "Введи число от 1 до 10"


# my_str = "blablacarblablacar" #условие
# my_symbol = "bla"

# my_symbol_count = my_str.count(my_symbol)
# print(my_symbol_count)
#
# ####################################
#
# print(f"{my_symbol}\n" * my_symbol_count) #2 вариант
# # for _ in range(my_symbol_count):  #1 вариант
# #      print(my_symbol)
#
# res_msg = f"{my_symbol}\n" * my_symbol_count #3 вариант
# print(res_msg.strip())
####################################
# my_str = "bla BLA car"
# my_str = my_str.lower()
# symbols_heap = []
# for symbol in my_str:
#     if symbol not in symbols_heap:
#         symbols_heap.append(symbol)
# res_len = len(symbols_heap)
# print(res_len)

####################################
# my_str = "qwerty"
# my_list = []
# for index in range(len(my_str)):
#     if not index % 2:
#         symbol = my_str[index]
#         my_list.append(symbol)
# print(my_list)

#2 подход

# my_str = "qwerty"
# my_list = []
#
# # for index, symbol in enumerate(my_str):
# #     if not index % 2:
# #         my_list.append(symbol)
# #
# # print(my_list)
#
# ####################################
# for value in enumerate(my_str):
#     print(value)

######################################
# my_str = "qwerty"
# my_list = []
# str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
#
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

#####################################
my_number = 45678087654567808765456999780876545678
# digit_count = len(str(my_number))
# print(digit_count)

#####################################

# number_str = str (my_number)
# max_symbol = max(number_str)
# print(max_symbol)

#####################################
# number_str = str(my_number)
# new_number_str = number_str[::-1]
# new_number = int(new_number_str)
# print(new_number)
#
# new_number = int(str(my_number)[::-1])
# print(new_number)
#####################################
#
# my_list = [1, 2, 5, 3, -8 ,4]
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)
#
# my_list = [1, 2, 5, 3, -8 ,4]
# my_str = 'qwerty'
# sorted_list = sorted(my_str)
# print(sorted_list)

#####################################

number_str = str(my_number)
sorted_number_symbols_list = sorted(number_str, reverse=True)
new_number_str = ''.join(sorted_number_symbols_list)
new_number = int(new_number_str)
print(new_number)
















