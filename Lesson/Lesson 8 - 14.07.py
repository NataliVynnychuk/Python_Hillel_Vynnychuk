# #МЕТОДЫ СЛОВАРЕЙ:
#
symbols = {symbol: ord(symbol) for symbol in 'eyuioa'}
# print(symbols)
#
persons = {"John": 12, "Jack": 34, "Anna": 27}
# print(persons["Anna"])
#
persons ["Jackob"] = 59
# persons["John"] = 4
# # persons.clear()
# # persons = {}
# # print(persons.get("Vova", 1000))
#
result = "Anna" in persons #in проверяет только ключи!!!
# print(result)
#
key = "Anna"
# if key not in persons:
#     persons[key] = 41
#
# print(persons)
#
for key in persons:
    print(key, persons[key])
value = persons.pop("Jackob")
print(">>>>>", value)
for key, value in persons.items():
    print(key, value)

print(type(persons.keys()), persons.keys())

max_age = max(persons.values())
print("\m\\a\\x_\\a\\g\\e")

value = input()
print(value)

##########################################
# 2 часть
# persons = {"John": 12, "Jack": 34}
# persons_other = {"Anna": 42, "Jack": 64}
#
# persons_result = {}
# persons_result.update(persons)
# persons_result.update(persons_other) #распаковка словарей
#
# # persons_result = {**persons, **persons_other} #2 метод
# print(persons_result)

products = [{"name": "water", "price": 12, "title": "Bonaqua"},
            {"name": "bread", "price": 7, "title": "Baton"},
            {"name": "bread", "price": 9, "title": "WhiteBread"},
            {"name": "apple", "price": 25, "title": "Golden"}]

bread_prices = []
for product in products:
    if product["name"] == 'bread':
        product['price'] = product['price'] * 1.1 - 1
        # bread_prices.append(product['price'])
print(products)























