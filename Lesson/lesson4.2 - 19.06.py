# # count = 10
# # while count > 0:
# #     count -= 1
# #     print(f"count {count}")
# # print("The end")
#
# # #     # count += 1 #увеличение на 1
# # #     count -= 1 #уменьшение на 1
#
# ######################################
#
#
#
# #ЦИКЛ for:
# # test_str = "qwerEEty4567"
# # for symbol in test_str:
# #     if symbol.lower() not in "eyuioa" and symbol.isalpha():
# #         print(f"symbol: {symbol}")



# test_str = "qwert.,.,.!ydfgEAtreds"
# result = []
# for symbol in test_str:
#     if symbol.lower() not in "eyaio" and symbol.isalpha():
#         # print(f"symbol: {symbol}")
#         result.append(symbol)
# print(result)

# # join_str = "".join(result)
# # print(join_str)
#
# #tuple - кортеж - неизменяемый тип данных
# #list - список - изменяемый тип данных
# #
# my_tuple = (1, 2, "qwe", (-1,0), None) #кортеж
# print(type(my_tuple), my_tuple)
#
# my_list = [1, 2, "qwe", (-1,0), None] #список
# print(type(my_list), my_list)
# #
# index = 4
# # value_tuple = my_tuple[index]
# # value_list = my_list [index]
# #
# # print(value_tuple, value_list)
#
# my_tuple = list(my_tuple)
# my_tuple[index] = 'NEW_VALUE'
# my_tuple = tuple(my_tuple)
# # my_list[index] = 3
# # print(type(my_list), my_list)
#
# # #срезы как в строках
# #
# # #приведение к типам
# new_list = list(my_tuple)
# new_tuple = tuple(my_list)
# print("new_list", type(new_list), new_list)
# print("new_tuple", type(new_tuple), new_tuple)

# new_list = []
#
# some_value = new_list.append('first')
# new_list.append('second')
# new_list.append('first')
# new_list.append([1,3,5])
# last_value = new_list.pop()
# print(new_list)
# print(last_value, some_value)







