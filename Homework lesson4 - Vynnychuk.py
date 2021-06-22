# # ## ДЗ* Сделать такую же програмку, но Давать подсказки, типа: "Попробуй больше", "Попробуй меньше"
# tmp_value = 5
#
# go_game = True
# value = input("Введи число от 1 до 10")
#
# while go_game:
#     if str(tmp_value) == value:
#         go_game = False
#         print("Ура, угадал!")
#     elif str(tmp_value) < value:
#         value = input("Попробуй меньше")
#     elif str(tmp_value) > value:
#         value = input("Попробуй больше")


#################################################
# my_list = [1, 2, 3, 4, 5, 678, 987, 1234, 65, 33, 22]
# for symbol in my_list:
#     if symbol > 100:
#         print(f"symbol: {symbol}")

#################################################
# my_list = [1, 2, 3, 4, 5, 678, 987, 1234, 65, 33, 22]
# my_results = []
# for symbol in my_list:
#     if symbol > 100:
#         my_results.append(symbol)
# print(my_results)

#################################################
# my_list = [1, 2, 3, 4, 5, 678, 987, 1234, 65, 33, 22]
# new_my_list = my_list.append(0) if len(my_list) < 2 >= else my_list.append[::-1+-2]
# print(new_my_list)

my_list = [1, 2, 3, 4, 5, 678, 987, 1234, 65, 33, 22]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list = 5
print(my_list)







