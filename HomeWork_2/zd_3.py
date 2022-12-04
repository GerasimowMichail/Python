# 3 Задать список из n чисел последовательности (1+ 1/n )**n и вывести на экран их сумму n

n=int(input("Введите N "))
sp=[]
summ=0
for i in range(1, n+1):
       res=round(((1+1/i)**i),3)
       summ=summ+res
       sp.append(res) 
print(sp)
print(summ)
