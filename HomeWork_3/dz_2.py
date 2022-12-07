# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

spisok = [2, 3, 5, 9, 3, 15, 20, 22, 25]
len_sp=len(spisok)
print(f"Длина списка {len_sp}")
sp_2=[]
def mult_list(spisok):   
    mult = 1
    for i in range(int(len_sp/2)):
        mult = spisok[i]*spisok[len_sp-i-1]
        sp_2.append(mult)
    return sp_2

spisok1 = mult_list(spisok)
print(f"Произведение элементов списка: {spisok1}")

