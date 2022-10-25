import random
from pathlib import Path

def polynom(mylist):
    pol = ''
    for i in range(len(mylist)):
        if i < len(mylist) - 2:
            pol += f'{mylist[i]}x^{len(mylist)-i-1} + '
        elif i == len(mylist) - 2:
            pol += f'{mylist[i]}x + '
        elif i == len(mylist) - 1:
            pol += f'{mylist[i]} = 0'
    return pol

k = int(input("Введите степень многочлена (натуральное число): "))
while k < 1:
    k = int(input("Вы ввели не натуральное число, повторите ввод: "))

mylist = [random.randint(0,101) for i in range(k+1)]

p = Path('./hw4/task4/')
file = p / 'file.txt'
with open(file, 'w') as data:
    data.write(polynom(mylist))