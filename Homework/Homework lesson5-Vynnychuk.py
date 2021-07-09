# #1
my_number = 543200087650000000
result = str(my_number).count("0")
print(result)
####################################
#2
value = 89302654012032290000
count = 0
for index in str(value)[::-1]:
    if index =='0':
        count+=1
    else:break
print(count)
####################################
#3
my_list_1 = [1, 4, 7, 8, 3, 9, 0]
my_list_2 = [5, 8, 0, 2, 4, 1, 7, 8, 9]
my_result = []
for index, value in enumerate(my_list_1):
    if not index % 2:
        my_result.append(value)
for index, value in enumerate(my_list_2):
    if index % 2:
        my_result.append(value)
print(my_result)

# ИЛИ:

my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)
#####################################
#4
my_list = [1, 2, 3, 4]
new_list = []
for value in my_list[1:]:
    new_list.append(value)
new_list.append(my_list[0])
print(new_list)
#####################################
#5
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)
#####################################
#6
my_str = '20 больше чем 10 но меньше чем 100'
count = 0
for value in my_str.split():
    if value.isdigit():
        count += int(value)
print(count)
#####################################
#7
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)
#####################################
#8
my_str = 'qwertyqwertyr'
if len(my_str) % 2 != 0:
    my_str += "_"
my_list = []
count = 0
while count < len(my_str):
    my_list.append(my_str[count] + my_str[count+1])
    count += 2
print(my_list)
#####################################
#9
my_list = [2,4,1,5,3,9,0,7]
index = 1
count = 0
while index < len(my_list) - 1:
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        count += 1
    index += 2
print(count)


