# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

import random
import re

str_1 = open('text_1.txt', 'r')
str_2 = open('text_2.txt', 'r')
str_1 = str_1.readline()
str_2 = str_2.readline()

pattern1 = r'([+-]?\d+)x\^?(\d*)|(\d*)=0$'
pattern2 = r'([+-]?\d+)x\^?(\d*)|(\d*)=0$'

output1 = re.compile(pattern1)
output2 = re.compile(pattern2)
result_1 = output1.findall(str_1)
result_2 = output2.findall(str_2)

print(f"result = {str_1}")
print(f"result = {str_2}")
print("+++++")
res_dict = dict()
res_dict_1 = dict()
res_dict_2 = dict()

for i in result_1:
    if i[1]:
        res_dict_1[int(i[1])] = int(i[0])
    elif i[1] == '' and i[0]:
        res_dict_1[1] = int(i[0])
    elif i[2]:
        res_dict_1[0] = int(i[2])
        
print(res_dict_1)

for i in result_2:
    if i[1]:
        res_dict_2[int(i[1])] = int(i[0])
    elif i[1] == '' and i[0]:
        res_dict_2[1] = int(i[0])
    elif i[2]:
        res_dict_2[0] = int(i[2])
        
print(res_dict_2)

k = len(res_dict_1)
# print(len(res_dict_1))
# print(k)
# for i in range(k):
#     res_dict.values[i] = res_dict_1.values(i) + res_dict_2.values(i) 
#     # print(res_dict_1([i][]), end=' ')   
#     # print(res_dict_2.get(i), end=" ")  
#     # print( k,v )
#     print(res_dict.values[i])
    
for i in range(k, 0, -1):
    # res_dict(i)  = res_dict_1.get([i]) + res_dict_2([i])
# print(res_dict.keys())


# '54x^4-22x^3+34x^2+5x+18=0'
# k = 3
# res_dict = dict()
# res_dict[2] = random.randint(0, 100)
# # res_dict = {
# #     3: 22,
# #     2: 34,
# #     1: 5,
# #     0: 18
# # }
# out = ''
# for k in res_dict:
#     out += f'{res_dict[k]}x^{k}'

# [18, 5, 34, -22, 54]
# [5, 0, 73, 14, 0]
# [23, 5, 107, -8, 54].reverse()

# res_list = []
# key_list = []
# max_x = 0
# for i in result:
#     try:
#         koef = float(i[0])
#     except ValueError:
#         continue
#     if i[1]:
#         x1 = i[1]
#         x1 = x1.replace('x^', '')
#         if x1.isdigit() and int(x1) > max_x:
#             max_x = int(x1)
#         key_list.append(x1)
#     res_list.append(koef)
#
#
# print(res_list)
# print(key_list)
# print(max_x)
#
# # [54.0, -22.0, 34.0, 5.0, 18.0]
# # {:+f} 