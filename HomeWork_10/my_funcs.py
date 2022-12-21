def my_sum(x, y):
    return x + y

def my_div(x, y):
    return x / y

def my_sequence(n):
    res_list = []
    for i in range(1, n + 1):
        res_list.append((1+2)**i)
    return res_list

# print(my_sequence(2))
# print(my_sequence(3))
# print(my_sequence(4))
# print(my_sequence(5))

def my_sequence2(n):
    # (1+1/n)**n
    res_list = []
    for i in range(1, n + 1):
        res_list.append((1+1/i)**i)
    return round(sum(res_list), 2)
# print(my_sequence2(6))

# try:
#     print(my_div(5, 1))
# except ZeroDivisionError as err:
#     print(err)
#     print('делить на ноль нельзя')
# except TypeError:
#     print('необходимо вводить числа')