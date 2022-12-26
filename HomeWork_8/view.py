def inp_menu():
    inp_choice = input('''Чего изволите?
# 1 добавление школьника
# 2 посмотреть всех школьников
# 3 найти школьника по фамилии
# 4 найти по номеру школы
# 5 изменить  класс

# 0 выход

''')
    return inp_choice


def add_student():
    print(f'''Введите данные добавляемого учащегося через  
     name last_name школа класс литера''')
    inp_name = input("Введите имя: ").capitalize()
    inp_last_name = input("Введите фамилию: ").capitalize()
    inp_shool = input("Введите школу: ").capitalize()
    inp_klass = int(input("Введите класс: "))
    inp_liter = (input("литер класса: "))
    return inp_name, inp_last_name, inp_shool, inp_klass, inp_liter


def find_student():
    student = input('Введите фамилию школьника, которого хотите найти: ')
    return student


def find_shool():
    shool = input('Введите школу: ')
    return shool


def change_klass():
    id_klass = input('Введите id школьника, класс которого хотите изменить: ')
    new_klass = int(input('Введите класс: '))
    return id_klass, new_klass


def print_data(inp_str):
    print(inp_str)
