# Дано число обозначающее день недели. Вывести его название и
# указать является ли он выходным.

print("Введите число обозначающее день недели: ")
a=int(input())
if a==1:
    
    print("Понедельник")
    print("Нет")
elif a==2:
    print("Вторник")
    print("Нет")
elif a==3:
    print("Среда")
    print("Нет")
elif a==4:
    print("Четверг")
    print("Нет")
elif a==5:
    print("Пятница")
    print("Нет")
elif a==6:
    print("Суббота" + " Выходной")
    
elif a==7:
    print("Воскресенье"+" Выходной")
else:
    print("некоректное число")