# 2 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

a=int(input("Введите N "))
res=1
sp= []
for i in range(1, a+1):
       res=res*i
       sp.append(res) 
print(sp)
