#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
mylist = [random.randint(1,9) for i in range(random.randint(4,10))]
print(f"список:\n{mylist}")

#использование enumerate, list comprehension
result = sum([i for count, i in enumerate(mylist) if count % 2 == 1], 0)
print('Сумма элементов списка, стоящих на нечётной позиции равна', result)