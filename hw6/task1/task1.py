#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#БЫЛО
#number = int(input('Введите число: ')) 
#mylist = []
#for i in range(1, number + 1):
#    mylist.append(round((1 + 1 / i) ** i, 2))        
#print(mylist)
#print(round(sum(mylist), 2))

#СТАЛО: используем List comprehension
mylist = [round((1 + 1 / i) ** i, 2) for i in range(1, int(input('Введите число: ')) + 1)] 
print(mylist)
print(round(sum(mylist), 2))