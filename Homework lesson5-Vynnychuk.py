# #1
# value = 8930265401203220000000056
# result = list(str(value)).count("0")
# print(result)
####################################
#2
# value = 893026540120322000000
# count = 0
# for index in str(value)[::-1]:
#     if index =='0':
#         count+=1
#     else:break
# print(count)

####################################
#3
# my_list_1 = [1, 4, 7, 8, 3, 9, 0]
# my_list_2 = [5, 8, 0, 2, 4, 1, 7, 8, 9]
# my_result = []
# for index, value in enumerate(my_list_1):
#     if not index % 2:
#         my_result.append(value)
# for index, value in enumerate(my_list_2):
#     if index % 2:
#         my_result.append(value)
# print(my_result)

# ИЛИ:

# my_result = my_list_1[::2] + my_list_2[1::2]
# print(my_result)

#####################################
# #4
# my_list = [1, 2, 3, 4]
# new_list = []
# for value in my_list[1:]:
#     new_list.append(value)
# new_list.append(my_list[0])
# print(new_list)

#####################################
#5
# my_list = [1, 2, 3, 4, 5]
# my_list.append(my_list.pop(0))
# print(my_list)

#####################################
#6
my_str = '20 больше чем 10 но меньше чем 100'
int_sum = 0
for value in my_str.split():
    if value.isdigit():
        int_sum += int(value)
print(int_sum)

#####################################


