# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
persons = [{"name": "John", "age": 15},
           {"name": "Anna", "age": 30},
           {"name": "Vova", "age": 25},
           {"name": "Kristina", "age": 20},
           {"name": "Jack", "age": 15}]

age_list = [list(items.values())[1] for items in persons]
long_name = [list(items.values())[0] for items in persons]

#а)
for items in persons:
    if list(items.values())[1] == min(age_list):
        print(list(items.values())[0])
#б)
for name in long_name:
    if len(name) == len(max(long_name, key=len)):
        print(name)
#в)
average_age = sum(age_list) // len(age_list)
print(average_age)

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},


my_dict_1 = {1:11, 5:21, 3:33}
my_dict_2 = {1:44, 4:55, 3:22}

#а)
list_keys = list(set(my_dict_1).intersection(set(my_dict_2)))
print(list_keys)

#б)
new_list_keys = list(set(my_dict_1).difference(my_dict_2))
print(new_list_keys)

#в)
new_dict = {key: value for key, value in my_dict_1.items() if key not in my_dict_2}
print(new_dict)

#г)
my_new_dict = {}

my_dicts = [my_dict_1, my_dict_2]
for dict in my_dicts:
    for key, value in dict.items():
        if my_new_dict.get(key) is None:
            my_new_dict[key] = value
        else:
            my_new_dict[key] = [dict[key] for dict in my_dicts if key in dict]
print(my_new_dict)


