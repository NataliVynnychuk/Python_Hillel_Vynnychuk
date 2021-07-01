value = 50
new_value = value // 2 if value < 100 else - value
print(new_value)

##################################################

value = 50
new_value = 1 if value < 100 else 0
print(new_value)

##################################################

value = 50
new_value = True if value < 100 else False
print(new_value)

##################################################

my_str = "hillel"
new_str = my_str.upper()
print(new_str)

##################################################

my_str = "HILLEL"
new_str = my_str.lower()
print(new_str)

#################################################

my_str = "qwer"
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)

#################################################

my_str = "qwer"
new_str = my_str + my_str [::-1] if len(my_str) < 5 else my_str
print(new_str)
