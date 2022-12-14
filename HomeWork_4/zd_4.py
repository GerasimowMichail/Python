# 4 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
#   Пример:
#           k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
koefs = {}
# k = 15
k = int(input('введите целое число больше 0: '))
for i in range(k + 1):
    # print(i)
    koefs[i] = random.randint(-100, 100)
    # print(koefs[i])
print(koefs)
# {0: 71, 1: 62, 2: 44, 3: 89}
# 89x^3+44x^2
# print(max(koefs.keys()))
max_k = max(koefs.keys())

print(f'Максимальное значение ключа словарей {max(koefs.keys())}')
print(f'Максимальное значение значения словарей {max(koefs.values())}')

out_str = ''
# c = 0
first = True
for i in range(max_k, -1, -1):
    koef = koefs[i]
    pow_x = i
    print(f'Печать ключей словаря {pow_x}, значения элементво {koef}, {koefs[i]}')
    if koef > 0:
        
        if i > 1:
            # if c == 0:
            if first:
                 if koef == 1:
                    out_str += f'x^{pow_x}'
                 elif koef == -1:
                    out_str += f'-x^{pow_x}'    
                
                 else:
                    if koef>0: 
                        out_str += f'{koef}x^{pow_x}'
                    else:
                        out_str += f'-{koef}x^{pow_x}'
                # 89x^3
            else:
                if koef == 1:
                    if koef>0:
                         out_str += f' + x^{pow_x}'
                    else:
                        out_str += f' - x^{pow_x}'       
                # +89x^3
        elif i == 1:
            if first:
                out_str += f'{koef}x'
                # 62x
            else:
                out_str += f' + {koef}x'
                
        else:
            out_str += f' + {koef}'
        # c += 1
        if first:
            first = False
    else :
        out_str = out_str    
   
              
out_str = out_str + " = 0 "             
            
print(out_str)
with open('result.txt', 'w', encoding='utf-8') as fd:
    fd.write(out_str)
    
