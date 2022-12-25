def inp_menu():
    inp_choice = input('''Чего изволите?
# 1 добавление номера телефона
# 2 посмотреть всех номеров в справочнике
# 3 найти телефон по фамилии
# 4 экспорт в txt файл
# 0 выход
''')
    return inp_choice


def add_number():
    print(f'''Введите данные  через  
    id name last_name  number ''')
    inp_name = input("Введите имя: ").capitalize()
    inp_last_name = input("Введите фамилию: ").capitalize()
    # inp_position = input("Введите номер телефона: ").capitalize()
    inp_number = int(input("Введите номер телефона: "))
    # inp_bonus = int(input("Введите премию: "))
    return inp_name, inp_last_name,  inp_number


def find_number():
    number = input('Введите фамилию, чей телефон хотите найти: ')
    return number


# def find_position():
#     position = input('Введите должность: ')
#     return position


# def change_number():
#     id_number = input('Введите id, которого хотите найти: ')
#     new_number = int(input('Введите новый номер телефона: '))
#     return id_number, new_number


def print_data(inp_str):
    print(inp_str)
