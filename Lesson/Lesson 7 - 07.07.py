# my_str = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"
# print(my_str.swapcase())

# result_1 = []
# for symbol in my_str:
#     if symbol.islower():
#         result_1.append(symbol)
# # result_1 = [symbol for symbol in my_str if symbol.isupper()]
# str_1 = "".join(result_1)
# print(str_1)
#
# str_2 = ""
# for symbol in my_str:
#     if symbol.islower() and symbol not in "aeyiuo":
#         str_2 += symbol
# print(str_2)
#
# str_3 = ""
# for symbol in my_str:
#     if symbol.islower():
#         str_3 += symbol.upper()
#     elif symbol.isupper():
#         str_3 += symbol.lower()
#     else: str_3 += symbol
# print(str_3)
#
#
# big_letters = []
# little_a_letter = []
# little_b_letter = []
# symbols = []
#
# for symbol in my_str:
#     if symbol.isupper():
#         big_letters.append(symbol)
#     elif symbol.islower() and symbol in "etyuoa":
#         little_a_letter.append(symbol)
#     elif symbol.islower() and symbol not in "etyuoa":
#         little_a_letter.append(symbol)
#     else:
#         symbols.append(symbol)
# result = sorted(big_letters) + sorted(little_a_letter) + sorted(little_b_letter) + symbols
# res_str = "".join(result)
# print(res_str)


