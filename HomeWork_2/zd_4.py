# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

# fruits = ["Apple", "Pear", "Peach", "Banana"]
# prices = [0.35, 0.40, 0.40, 0.28]

# fruit_dictionary = dict(zip(fruits, prices))

# print(fruit_dictionary)

from random import randint


def f_spisok(n):
        spisok = []
        for i in range(0,n):
            spisok.append(randint(-n,n))
        
        return(spisok)
    

def mult(numm):
    mult=1    
    positions = [1,3,6]
    for i in positions:
        if i<=n:
            mult*=numm[i-1]
    return mult

print("Введите N не менее 6-ти символов: ")
n=int(input())
numm=f_spisok(n)
print(numm)
mult_itog=mult(numm)
print(mult_itog)            
    
    


