# ламбда функция 

func = lambda y: y+2
print(func(5))

# функция filter

my_list = [1, 2, 4, 6, 8, 9, 2]
print(f"старый список {my_list}")
new_list = list(filter(lambda x: (x%3 == 0), my_list))
print(f"новый список, элементы которого деляться на 3 без остатка {new_list}")
print("---"*50)
# функция map

old_list  = [1, 2, 4, 6, 8, 9, 2]
print(f"старый список {old_list}")
new_list = list(map((lambda x: x*2), old_list))
print(f"новый удвоенный список {new_list}")

print("---"*50)
# Спиское включение
print("Списковое включение")
tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    
    print(table(), end = " ")
print("---"*50)

# Функция zip
print("Функция zip")
print("---"*50)
employee_numbers = [1, 10, 20, 30]
employee_work = ["Водитель", "Слесарь", "Монтажник", "Директор"]

zipped_values = zip(employee_numbers, employee_work)
zipped_list = list(zipped_values)
# print(zipped_values)
print(zipped_list)

print("---"*50)

# Функция enumerate
print("Функция enumerate")
print("---"*50)
names = ["Коля", "ТОля", "Катя"]
enumNames = enumerate(names, 1)
print(list(enumNames))
print("---"*50)
# Функция enumerate
print("Функция List comprehension")
print("---"*50)

old_prices = [100, 400, 500, 900]  # Исходный список цен на товары в рублях
print(f'старый список {old_prices}')
discount = 0.1  # Скидка в 10 %
new_prices = [int(product * (1 - discount)) for product in old_prices]  # Вычисляем новые цены (без учета копеек)
print(f'Новый список {new_prices}') 