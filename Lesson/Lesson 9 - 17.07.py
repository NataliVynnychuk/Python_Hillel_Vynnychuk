# Стандартные библиотеки python
# Функции, область видимости, параметры, параметры по умолчанию, типизация

import string
import random
# import random as rnd

#
print(string.ascii_lowercase)

value = random.randint(10, 20)
my_list = [1, 2, 3, 10, 20, 30]
# my_list = [True, False]
my_str = 'qwerty'
choice_from_list = random.choice(my_str)
print(value, choice_from_list)

from random import randint, choice

my_str = 'qwerty'
choice_from_list = choice(my_str)
value = randint(100, 200)
print(value, choice_from_list)

new_list = random.shuffle(my_list) #стандартная ошибка!!!
print(new_list)

new_list = my_list.copy() #shuffle меняет объект!!! поэтому нужен copy
random.shuffle(new_list)
print(my_list, new_list)

########################################################################

#Dry

point_A = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_B = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_C = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

triangle_ABC = {"A": point_A,
                "B": point_B,
                "C": point_C}
print(triangle_ABC)

point_M = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_N = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_K = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

triangle_MNK = {"M": point_M,
                "N": point_N,
                "K": point_K}
print(triangle_MNK)

















