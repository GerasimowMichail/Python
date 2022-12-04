# 5 Реализовать алгоритм перемешивания списка.
# 

from random import randint

def f_spisok(n):
        spisok = []
        for i in range(0,n):
            spisok.append(randint(-n,n))        
        return(spisok)
   
def rand_list(list_1):
    # Создаем копию, поскольку мы не должны изменять оригинал
    list = list_1[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        index_random =randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_random]
        list[index_random] = temp
    # Возвращаем список
    return list



print("Введите длину списка для перемешивания: ")
n=int(input())
list = f_spisok(n)
mixed_list = rand_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)