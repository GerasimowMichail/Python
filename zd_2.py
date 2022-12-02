# Найти максимальное из 5ти чисел
print("Максимальное число")
list1=[2, 3, 5, 7, 50, 12]
    
def max_list(arr): 
    max_ = list1[0]
    for ele in list1:
        if ele > max_:
           max_ = ele
    return max_ 


result = max_list(list1)
print(result) 
